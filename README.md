# 🔍 Credit Risk Predictor (FastAPI + React)

This is a full-stack application that predicts **credit risk** based on input features like credit amount, duration, job code, and more. The backend is built using FastAPI and the frontend uses React. It uses a machine learning model trained with scikit-learn.

---

## 📦 Features

- 🎯 Predict credit risk using a trained ML model
- 🔙 Backend: FastAPI with model inference
- 🖥️ Frontend: React UI with real-time prediction display
- 🔗 Communication: POST request from frontend to backend
- ⚡ Local development setup (localhost)

---

## 🧪 Sample Prediction

**Input Fields:**
- Credit amount: `10000`
- Duration: `4`
- Job code: `1`
- Age: `22`
- Purpose Car: `1`
- Purpose Radio/TV: `0`

**Result:** ⚠️ High Risk (Displayed in UI)

---

## 📁 Project Structure

credit-risk-app/
├── backend/
│ ├── main.py
│ ├── credit_risk_model.pkl
│ ├── scaler.pkl
│ └── requirements.txt
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── App.js
│ │ └── ...
│ └── package.json


---

## ⚙️ Technologies Used

- **Backend**: Python, FastAPI, Uvicorn, Joblib, Scikit-learn
- **Frontend**: React, Axios
- **Local Hosting**: FastAPI on `localhost:8000`, React on `localhost:3000`

---

## 🚀 How to Run the Project Locally

### 1. Run Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

By default, it runs at:
➡️ http://localhost:8000

2. Run Frontend (React)
cd frontend
npm install
npm start

Opens at:
➡️ http://localhost:3000