def order_block(df, direction):

    if len(df) < 6:
        return False

    candles = df.tail(6)

    if direction == "BUY":

        bearish = candles.iloc[-3]

        bullish = candles.iloc[-2]

        if (
            bearish["close"] < bearish["open"]
            and bullish["close"] > bullish["high"] * 0.999
        ):
            return True

    if direction == "SELL":

        bullish = candles.iloc[-3]

        bearish = candles.iloc[-2]

        if (
            bullish["close"] > bullish["open"]
            and bearish["close"] < bearish["low"] * 1.001
        ):
            return True

    return False
