import numpy as np

def wape(y_true, y_pred):
    return np.sum(np.abs(y_true - y_pred)) / np.sum(np.abs(y_true)) * 100

def mase(y_true, y_pred, y_train, seasonality=1):
    n = len(y_train)
    if n <= seasonality:
        return np.nan
    naive_errors = np.mean(np.abs(y_train[seasonality:] - y_train[:-seasonality]))
    if naive_errors == 0:
        return np.nan
    return np.mean(np.abs(y_true - y_pred)) / naive_errors