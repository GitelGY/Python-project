from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

app = FastAPI()

# הגדרת CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
model_columns = joblib.load('columns.pkl')

class PredictionData(BaseModel):
    Year: int
    Spending_USD: float
    Country: str

@app.post("/predict")
def predict(data: PredictionData):
    input_dict = data.dict()
    
    df_input = pd.DataFrame(columns=model_columns)
    df_input.loc[0] = 0
    
    df_input['Year'] = input_dict['Year']
    df_input['Spending_USD'] = input_dict['Spending_USD']
    
    
    country_column = f"Country_{input_dict['Country']}"
    if country_column in df_input.columns:
        df_input[country_column] = 1
    
    input_scaled = scaler.transform(df_input)
    
    prediction = model.predict(input_scaled)
    
    return {"prediction": round(float(prediction[0]), 2)}

@app.get("/")
def home():
    return {"message": "Health Expectancy API is running!"}


try:
    lr_model = joblib.load('lr_model.pkl') 
except:
    print("Warning: lr_model.pkl not found. Feature importance will not work.")

@app.get("/info")
def get_info():
    if hasattr(lr_model, 'coef_'):
        coeffs = dict(zip(model_columns, lr_model.coef_.tolist()))
        sorted_coeffs = dict(sorted(coeffs.items(), key=lambda item: abs(item[1]), reverse=True))
        return {
            "model_type": "Linear Regression",
            "feature_importance": sorted_coeffs
        }
    else:
        return {"error": "Model does not support coefficients"}

        