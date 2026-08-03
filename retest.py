def retest(df, swing_high, swing_low, direction):

    current = df.iloc[-1]

    if direction == "BUY":

        if (
            current["low"] <= swing_high
            and current["close"] > swing_high
        ):
            return True

    if direction == "SELL":

        if (
            current["high"] >= swing_low
            and current["close"] < swing_low
        ):
            return True

    return False
