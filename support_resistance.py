def levels(df):

    highs = df["high"].tail(100)
    lows = df["low"].tail(100)

    resistance = highs.mode().iloc[0] if not highs.mode().empty else highs.max()
    support = lows.mode().iloc[0] if not lows.mode().empty else lows.min()

    return support, resistance
