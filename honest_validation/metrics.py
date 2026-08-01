import numpy as np

def wape(y_true, y_pred):
    """
    Weighted Absolute Percentage Error.
    
    Parameters
    ----------
    y_true : array-like
        Ground truth values.
    y_pred : array-like
        Predicted values.
    
    Returns
    -------
    float
        WAPE value as a percentage (0 to 100).
    """
    return np.sum(np.abs(y_true - y_pred)) / np.sum(np.abs(y_true)) * 100


def mase(y_true, y_pred, y_train, seasonality=1):
    """
    Mean Absolute Scaled Error.
    
    Parameters
    ----------
    y_true : array-like
        Ground truth values.
    y_pred : array-like
        Predicted values.
    y_train : array-like
        Training data for naive baseline scaling.
    seasonality : int, optional
        Seasonal period for naive forecast (default 1).
    
    Returns
    -------
    float
        MASE value (NaN if insufficient data).
    """
    n = len(y_train)
    if n <= seasonality:
        return np.nan
    naive_errors = np.mean(np.abs(y_train[seasonality:] - y_train[:-seasonality]))
    if naive_errors == 0:
        return np.nan
    return np.mean(np.abs(y_true - y_pred)) / naive_errors