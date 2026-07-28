
from twelvedata import TDClient
import os

def get_data(symbol, interval):
    td = TDClient(apikey=os.getenv("TWELVEDATA_API_KEY"))

    ts = td.time_series(
        symbol=symbol,
        interval=interval,
        outputsize=30
    )

    return ts.as_pandas()
