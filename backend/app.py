from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = pickle.load(open("p_salary.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "Salary prediction API is working"}

@app.post("/predict")
def predict(data: dict):
    exp = float(data["YearsExperience"])

    result = model.predict(
        pd.DataFrame([[exp]], columns=["YearsExperience"])
    )

    return {
        "YearsExperience": exp,
        "PredictedSalary": float(result[0])
    }