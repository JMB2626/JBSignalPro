from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator

def analyse(df):
    df["EMA20"] = EMAIndicator(df["close"], window=20).ema_indicator()
    df["EMA50"] = EMAIndicator(df["close"], window=50).ema_indicator()
    df["RSI"] = RSIIndicator(df["close"], window=14).rsi()

    last = df.iloc[-1]

    if last["EMA20"] > last["EMA50"] and last["RSI"] < 70:
        return "🟢 ACHAT"

    if last["EMA20"] < last["EMA50"] and last["RSI"] > 30:
        return "🔴 VENTE"

    return "⏸ ATTENTE"
