def engulfing(df):

    prev = df.iloc[-2]
    curr = df.iloc[-1]

    if (
        prev["close"] < prev["open"]
        and curr["close"] > curr["open"]
        and curr["open"] <= prev["close"]
        and curr["close"] >= prev["open"]
    ):
        return "BUY"

    if (
        prev["close"] > prev["open"]
        and curr["close"] < curr["open"]
        and curr["open"] >= prev["close"]
        and curr["close"] <= prev["open"]
    ):
        return "SELL"

    return "NONE"
