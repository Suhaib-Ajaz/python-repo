from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

gb_model = joblib.load("D:\AIs Geek\python-repo\Project\gradient_boosting_model.pkl")
scaler = joblib.load("D:\AIs Geek\python-repo\Project\scaler.pkl")

app = FastAPI(title="Placement Prediction API")

class Candidate(BaseModel):
    IQ: float
    CGPA: float
    Academic_Performance: float
    Internship_Experience: int
    Extra_Curricular_Score: float
    Communication_Skills: float
    Projects_Completed: int

@app.post("/")
def hello():
    return {"message": "Welcome to placement prediction API"}

@app.post("/predict")
def predict(candidate: Candidate):
    data = pd.DataFrame([candidate.dict()])
    data_scaled = scaler.transform(data)

    pred = gb_model.predict(data_scaled)[0]
    prob = gb_model.predict_proba(data_scaled)[0, pred]

    return {
        "prediction": int(pred),
        "probability": float(prob)
    }

#uvicorn deploy:app --reload