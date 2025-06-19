"""
logger_config.py

Logging configuration for the WOFOST project.
"""

import logging

def setup_logging(level=logging.INFO) -> None:
    """
    Configure the root logger.

    Parameters
    ----------
    level : int, optional
        Logging level (default is logging.INFO).

    Returns
    -------
    None
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
