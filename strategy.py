from trend import trend
from support_resistance import levels
from engulfing import engulfing
from history import save_signal
from rejection import rejection

def analyse(df_h4, df_m1):

    direction = trend(df_h4)

    support, resistance = levels(df_h4)

    current = df_m1.iloc[-1]

    volume_ok = True

    if "volume" in df_m1.columns:
        volume_ok = current["volume"] > df_m1["volume"].tail(10).mean()

    pattern = engulfing(df_m1)
    reject = rejection(df_m1)

    tolerance = 3.0

    # ACHAT
    if direction == "BUY":

        proche_support = abs(current["low"] - support) <= tolerance

        if proche_support and pattern == "BUY" and reject == "BUY" and volume_ok:

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
    if direction == "SELL":

        proche_resistance = abs(resistance - current["high"]) <= tolerance

        if proche_resistance and pattern == "SELL" and reject == "SELL" and volume_ok:

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
