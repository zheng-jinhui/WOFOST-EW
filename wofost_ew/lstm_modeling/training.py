"""
training.py

Custom scorer and hyperparameter tuning via GridSearchCV for LSTM model.
"""

import numpy as np
from sklearn.model_selection import LeaveOneOut, GridSearchCV
from sklearn.metrics import make_scorer
from scikeras.wrappers import KerasRegressor
from model_builder import create_lstm_model

def custom_scorer(y_true, y_pred):
    """
    Custom scoring function: negative RMSE.

    Args:
        y_true (array-like): True labels.
        y_pred (array-like): Predicted labels.

    Returns:
        float: Negative RMSE score.
    """
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    return -rmse

def run_grid_search(
    X,
    y,
    input_shape,
    learning_rate,
    recurrent_dropout,
    param_grid,
    n_jobs=1,
    verbose=2
):
    """
    Run GridSearchCV with Leave-One-Out CV to find best hyperparameters.

    Args:
        X (np.ndarray): Input features.
        y (np.ndarray): Target labels.
        input_shape (tuple): Input shape for model.
        learning_rate (float): Learning rate for optimizer.
        recurrent_dropout (float): Recurrent dropout rate.
        param_grid (dict): Hyperparameter grid.
        n_jobs (int): Number of parallel jobs.
        verbose (int): Verbosity level.

    Returns:
        GridSearchCV: Fitted GridSearchCV object.
    """
    model = KerasRegressor(
        model=create_lstm_model,
        model__input_shape=input_shape,
        model__learning_rate=learning_rate,
        model__recurrent_dropout=recurrent_dropout,
        verbose=0
    )

    loo = LeaveOneOut()
    scorer = make_scorer(custom_scorer, greater_is_better=True)

    grid = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=loo,
        scoring=scorer,
        n_jobs=n_jobs,
        verbose=verbose
    )

    grid_result = grid.fit(X, y)
    return grid_result
