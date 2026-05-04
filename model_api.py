from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = pickle.load(open("p_salary.pkl", "rb"))

@app.get("/")
def home():
    return FileResponse("index.html")
@app.post("/predict")
def predict(data: dict):
    exp = float(data['YearsExperience'])
    result = model.predict([[exp]])

    return {
        "YearsExperience": exp,
        "PredictedSalary": float(result[0])
    }

"""
User clicks button
↓
JS fetch() sends request
↓
FastAPI /predict receives data
↓
Model predicts salary
↓
API returns JSON
↓
Frontend displays result
"""