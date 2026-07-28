from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator
from history import save_signal

def analyse(df):

    df["EMA20"] = EMAIndicator(df["close"], window=20).ema_indicator()
    df["EMA50"] = EMAIndicator(df["close"], window=50).ema_indicator()
    df["EMA200"] = EMAIndicator(df["close"], window=200).ema_indicator()
    df["RSI"] = RSIIndicator(df["close"], window=14).rsi()

    last = df.iloc[-1]

    if last["EMA20"] > last["EMA50"] and last["RSI"] > 55:
        save_signal(
            last["EMA20"],
            last["EMA50"],
            last["EMA200"],
            last["RSI"],
            "BUY",
            last["close"]
        )
        return "🟢 ACHAT", 80

    if last["EMA20"] < last["EMA50"] and last["RSI"] < 45:
        save_signal(
            last["EMA20"],
            last["EMA50"],
            last["EMA200"],
            last["RSI"],
            "SELL",
            last["close"]
        )
        return "🔴 VENTE", 80

    return "⏸ ATTENTE", 50
