import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# Charger les données
df = pd.read_csv("history.csv")

# Supprimer les lignes incomplètes
df = df.dropna()

# Transformer BUY/SELL en nombres
df["signal"] = df["signal"].map({
    "BUY": 1,
    "SELL": 0
})

# Variables d'entrée
X = df[["EMA20", "EMA50", "EMA200", "RSI"]]

# Résultat attendu
y = df["signal"]

# Entraîner le modèle
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Sauvegarder le modèle
joblib.dump(model, "model.pkl")

print("✅ model.pkl créé avec succès")
