def choch(df):

    if len(df) < 4:
        return "NONE"

    c1 = df.iloc[-4]
    c2 = df.iloc[-3]
    c3 = df.iloc[-2]
    c4 = df.iloc[-1]

    # CHOCH haussier
    if (
        c2["close"] < c2["open"]
        and c3["close"] > c3["open"]
        and c4["close"] > c3["high"]
    ):
        return "BUY"

    # CHOCH baissier
    if (
        c2["close"] > c2["open"]
        and c3["close"] < c3["open"]
        and c4["close"] < c3["low"]
    ):
        return "SELL"

    return "NONE"
