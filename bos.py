def bos(df, resistance, support):

    current = df.iloc[-1]

    if current["close"] > resistance:
        return "BUY"

    if current["close"] < support:
        return "SELL"

    return "NONE"
