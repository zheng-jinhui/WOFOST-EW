"""
wofost_runner.py

Module to run WOFOST model simulations.
"""

import logging
from typing import Dict, Any
import pandas as pd
from pcse_wofost_ew.input import NASAPowerWeatherDataProvider
from pcse_wofost_ew.models import Wofost71_WLP_FD
from pcse_wofost_ew.base import ParameterProvider
from param_utils import update_cropdata_from_para

logger = logging.getLogger(__name__)

def run_wofost_ew(
    longitude: float,
    latitude: float,
    cropdata: Dict[str, Any],
    para: Dict[str, Any],
    soildata: Dict[str, Any],
    sitedata: Dict[str, Any],
    agromanagement: Any
) -> pd.DataFrame:
    """
    Run WOFOST model with given parameters and return the simulation output as a DataFrame.

    Parameters
    ----------
    longitude : float
        Longitude of the simulation site.
    latitude : float
        Latitude of the simulation site.
    cropdata : dict
        Crop parameter dictionary, will be updated from para.
    para : dict
        Parameter dictionary containing crop parameters and additional info.
    soildata : dict
        Soil parameter dictionary.
    sitedata : dict
        Site parameter dictionary.
    agromanagement : object
        Agro-management schedule object.

    Returns
    -------
    pd.DataFrame
        DataFrame containing WOFOST simulation output.

    Raises
    ------
    Exception
        Raises exception if simulation fails.
    """
    try:
        logger.info(f"Starting WOFOST simulation at lat={latitude}, lon={longitude}")

        # Initialize weather data provider with NASA Power weather data
        weather_provider = NASAPowerWeatherDataProvider(latitude=latitude, longitude=longitude)

        # Update cropdata parameters from para dictionary
        update_cropdata_from_para(cropdata, para)
        logger.debug("Cropdata updated from para.")

        # Prepare model parameters combining crop, soil and site data
        parameters = ParameterProvider(cropdata=cropdata, soildata=soildata, sitedata=sitedata)

        # Initialize WOFOST model instance
        model = Wofost71_WLP_FD(parameters, weather_provider, agromanagement)

        # Run simulation until termination
        model.run_till_terminate()
        logger.info("WOFOST simulation completed successfully.")

        # Retrieve simulation output and convert to DataFrame
        output_df = pd.DataFrame(model.get_output())
        return output_df

    except Exception as e:
        logger.error("WOFOST simulation failed.", exc_info=True)
        raise
