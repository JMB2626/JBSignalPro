def levels(df):

    resistance = df["high"].tail(50).max()
    support = df["low"].tail(50).min()

    return support, resistance
