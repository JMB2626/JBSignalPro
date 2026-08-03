def trend(df):

    highs = df["high"].tail(10).tolist()
    lows = df["low"].tail(10).tolist()

    hh = 0
    hl = 0
    lh = 0
    ll = 0

    for i in range(1, len(highs)):

        if highs[i] > highs[i - 1]:
            hh += 1
        else:
            lh += 1

        if lows[i] > lows[i - 1]:
            hl += 1
        else:
            ll += 1

    if hh >= 6 and hl >= 6:
        return "UP"

    if lh >= 6 and ll >= 6:
        return "DOWN"

    return "RANGE"
