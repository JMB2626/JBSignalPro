from history import save_signal

def analyse(df):

    if len(df) < 5:
        return "⏸ ATTENTE", 50

    c1 = df.iloc[-5]
    c2 = df.iloc[-4]
    c3 = df.iloc[-3]
    c4 = df.iloc[-2]
    c5 = df.iloc[-1]

    # Swing High
    if c3["high"] > c2["high"] and c3["high"] > c4["high"]:

        if c5["close"] > c3["high"]:

            save_signal(
                0,0,0,0,
                "BUY",
                c5["close"]
            )

            return "🟢 ACHAT", 90

    # Swing Low
    if c3["low"] < c2["low"] and c3["low"] < c4["low"]:

        if c5["close"] < c3["low"]:

            save_signal(
                0,0,0,0,
                "SELL",
                c5["close"]
            )

            return "🔴 VENTE", 90

    return "⏸ ATTENTE", 50
