"""
model_builder.py

Build and compile LSTM model with specified hyperparameters.
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam

def create_lstm_model(
    units1: int,
    units2: int,
    dense_units: int,
    dropout: float,
    recurrent_dropout: float,
    input_shape: tuple,
    learning_rate: float
):
    """
    Create a 5-layer LSTM model.

    Args:
        units1 (int): Number of units in first LSTM layer.
        units2 (int): Number of units in second LSTM layer.
        dense_units (int): Number of units in Dense layer.
        dropout (float): Dropout rate.
        recurrent_dropout (float): Recurrent dropout rate.
        input_shape (tuple): Input shape of the data.
        learning_rate (float): Learning rate for Adam optimizer.

    Returns:
        tf.keras.Model: Compiled Keras model.
    """
    model = Sequential([
        LSTM(units=units1, return_sequences=True, input_shape=input_shape,
             activation='tanh', recurrent_activation='sigmoid',
             dropout=dropout, recurrent_dropout=recurrent_dropout),
        LSTM(units=units2, return_sequences=False,
             activation='tanh', recurrent_activation='sigmoid',
             dropout=dropout, recurrent_dropout=recurrent_dropout),
        Dropout(dropout),
        Dense(units=dense_units, activation='relu'),
        Dense(units=1, activation='linear')
    ])
    optimizer = Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss='mse')
    return model
