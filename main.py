from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
import os

app = FastAPI(title="Student Grade Prediction API (Final Version)")

# Path file
MODEL_PATH = "model.pkl"
SCALER_PATH = "scaler.pkl"
DATA_PATH = "Final Data.csv"

# Load model dan scaler
def load_model_scaler():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)
    return model, scaler

# Schema input mentah
class Student(BaseModel):
    school: str
    sex: str
    address: str
    famsup: str
    schoolsup: str
    paid: str
    activities: str
    nursery: str
    higher: str
    internet: str
    romantic: str
    Pstatus: str
    reason: str
    Fjob: str
    Mjob: str
    studytime: int
    failures: int
    absences: int
    G1: float
    G2: float
    Dalc: int
    Walc: int
    health: int
    Medu: int
    Fedu: int

# Preprocessing otomatis One-Hot
def preprocess_input(data, scaler):
    # Load kolom fitur
    df_final = pd.read_csv(DATA_PATH)
    target_col = "G3"
    feature_order = [col for col in df_final.columns if col != target_col]

    # Siapkan semua fitur = 0
    base_features = {feat: 0 for feat in feature_order}

    # Mapping one-hot kategori
    one_hot_fields = {
        f"school_{data.school}": 1,
        f"sex_{data.sex}": 1,
        f"address_{data.address}": 1,
        f"famsup_{data.famsup}": 1,
        f"schoolsup_{data.schoolsup}": 1,
        f"paid_{data.paid}": 1,
        f"activities_{data.activities}": 1,
        f"nursery_{data.nursery}": 1,
        f"higher_{data.higher}": 1,
        f"internet_{data.internet}": 1,
        f"romantic_{data.romantic}": 1,
        f"Pstatus_{data.Pstatus}": 1,
        f"reason_{data.reason}": 1,
        f"Fjob_{data.Fjob}": 1,
        f"Mjob_{data.Mjob}": 1
    }

    for key, value in one_hot_fields.items():
        if key in base_features:
            base_features[key] = value

    # Mapping fitur numerik
    numerics = {
        'studytime': data.studytime,
        'failures': data.failures,
        'absences': data.absences,
        'G1': data.G1,
        'G2': data.G2,
        'Dalc': data.Dalc,
        'Walc': data.Walc,
        'health': data.health,
        'Medu': data.Medu,
        'Fedu': data.Fedu
    }

    for key, value in numerics.items():
        if key in base_features:
            base_features[key] = value

    # Buat DataFrame
    df = pd.DataFrame([base_features])

    # Scaling
    df_scaled = scaler.transform(df)

    return df_scaled

# Endpoint utama
@app.get("/")
def read_root():
    return {"message": "Student Grade Prediction API is running"}

@app.post("/predict")
def predict_grade(data: Student):
    try:
        model, scaler = load_model_scaler()
        processed = preprocess_input(data, scaler)
        prediction = model.predict(processed)[0]

        return {
            "G1": data.G1,
            "G2": data.G2,
            "Predicted_G3": round(float(prediction), 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")