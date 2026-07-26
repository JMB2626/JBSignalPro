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
            timeframes = ["1min", "5min", "15min"]
            resultats = []

            for tf in timeframes:
                df = get_data(actif, tf)
                signal, confiance = analyse(df)
                resultats.append((signal, confiance))

            if all(r[0] == "🟢 ACHAT" for r in resultats):
                signal = "🟢 ACHAT"
            elif all(r[0] == "🔴 VENTE" for r in resultats):
                signal = "🔴 VENTE"
            else:
                signal = "⏸ ATTENTE"

            confiance = sum(r[1] for r in resultats) // len(resultats)

            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={
                    "chat_id": CHAT_ID,
                    "text": f"📊 {actif}\nSignal : {signal}\nConfiance : {confiance}%"
                }
            )

        except Exception as e:
            print(e)

    return "Analyse terminée."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
