from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import os
from fastapi import Request
from fastapi.responses import JSONResponse


app = FastAPI()

print("🚀 FastAPI app started — CORS Middleware is active")


# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://credit-risk-ml.vercel.app", "https://credit-risk-65v06jjm4-sanduni-disanayakas-projects.vercel.app"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Load model and scaler ===
BASE_DIR = os.path.dirname(__file__)
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

@app.options("/predict")
async def options_predict(request: Request):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "*",
        "Access-Control-Allow-Headers": "*",
    }
    return JSONResponse(content={}, status_code=200, headers=headers)
