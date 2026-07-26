from flask import Flask
from market import get_data
from strategy import analyse
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/")
def home():
    actifs = ["EUR/USD", "GBP/USD", "USD/JPY", "XAU/USD"]

    for actif in actifs:
        try:
            df = get_data(actif)
            signal = analyse(df)

            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={
                    "chat_id": CHAT_ID,
                    "text": f"📊 {actif}\nSignal : {signal}"
                }
            )
        except Exception as e:
            print(e)

    return "Analyse terminée."
