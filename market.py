import os
import requests
import pandas as pd

API_KEY = os.getenv("FINNHUB_API_KEY")

def get_data():

    url = (
        f"https://finnhub.io/api/v1/forex/candle"
        f"?symbol=OANDA:XAU_USD"
        f"&resolution=5"
        f"&count=30"
        f"&token={API_KEY}"
    )

    data = requests.get(url).json()

    if data.get("s") != "ok":
        raise Exception(data)

    df = pd.DataFrame({
        "open": data["o"],
        "high": data["h"],
        "low": data["l"],
        "close": data["c"],
        "volume": data["v"]
    })

    return df
