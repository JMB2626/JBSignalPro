from flask import Flask
from market import get_data
from strategy import analyse
from result_checker import check_results
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
    print("=== Début analyse ===")
    check_results()

    actifs = ["EUR/USD", "XAU/USD"]

    for actif in actifs:
        try:
            resultats = []

            df = get_data(actif, "5min")
            signal, confiance = analyse(df)

            if signal == "⏸ ATTENTE":
               continue

            if dernier_signal.get(actif) != signal:
                print(actif, signal, confiance)

                requests.post(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                    data={
                        "chat_id": CHAT_ID,
                        "text": f"📊 {actif}\nSignal : {signal}\nConfiance : {confiance}%"
                    }
                )

                dernier_signal[actif] = signal

        except Exception as e:
            print(f"Erreur sur {actif} : {e}")

schedule.every(5).minutes.do(envoyer_signaux)

def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

@app.route("/")
def home():
    return "JBSignalPro est actif."

if __name__ == "__main__":
    threading.Thread(target=scheduler, daemon=True).start()

    # Analyse immédiate au démarrage
    envoyer_signaux()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
