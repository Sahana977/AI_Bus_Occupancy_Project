from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

app = FastAPI(
    title="AI Bus Occupancy Prediction API",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ==================================
# LOAD MODEL & ENCODERS
# ==================================

model = joblib.load("../models/best_model.pkl")

trip_encoder = joblib.load(
    "../models/trip_encoder.pkl"
)

stop_encoder = joblib.load(
    "../models/stop_encoder.pkl"
)

# ==================================
# REQUEST MODEL
# ==================================

class PredictionInput(BaseModel):
    trip_id: str = "500D-1"
    stop_id: str = "500D-1#5"
    arrival_time: str = "08:30"
    delay_min: int = 4
    is_peak_hour: int = 1

# ==================================
# HOME
# ==================================

@app.get("/")
def home():
    return {
        "message": "AI Bus Occupancy Prediction API Running Successfully"
    }

# ==================================
# TRAFFIC LEVEL
# ==================================

def get_traffic_level(delay):

    if delay <= 2:
        return 0

    elif delay <= 5:
        return 1

    return 2

# ==================================
# OCCUPANCY CATEGORY
# ==================================

def occupancy_category(value):

    if value < 30:
        return "Low"

    elif value < 70:
        return "Moderate"

    return "High"

# ==================================
# FEATURE CREATION
# ==================================

def create_features(data):

    try:
        trip_encoded = trip_encoder.transform(
            [data.trip_id]
        )[0]

    except:
        trip_encoded = 0

    try:
        stop_encoded = stop_encoder.transform(
            [data.stop_id]
        )[0]

    except:
        stop_encoded = 0

    try:
        h, m = map(
            int,
            data.arrival_time.split(":")
        )

    except:
        h = 8
        m = 0

    minutes = h * 60 + m

    time_sin = np.sin(
        2 * np.pi * minutes / 1440
    )

    time_cos = np.cos(
        2 * np.pi * minutes / 1440
    )

    traffic_level = get_traffic_level(
        data.delay_min
    )

    features = pd.DataFrame(
        [[
            trip_encoded,
            stop_encoded,
            data.delay_min,
            data.is_peak_hour,
            traffic_level,
            time_sin,
            time_cos
        ]],
        columns=[
            "trip_encoded",
            "stop_encoded",
            "delay_min",
            "is_peak_hour",
            "traffic_level",
            "time_sin",
            "time_cos"
        ]
    )

    return features

# ==================================
# PREDICT OCCUPANCY
# ==================================

@app.post("/predict")
def predict(data: PredictionInput):

    features = create_features(data)

    prediction = model.predict(
        features
    )[0]

    prediction = round(
        float(prediction),
        2
    )

    return {
        "predicted_occupancy": prediction,
        "occupancy_level": occupancy_category(
            prediction
        )
    }

# ==================================
# TRAFFIC PREDICTION
# ==================================

@app.post("/traffic")
def traffic(data: PredictionInput):

    level = get_traffic_level(
        data.delay_min
    )

    mapping = {
        0: "Low",
        1: "Moderate",
        2: "High"
    }

    return {
        "traffic_level": level,
        "traffic_status": mapping[level]
    }

# ==================================
# ANALYTICS
# ==================================

@app.get("/analytics")
def analytics():

    df = pd.read_csv(
        "../dataset/BusOccupancyDataset.csv"
    )

    avg_occupancy = round(
        df["seat_occupancy"].mean(),
        2
    )

    max_occupancy = int(
        df["seat_occupancy"].max()
    )

    min_occupancy = int(
        df["seat_occupancy"].min()
    )

    avg_delay = round(
        df["delay_min"].mean(),
        2
    )

    peak_percentage = round(
        (
            df["is_peak_hour"].sum()
            /
            len(df)
        ) * 100,
        2
    )

    return {
        "average_occupancy": avg_occupancy,
        "maximum_occupancy": max_occupancy,
        "minimum_occupancy": min_occupancy,
        "average_delay": avg_delay,
        "peak_hour_percentage": peak_percentage
    }

# ==================================
# HEALTH CHECK
# ==================================

@app.get("/health")
def health():

    return {
        "status": "running",
        "model": "CatBoost",
        "api": "healthy"
    }