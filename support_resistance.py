def levels(df):

    highs = []
    lows = []

    # Recherche des Swing High et Swing Low
    for i in range(2, len(df) - 2):

        # Swing High
        if (
            df["high"].iloc[i] > df["high"].iloc[i-1]
            and df["high"].iloc[i] > df["high"].iloc[i-2]
            and df["high"].iloc[i] > df["high"].iloc[i+1]
            and df["high"].iloc[i] > df["high"].iloc[i+2]
        ):
            highs.append(df["high"].iloc[i])

        # Swing Low
        if (
            df["low"].iloc[i] < df["low"].iloc[i-1]
            and df["low"].iloc[i] < df["low"].iloc[i-2]
            and df["low"].iloc[i] < df["low"].iloc[i+1]
            and df["low"].iloc[i] < df["low"].iloc[i+2]
        ):
            lows.append(df["low"].iloc[i])

    resistance = highs[-1] if highs else df["high"].max()
    support = lows[-1] if lows else df["low"].min()

    return support, resistance
