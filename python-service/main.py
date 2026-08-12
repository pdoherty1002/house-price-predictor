from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd

class HouseFeatures(BaseModel):
    MSSubClass: int
    MSZoning: str
    LotArea: int
    LotShape: str
    Neighborhood: str
    OverallQual: int
    OverallCond: int
    YearBuilt: int
    BedroomAbvGr: int
    KitchenQual: str

app = FastAPI()

model = joblib.load("house_price_model.pkl")
model_columns = joblib.load("model_columns.pkl")

@app.get("/")
def read_root():
    return {"message": "House price API is running"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    input_dict = features.model_dump()
    input_df = pd.DataFrame([input_dict])
    input_encoded = pd.get_dummies(input_df, columns=["MSZoning", "LotShape", "Neighborhood", "KitchenQual"])
    input_final = input_encoded.reindex(columns=model_columns, fill_value=False)
    
    prediction = model.predict(input_final)
    
    return {"predicted_price": prediction[0]}