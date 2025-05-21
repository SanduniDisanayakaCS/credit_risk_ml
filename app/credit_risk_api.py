from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI()

# === Load model and scaler ===
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Go up one level
model = joblib.load(os.path.join(BASE_DIR, "models", "credit_risk_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models", "scaler.pkl"))

# === Define input schema ===
class InputData(BaseModel):
    features: list  # Expecting 6 numeric values

@app.post("/predict")
def predict(data: InputData):
    x = np.array(data.features).reshape(1, -1)
    x_scaled = scaler.transform(x)
    pred = model.predict(x_scaled)
    return {"credit_risk_prediction": int(pred[0])}
