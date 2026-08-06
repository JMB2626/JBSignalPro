from trend import trend
from support_resistance import levels
from engulfing import engulfing
from history import save_signal

def analyse(df_h4, df_m1):

    if len(df_h4) < 50 or len(df_m1) < 25:
        return "⏸ ATTENTE", 50

    direction = trend(df_h4)

    support, resistance = levels(df_h4)

    current = df_m1.iloc[-1]

    pattern = engulfing(df_m1)

    volume_ok = True

    if "volume" in df_m1.columns:
        volume_ok = current["volume"] > df_m1["volume"].tail(10).mean()

    # ACHAT
    if (
        direction == "BUY"
        and current["close"] > resistance
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

        return "🟢 ACHAT", 90

    # VENTE
    if (
        direction == "SELL"
        and current["close"] < support
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

        return "🔴 VENTE", 90

    return "⏸ ATTENTE", 50
