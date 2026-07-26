import pandas as pd
from market import get_data
from trainer import train

def check_results():

    df = pd.read_csv("history.csv")

    for i in df.index:

        if df.loc[i, "result"] != -1:
            continue

        signal = df.loc[i, "signal"]
        entry = df.loc[i, "entry"]

        market = get_data("EUR/USD", "5min")
        last = market.iloc[-1]["close"]

        if signal == "BUY":
            df.loc[i, "result"] = 1 if last > entry else 0

        if signal == "SELL":
            df.loc[i, "result"] = 1 if last < entry else 0

    df.to_csv("history.csv", index=False)

    train()
