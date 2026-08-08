import websocket
import json
import pandas as pd

DERIV_APP_ID = os.getenv("DERIV_APP_ID")

DERIV_WS = f"wss://ws.binaryws.com/websockets/v3?app_id={DERIV_APP_ID}"
SYMBOL = "R_75"


def get_data(granularity):

    ws = websocket.create_connection(DERIV_WS)

    request = {
        "ticks_history": SYMBOL,
        "count": 100,
        "end": "latest",
        "style": "candles",
        "granularity": granularity
    }

    ws.send(json.dumps(request))

    response = json.loads(ws.recv())

    ws.close()

    if "error" in response:
        raise Exception(response["error"])

    candles = response.get("candles", [])

    if not candles:
        raise Exception("Aucune donnée reçue de Deriv")

    df = pd.DataFrame(candles)

    for col in ["open", "high", "low", "close"]:
        df[col] = pd.to_numeric(df[col])

    df["volume"] = 0

    return df


def get_h4():
    return get_data(14400)


def get_m1():
    return get_data(60)
