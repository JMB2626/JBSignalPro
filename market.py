from twelvedata import TDClient
import os

td = TDClient(apikey=os.getenv("TWELVEDATA_API_KEY"))

def get_data(symbol):
    ts = td.time_series(
        symbol=symbol,
        interval="5min",
        outputsize=100,
        timezone="UTC"
    )

    return ts.as_pandas()
