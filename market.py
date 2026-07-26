from twelvedata import TDClient
import os

def get_data(symbol):
    api_key = os.getenv("TWELVEDATA_API_KEY")

    if not api_key:
        raise Exception("TWELVEDATA_API_KEY introuvable")

    td = TDClient(apikey=api_key)

    ts = td.time_series(
        symbol=symbol,
        interval="5min",
        outputsize=100,
    )

    return ts.as_pandas()
