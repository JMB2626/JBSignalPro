def confirmation(df):

    prev = df.iloc[-2]
    curr = df.iloc[-1]

    if curr["close"] > prev["high"]:
        return "BUY"

    if curr["close"] < prev["low"]:
        return "SELL"

    return "NONE"
