from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    token = os.getenv("BOT_TOKEN")

    if token:
        return "JBSignalPro est connecté à Telegram."
    else:
        return "BOT_TOKEN introuvable."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
