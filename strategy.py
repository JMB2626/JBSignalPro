from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator

def analyse(df):
    df["EMA20"] = EMAIndicator(df["close"], window=20).ema_indicator()
    df["EMA50"] = EMAIndicator(df["close"], window=50).ema_indicator()
    df["RSI"] = RSIIndicator(df["close"], window=14).rsi()

    last = df.iloc[-1]

    score = 0

    if last["EMA20"] > last["EMA50"]:
        score += 50

    if 45 <= last["RSI"] <= 65:
        score += 50

    confiance = score

    if score == 100:
        signal = "🟢 ACHAT"
    elif score == 50:
        signal = "⏸ ATTENTE"
    else:
        signal = "🔴 VENTE"

    return signal, confiance
