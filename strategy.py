from history import save_signal

def analyse(df):

    last = df.iloc[-1]
    prev = df.iloc[-2]

    # Cassure haussière (Break of Structure)
    if last["close"] > prev["high"]:
        save_signal(
            0,
            0,
            0,
            0,
            "BUY",
            last["close"]
        )
        return "🟢 ACHAT", 90

    # Cassure baissière
    if last["close"] < prev["low"]:
        save_signal(
            0,
            0,
            0,
            0,
            "SELL",
            last["close"]
        )
        return "🔴 VENTE", 90

    return "⏸ ATTENTE", 50
