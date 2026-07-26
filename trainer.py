import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

def train():

    if not os.path.exists("history.csv"):
        return

    df = pd.read_csv("history.csv")

    df = df[df["result"] != -1]

    if len(df) < 100:
        return

    X = df[["ema20", "ema50", "ema200", "rsi"]]
    y = df["result"]

    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42
    )

    model.fit(X, y)

    joblib.dump(model, "model.pkl")
