from flask import Flask
from market import get_h4, get_m1
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

    actifs = ["R_75"]

    for actif in actifs:
        try:
            print(f"=== Analyse {actif} ===")

            df_h4 = get_h4()
            df_m1 = get_m1()

            print(f"H4 : {len(df_h4)} bougies")
            print(f"M1 : {len(df_m1)} bougies")

            signal, confiance = analyse(df_h4, df_m1)

            print(
                f"Signal : {signal} | "
                f"Confiance : {confiance}%"
            )

            if signal == "⏸ ATTENTE":
                continue

            if dernier_signal.get(actif) != signal:

                requests.post(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                    data={
                        "chat_id": CHAT_ID,
                        "text": (
                            f"📊 {actif}\n"
                            f"Signal : {signal}\n"
                            f"Confiance : {confiance}%"
                        )
                    }
                )

                dernier_signal[actif] = signal

        except Exception as e:
            print(f"Erreur sur {actif} : {e}")


schedule.every(1).minutes.do(envoyer_signaux)


def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


@app.route("/")
def home():
    return "JBSignalPro est actif."


if __name__ == "__main__":

    threading.Thread(
        target=scheduler,
        daemon=True
    ).start()

    envoyer_signaux()

    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port
    )
