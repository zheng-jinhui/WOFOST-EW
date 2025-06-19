"""
seed_utils.py

Utility to set global random seeds for reproducibility.
"""

import os
import random
import numpy as np
import tensorflow as tf

def set_seed(seed: int = 300) -> None:
    """
    Set seeds for random, numpy, tensorflow and python environment.

    Args:
        seed (int): Seed value.
    """
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)
