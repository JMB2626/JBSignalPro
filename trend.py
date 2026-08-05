def trend(df):

    first = df["close"].iloc[0]
    last = df["close"].iloc[-1]

    if last > first:
        return "BUY"

    if last < first:
        return "SELL"

    return "RANGE"
