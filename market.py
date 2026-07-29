from twelvedata import TDClient
import os

def get_data():
    td = TDClient(apikey=os.getenv("TWELVEDATA_API_KEY"))

    ts = td.time_series(
        symbol="XAU/USD",
        interval="5min",
        outputsize=30
    )

    return ts.as_pandas()
