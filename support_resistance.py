def levels(df):

    highs = df["high"].tail(50)
    lows = df["low"].tail(50)

    resistance = highs.max()
    support = lows.min()

    return support, resistance
