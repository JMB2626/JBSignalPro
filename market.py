import os
import requests
import pandas as pd

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")


def get_data():

    url = (
        "https://www.alphavantage.co/query"
        "?function=TIME_SERIES_INTRADAY"
        "&symbol=XAUUSD"
        "&interval=5min"
        "&outputsize=compact"
        f"&apikey={API_KEY}"
    )

    data = requests.get(url).json()

    series = data.get("Time Series FX (5min)")

    if not series:
        raise Exception(data)

    df = pd.DataFrame.from_dict(
        series,
        orient="index"
    )

    df = df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close"
    })

    df = df.astype(float)

    df = df.sort_index()

    return df
