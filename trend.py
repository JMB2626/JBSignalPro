from ta.trend import EMAIndicator

def trend(df):

    ema20 = EMAIndicator(df["close"], window=20).ema_indicator()
    ema50 = EMAIndicator(df["close"], window=50).ema_indicator()

    prix = df["close"].iloc[-1]

    ema20_last = ema20.iloc[-1]
    ema50_last = ema50.iloc[-1]

    if prix > ema20_last > ema50_last:
        return "BUY"

    if prix < ema20_last < ema50_last:
        return "SELL"

    return "RANGE"
