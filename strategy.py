from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator

def analyse(df):
    df["EMA20"] = EMAIndicator(df["close"], window=20).ema_indicator()
    df["EMA50"] = EMAIndicator(df["close"], window=50).ema_indicator()
    df["RSI"] = RSIIndicator(df["close"], window=14).rsi()

    last = df.iloc[-1]

    ema20 = last["EMA20"]
    ema50 = last["EMA50"]
    rsi = last["RSI"]

    if ema20 > ema50 and rsi >= 55:
        return "🟢 ACHAT", 85

    if ema20 < ema50 and rsi <= 45:
        return "🔴 VENTE", 85

    return "⏸ ATTENTE", 40
