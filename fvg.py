def fair_value_gap(df, direction):

    if len(df) < 3:
        return False

    c1 = df.iloc[-3]
    c2 = df.iloc[-2]
    c3 = df.iloc[-1]

    if direction == "BUY":

        if c1["high"] < c3["low"]:
            return True

    if direction == "SELL":

        if c1["low"] > c3["high"]:
            return True

    return False
