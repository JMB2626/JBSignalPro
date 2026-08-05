from twelvedata import TDClient
import os

td = TDClient(apikey=os.getenv("TWELVEDATA_API_KEY"))

def get_data(interval):

    ts = td.time_series(
        symbol="XAU/USD",
        interval=interval,
        outputsize=100
    )

    return ts.as_pandas()


def get_h4():
    return get_data("4h")


def get_m1():
    return get_data("1min")
