from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
from schemas import CropPriceFeatures
import pandas as pd

app = FastAPI()

# Allow all origins for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("xgb_model.pkl", "rb") as f:
    loaded_xgb_model = pickle.load(f)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict/")
def predict(input_data: CropPriceFeatures):
    input_df = pd.DataFrame([input_data.model_dump(by_alias=True)])
    prediction = loaded_xgb_model.predict(input_df)
    return {"predicted_price": prediction.tolist()}
