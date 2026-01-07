from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR.parent / "model" / "house_price_model.pkl"

app = FastAPI()
model = None


class HouseInput(BaseModel):
    area: float = Field(..., gt=0)
    bedrooms: int = Field(..., ge=1, le=10)
    distance: float = Field(..., ge=0)


@app.on_event("startup")
def load_model():
    global model
    try:
        if not MODEL_PATH.exists():
            raise FileNotFoundError
        model = joblib.load(MODEL_PATH)
        logger.info("Model loaded successfully")
    except Exception as e:
        logger.exception("Failed to load model")
        raise RuntimeError("Model loading failed")


@app.post("/predict")
def predict_price(data: HouseInput):
    try:
        df = pd.DataFrame([data.dict()])
        prediction = model.predict(df)
        return {"predicted_price": float(prediction[0])}

    except Exception as e:
        logger.exception("Prediction failed")
        raise HTTPException(
            status_code=500,
            detail="Prediction failed"
        )
