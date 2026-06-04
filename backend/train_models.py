import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    explained_variance_score,
    median_absolute_error
)

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

from xgboost import XGBRegressor
from catboost import CatBoostRegressor

# ============================
# LOAD DATASET
# ============================

df = pd.read_csv("BusOccupancyDataset.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# ============================
# HANDLE MISSING VALUES
# ============================

df.dropna(inplace=True)

# ============================
# FEATURE ENGINEERING
# ============================

df["arrival_time"] = pd.to_datetime(
    df["arrival_time"],
    format="%H:%M:%S",
    errors="coerce"
)

df.dropna(inplace=True)

df["minutes"] = (
    df["arrival_time"].dt.hour * 60
    + df["arrival_time"].dt.minute
)

df["time_sin"] = np.sin(
    2 * np.pi * df["minutes"] / 1440
)

df["time_cos"] = np.cos(
    2 * np.pi * df["minutes"] / 1440
)

# ============================
# CREATE TRAFFIC LEVEL
# ============================

def traffic_level(delay):
    if delay <= 2:
        return 0
    elif delay <= 5:
        return 1
    else:
        return 2

df["traffic_level"] = df["delay_min"].apply(traffic_level)

# ============================
# ENCODE CATEGORICAL FEATURES
# ============================

trip_encoder = LabelEncoder()
stop_encoder = LabelEncoder()

df["trip_encoded"] = trip_encoder.fit_transform(df["trip_id"])
df["stop_encoded"] = stop_encoder.fit_transform(df["stop_id"])

joblib.dump(trip_encoder, "trip_encoder.pkl")
joblib.dump(stop_encoder, "stop_encoder.pkl")

# ============================
# FEATURES
# ============================

X = df[
    [
        "trip_encoded",
        "stop_encoded",
        "delay_min",
        "is_peak_hour",
        "traffic_level",
        "time_sin",
        "time_cos"
    ]
]

y = df["seat_occupancy"]

# ============================
# SPLIT DATA
# ============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)

# ============================
# RANDOM FOREST
# ============================

rf = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

# ============================
# XGBOOST
# ============================

xgb = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6,
    random_state=42
)

xgb.fit(X_train, y_train)
xgb_pred = xgb.predict(X_test)

# ============================
# CATBOOST
# ============================

cat = CatBoostRegressor(
    iterations=300,
    learning_rate=0.05,
    depth=6,
    verbose=False
)

cat.fit(X_train, y_train)
cat_pred = cat.predict(X_test)

# ============================
# EVALUATION
# ============================

def evaluate(name, y_true, y_pred):

    mae = mean_absolute_error(y_true, y_pred)

    mse = mean_squared_error(y_true, y_pred)

    rmse = np.sqrt(mse)

    r2 = r2_score(y_true, y_pred)

    medae = median_absolute_error(y_true, y_pred)

    evs = explained_variance_score(y_true, y_pred)

    y_true_nonzero = np.where(y_true == 0, 1, y_true)

    mape = np.mean(
        np.abs((y_true - y_pred) / y_true_nonzero)
    ) * 100

    print("\n")
    print("=" * 50)
    print(name)
    print("=" * 50)

    print("MAE   :", round(mae, 2))
    print("RMSE  :", round(rmse, 2))
    print("R2    :", round(r2, 4))
    print("MAPE  :", round(mape, 2))
    print("MedAE :", round(medae, 2))
    print("EVS   :", round(evs, 4))

    return r2

rf_score = evaluate(
    "Random Forest",
    y_test,
    rf_pred
)

xgb_score = evaluate(
    "XGBoost",
    y_test,
    xgb_pred
)

cat_score = evaluate(
    "CatBoost",
    y_test,
    cat_pred
)

# ============================
# SAVE BEST MODEL
# ============================

scores = {
    "RandomForest": rf_score,
    "XGBoost": xgb_score,
    "CatBoost": cat_score
}

best_model_name = max(scores, key=scores.get)

print("\nBest Model:", best_model_name)

if best_model_name == "RandomForest":
    joblib.dump(rf, "best_model.pkl")

elif best_model_name == "XGBoost":
    joblib.dump(xgb, "best_model.pkl")

else:
    joblib.dump(cat, "best_model.pkl")

print("Model Saved Successfully")