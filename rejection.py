def rejection(df):

    candle = df.iloc[-1]

    body = abs(candle["close"] - candle["open"])

    upper_wick = candle["high"] - max(candle["open"], candle["close"])

    lower_wick = min(candle["open"], candle["close"]) - candle["low"]

    if lower_wick > body * 2:
        return "BUY"

    if upper_wick > body * 2:
        return "SELL"

    return "NONE"
