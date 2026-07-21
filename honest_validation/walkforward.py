def walkforward_split(df, train_until, val_start, embargo=0):
    train = df[df.index <= train_until]
    val = df[df.index >= val_start + embargo]
    return train, val