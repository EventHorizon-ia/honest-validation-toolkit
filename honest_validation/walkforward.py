import pandas as pd

def walkforward_split(df, train_until, val_start, embargo=0):
    """
    Chronological train/validation split.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with datetime index.
    train_until : str or datetime
        Last date of training set (inclusive).
    val_start : str or datetime
        First date of validation set.
    embargo : int, optional
        Gap in days between train and validation (default 0).
    
    Returns
    -------
    train : pd.DataFrame
        Training subset.
    val : pd.DataFrame
        Validation subset.
    """
    train = df[df.index <= train_until]
    val_start_dt = pd.Timestamp(val_start) + pd.Timedelta(days=embargo)
    val = df[df.index >= val_start_dt]
    return train, val