def bos(df, swing_high, swing_low):

    current = df.iloc[-1]

    if current["close"] > swing_high:
        return "BUY"

    if current["close"] < swing_low:
        return "SELL"

    return "NONE"
