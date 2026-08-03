def trend(df):

    highs = df["high"].tail(20).tolist()
    lows = df["low"].tail(20).tolist()

    hh = highs[-1] > highs[-2]
    hl = lows[-1] > lows[-2]

    lh = highs[-1] < highs[-2]
    ll = lows[-1] < lows[-2]

    if hh and hl:
        return "UP"

    if lh and ll:
        return "DOWN"

    return "RANGE"
