from support_resistance import levels
from engulfing import engulfing
from history import save_signal

def analyse(df):

    if len(df) < 25:
        return "⏸ ATTENTE", 50

    support, resistance = levels(df)

    current = df.iloc[-1]

    pattern = engulfing(df)

    volume_ok = True

    if "volume" in df.columns:
        volume_ok = current["volume"] > df["volume"].tail(10).mean()

    # ACHAT
    if (
        current["close"] > resistance
        and pattern == "BUY"
        and volume_ok
    ):

        save_signal(
            0,
            0,
            0,
            0,
            "BUY",
            current["close"]
        )

        return "🟢 ACHAT", 85

    # VENTE
    if (
        current["close"] < support
        and pattern == "SELL"
        and volume_ok
    ):

        save_signal(
            0,
            0,
            0,
            0,
            "SELL",
            current["close"]
        )

        return "🔴 VENTE", 85

    return "⏸ ATTENTE", 50
