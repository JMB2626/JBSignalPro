def levels(df):

    resistance = df["high"].tail(20).max()
    support = df["low"].tail(20).min()

    return support, resistance
