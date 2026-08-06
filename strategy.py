
from trend import trend
from support_resistance import levels
from rejection import rejection
from confirmation import confirmation
from history import save_signal

def analyse(df_h4, df_m1):

    direction = trend(df_h4)

    support, resistance = levels(df_h4)

    current = df_m1.iloc[-1]

    reject = rejection(df_m1)

    confirm = confirmation(df_m1)

    volume_ok = True

    if "volume" in df_m1.columns:
        volume_ok = current["volume"] > df_m1["volume"].tail(10).mean()

    tolerance = 3.0

    # ACHAT
    if direction == "BUY":

        proche_support = abs(current["low"] - support) <= tolerance

        if proche_support and reject == "BUY" and confirm == "BUY" and volume_ok:

            save_signal(0,0,0,0,"BUY",current["close"])

            return "🟢 ACHAT",95

    # VENTE
    if direction == "SELL":

        proche_resistance = abs(current["high"] - resistance) <= tolerance

        if proche_resistance and reject == "SELL" and confirm == "SELL" and volume_ok:

            save_signal(0,0,0,0,"SELL",current["close"])

            return "🔴 VENTE",95

    return "⏸ ATTENTE",50
