"""
param_utils.py

Parameter processing utilities for WOFOST-EW model.
"""

from typing import Dict, Any

# List of keys to copy from para to cropdata
PARAM_KEYS = [
    'TBASEM', 'TEFFMX', 'TSUMEM', 'IDSL', 'DLO', 'DLC', 'TSUM1', 'TSUM2',
    'DVSI', 'DVSEND', 'TDWI', 'LAIEM', 'RGRLAI', 'SPA', 'SPAN', 'TBASE',
    'CVL', 'CVO', 'CVR', 'CVS', 'Q10', 'RML', 'RMO', 'RMR', 'RMS', 'PERDL',
    'CFET', 'DEPNR', 'IAIRDU', 'IOX', 'RDI', 'RRI', 'RDMCR', 'NMINSO', 'NMINVE',
    'NMAXSO', 'NMAXVE', 'PMINSO', 'PMINVE', 'PMAXSO', 'PMAXVE', 'KMINSO',
    'KMINVE', 'KMAXSO', 'KMAXVE', 'YZERO', 'NFIX', 'CRPNAM', 'DTSMTB', 'SLATB',
    'SSATB', 'KDIFTB', 'EFFTB', 'AMAXTB', 'TMPFTB', 'TMNFTB', 'RFSETB', 'FRTB',
    'FLTB', 'FSTB', 'FOTB', 'RDRRTB', 'RDRSTB', 'HDD', 'LDD', 'R95P', 'R10mm',
    'Rx1day', 'PDSI', 'VPD', 'LSTM_MODEL_PATH'
]

def update_cropdata_from_para(cropdata: Dict[str, Any], para: Dict[str, Any]) -> None:
    """
    Update cropdata dictionary with values from para for predefined keys.

    Parameters
    ----------
    cropdata : dict
        Dictionary to be updated (will be modified in-place).
    para : dict
        Source dictionary containing parameter values.

    Returns
    -------
    None
    """
    for key in PARAM_KEYS:
        if key in para:
            cropdata[key] = para[key]
