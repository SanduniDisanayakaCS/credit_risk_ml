import React, { useState } from "react";
import axios from "axios";
import "./App.css"; // if you use styles

function App() {
  const [features, setFeatures] = useState(Array(6).fill(0));
  const [prediction, setPrediction] = useState(null);

  const labels = [
    "💰 Credit amount",
    "📅 Duration (months)",
    "💼 Job (numeric code)",
    "🧍 Age",
    "🚗 Purpose: Car (1 = Yes)",
    "📺 Purpose: Radio/TV (1 = Yes)"
  ];

  const handleChange = (index, value) => {
    const updated = [...features];
    updated[index] = Number(value);
    setFeatures(updated);
  };

  const handleSubmit = async () => {
    try {
      const res = await axios.post("https://creditriskml-production.up.railway.app/predict",
        { features },
        { headers: { "Content-Type": "application/json" } }
      );
      setPrediction(res.data.credit_risk_prediction);
    } catch (err) {
      console.error("Backend error:", err.response ? err.response.data : err.message);
      alert("Prediction failed. Check backend connection.");
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>🔍 Credit Risk Predictor (Top 6 Features)</h2>
      <div style={styles.form}>
        {labels.map((label, i) => (
          <div key={i} style={styles.inputGroup}>
            <label>{label}</label>
            <input
              type="number"
              value={features[i]}
              onChange={(e) => handleChange(i, e.target.value)}
              style={styles.input}
            />
          </div>
        ))}
        <button onClick={handleSubmit} style={styles.button}>Predict</button>
        {prediction !== null && (
          <div style={prediction === 1 ? styles.warning : styles.success}>
            {prediction === 1 ? "⚠️ High Risk" : "✅ Low Risk"}
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  container: {
    fontFamily: "Segoe UI, sans-serif",
    padding: "2rem",
    background: "#f9f9f9",
    minHeight: "100vh"
  },
  title: {
    textAlign: "center",
    marginBottom: "2rem",
    color: "#0b3d91"
  },
  form: {
    maxWidth: "400px",
    margin: "0 auto"
  },
  inputGroup: {
    marginBottom: "1rem"
  },
  input: {
    width: "100%",
    padding: "0.5rem"
  },
  button: {
    width: "100%",
    padding: "0.75rem",
    background: "#0b3d91",
    color: "#fff",
    border: "none",
    cursor: "pointer"
  },
  success: {
    marginTop: "1rem",
    padding: "1rem",
    backgroundColor: "#d4edda",
    color: "#155724",
    textAlign: "center"
  },
  warning: {
    marginTop: "1rem",
    padding: "1rem",
    backgroundColor: "#fff3cd",
    color: "#856404",
    textAlign: "center"
  }
};

export default App;
