import joblib
import numpy as np

model = joblib.load("models/model.pkl")

def predict_workforce(features):
    arr = np.array(features).reshape(1, -1)
    result = model.predict(arr)
    return float(result[0])