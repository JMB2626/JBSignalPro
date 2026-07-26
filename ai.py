import os
import joblib
import numpy as np

MODEL = "model.pkl"

def predict(features):
    if not os.path.exists(MODEL):
        return None

    model = joblib.load(MODEL)
    x = np.array(features).reshape(1, -1)
    return model.predict(x)[0]
