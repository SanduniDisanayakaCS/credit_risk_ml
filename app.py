import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("models/credit_risk_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("💳 Credit Risk Prediction App")
st.markdown("Enter customer features to predict loan risk.")

# Example inputs (match your feature count, here: 21)
user_input = []
user_input.append(st.slider("Age", 18, 75, 30))
user_input.append(st.number_input("Credit amount", 0, 10000, 3000))
user_input.append(st.number_input("Duration (months)", 6, 72, 24))

# Dummy binary features (adjust based on your one-hot columns)
for i in range(18):  # fill rest with True/False toggles
    user_input.append(st.checkbox(f"Feature {i+4}"))

if st.button("Predict"):
    x = np.array(user_input).reshape(1, -1)
    x_scaled = scaler.transform(x)
    pred = model.predict(x_scaled)
    st.success(f"Prediction: {'High Risk' if pred[0]==1 else 'Low Risk'}")
