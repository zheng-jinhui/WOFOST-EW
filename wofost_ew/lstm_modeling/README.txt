# LSTM Model Training Utilities

## Overview

This repository contains modular Python utilities for building, training, and tuning an LSTM model for time series regression problems.

The code is split into three core modules:

- **seed_utils.py**: Set random seeds for reproducibility across Python, NumPy, and TensorFlow.  
- **model_builder.py**: Define and compile a flexible 5-layer LSTM model with customizable hyperparameters.  
- **training.py**: Custom scoring function and GridSearchCV wrapper using Leave-One-Out cross-validation for hyperparameter tuning.

These modules are designed to be integrated easily into your own data pipeline and modeling workflow.

---

## Modules Description

### seed_utils.py

- `set_seed(seed: int = 300)`:  
  Set random seeds globally to ensure reproducible training results.

### model_builder.py

- `create_lstm_model(units1, units2, dense_units, dropout, recurrent_dropout, input_shape, learning_rate)`:  
  Build and compile a 5-layer LSTM model with the specified parameters.

### training.py

- `custom_scorer(y_true, y_pred)`:  
  Calculate negative RMSE as a custom scoring metric.  
- `run_grid_search(X, y, input_shape, learning_rate, recurrent_dropout, param_grid, n_jobs=1, verbose=2)`:  
  Run a grid search with Leave-One-Out cross-validation to find the best hyperparameters.

---

## Installation

Use Python 3.7 or above. To install required dependencies, run:

```bash
pip install -r requirements.txt


## Usage Example
from seed_utils import set_seed
from model_builder import create_lstm_model
from training import run_grid_search

# Set random seed for reproducibility
set_seed(300)

# Prepare  data
# X: numpy array with shape (samples, timesteps, features)
# y: numpy array with shape (samples, 1)

input_shape = (1, 7)
learning_rate = 0.001
recurrent_dropout = 0.1

param_grid = {
    'model__units1': [100, 150],
    'model__units2': [50, 75],
    'model__dense_units': [32, 64],
    'model__dropout': [0.2, 0.3],
    'epochs': [50, 100],
    'batch_size': [16, 32]
}

grid_result = run_grid_search(
    X, y, input_shape, learning_rate, recurrent_dropout, param_grid
)

print("Best params:", grid_result.best_params_)
print("Best score (negative RMSE):", grid_result.best_score_)

# Save the best model
best_model = grid_result.best_estimator_.model_
best_model.save('best_lstm_model.h5')
