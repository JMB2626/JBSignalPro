from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator
from ai import predict
from history import save_signal

def analyse(df):

    df["EMA20"] = EMAIndicator(df["close"], window=20).ema_indicator()
    df["EMA50"] = EMAIndicator(df["close"], window=50).ema_indicator()
    df["EMA200"] = EMAIndicator(df["close"], window=200).ema_indicator()
    df["RSI"] = RSIIndicator(df["close"], window=14).rsi()

    last = df.iloc[-1]

    features = [
        last["EMA20"],
        last["EMA50"],
        last["EMA200"],
        last["RSI"]
    ]

    prediction = predict(features)
    save_signal(
    last["EMA20"],
    last["EMA50"],
    last["EMA200"],
    last["RSI"]
    )

    if prediction == 1:
        return "🟢 ACHAT", 90
        save_signal(
    last["EMA20"],
    last["EMA50"],
    last["EMA200"],
    last["RSI"]
        )

    if prediction == 0:
        return "🔴 VENTE", 90

    return "⏸ ATTENTE", 50
