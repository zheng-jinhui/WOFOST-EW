# WOFOST-EW Model Utilities

## Overview

This repository contains modular Python utilities for running and managing WOFOST-EW crop growth simulations.  
WOFOST-EW is an enhanced version of the WOFOST model, integrating extreme weather indices and deep learning-based impact modifiers.

The code is split into three core modules:

- **param_utils.py**: Utility for injecting crop parameters from external sources into WOFOST-compatible format.  
- **wofost_runner.py**: Wrapper function to run WOFOST-EW model with NASA POWER weather and updated parameters.  
- **logger_config.py**: Basic logging setup to enable consistent debugging and runtime reporting.

These modules are designed to be reusable and easily integrated into simulation pipelines for large-scale agricultural modeling.

---

## Modules Description

### param_utils.py

- `update_cropdata_from_para(cropdata, para)`:  
  Copy relevant parameters defined in `PARAM_KEYS` from a user-defined parameter dictionary into a WOFOST `cropdata` dict.

### wofost_runner.py

- `run_wofost_ew(longitude, latitude, cropdata, para, soildata, sitedata, agromanagement)`:  
  Initializes weather provider, updates parameters, runs the model to termination, and returns the simulation output as a pandas DataFrame.

### logger_config.py

- `setup_logging(level=logging.INFO)`:  
  Configure logging format and level for console output (timestamps, log levels, and messages).

---

## Installation

Use Python 3.7 or above. Install required dependencies:

```bash
pip install pcse pandas

## Usage Example
from logger_config import setup_logging
from wofostew_runner import run_wofost_ew

def main():
    # Initialize logging configuration
    setup_logging()

    # Example input parameters (fill with real data accordingly)
    longitude = 120.0
    latitude = 30.0

    # Cropdata dictionary, initially empty or partially filled
    cropdata = {}

    # Example para dictionary, must contain keys defined in param_utils.PARAM_KEYS
    para = {
        'TBASEM': 0,
        'TEFFMX': 45,
        # Add all necessary parameters here...
        'LSTM_MODEL_PATH': "/path/to/lstm_model"
    }

    # Example soil, site data and agromanagement placeholders
    soildata = {}
    sitedata = {}
    agromanagement = {}  # Replace with actual AgroManagement object

    try:
        # Run the model simulation
        simulation_result = run_wofost_ew(longitude, latitude, cropdata, para, soildata, sitedata, agromanagement)

        # Print first few rows of output
        print(simulation_result.head())

    except Exception as e:
        print(f"Simulation failed: {e}")

if __name__ == "__main__":
    main()
