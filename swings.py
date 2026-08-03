def last_swing_high(df):

    highs = df["high"].tolist()

    for i in range(len(highs) - 3, 2, -1):

        if (
            highs[i] > highs[i - 1]
            and highs[i] > highs[i - 2]
            and highs[i] > highs[i + 1]
            and highs[i] > highs[i + 2]
        ):
            return highs[i]

    return max(highs[-10:])


def last_swing_low(df):

    lows = df["low"].tolist()

    for i in range(len(lows) - 3, 2, -1):

        if (
            lows[i] < lows[i - 1]
            and lows[i] < lows[i - 2]
            and lows[i] < lows[i + 1]
            and lows[i] < lows[i + 2]
        ):
            return lows[i]

    return min(lows[-10:])
