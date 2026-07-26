
from flask import Flask
from market import get_data
from strategy import analyse
import requests
import os
import schedule
import threading
import time

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

dernier_signal = {}

def envoyer_signaux():
    actifs = ["EUR/USD", "GBP/USD", "USD/JPY", "XAU/USD"]

    for actif in actifs:
        try:
            resultats = []

            for tf in ["1min", "5min", "15min"]:
                df = get_data(actif, tf)
                signal, confiance = analyse(df)
                resultats.append((signal, confiance))

            if all(r[0] == "🟢 ACHAT" for r in resultats):
                signal = "🟢 ACHAT"
            elif all(r[0] == "🔴 VENTE" for r in resultats):
                signal = "🔴 VENTE"
            else:
                continue

            confiance = sum(r[1] for r in resultats) // len(resultats)

            if dernier_signal.get(actif) != signal:
                requests.post(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                    data={
                        "chat_id": CHAT_ID,
                        "text": f"📊 {actif}\nSignal : {signal}\nConfiance : {confiance}%"
                    }
                )

                dernier_signal[actif] = signal

        except Exception as e:
            print(e)

schedule.every(1).minutes.do(envoyer_signaux)

def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=scheduler, daemon=True).start()

@app.route("/")
def home():
    return "JBSignalPro est actif."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
