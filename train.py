import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("history.csv")

X = df[["ema20", "ema50", "ema200", "rsi"]]
y = df["result"]

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Modèle entraîné.")
