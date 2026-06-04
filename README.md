# AI Bus Occupancy Prediction System

## Overview

AI Bus Occupancy Prediction System is a Smart Transportation Analytics project that predicts bus occupancy, analyzes traffic conditions, and optimizes routes using Machine Learning and Graph Algorithms.

The system combines:

* React Frontend
* FastAPI Backend
* CatBoost Machine Learning Model
* Traffic Analysis Module
* Route Optimization Module
* Analytics Dashboard

---

# Features

## Occupancy Prediction

Predicts bus occupancy using:

* Trip ID
* Stop ID
* Arrival Time
* Delay Minutes
* Peak Hour Information

## Traffic Analysis

Classifies traffic into:

* Low
* Moderate
* High

## Route Optimization

Uses:

* Dijkstra Algorithm
* A* Algorithm

to determine the optimal route.

## Analytics Dashboard

Displays:

* Average Occupancy
* Maximum Occupancy
* Minimum Occupancy
* Average Delay
* Peak Hour Percentage

---

# Technologies Used

## Frontend

* React.js
* Vite
* Axios
* React Router

## Backend

* FastAPI
* Pandas
* NumPy
* Joblib

## Machine Learning

* Random Forest
* XGBoost
* CatBoost

## Graph Algorithms

* NetworkX
* Dijkstra Algorithm
* A* Algorithm

---

# Project Structure

```text
AI_Bus_Occupancy_Project/

├── backend/
│   ├── main.py
│   ├── train_models.py
│   ├── route_optimizer.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── dataset/
│   └── BusOccupancyDataset.csv
│
├── models/
│   ├── best_model.pkl
│   ├── trip_encoder.pkl
│   └── stop_encoder.pkl
│
├── Run_Project.bat
├── Stop_Project.bat
│
└── README.md
```

---

# Machine Learning Results

| Model         | R² Score |
| ------------- | -------- |
| Random Forest | 0.7996   |
| XGBoost       | 0.7860   |
| CatBoost      | 0.8130   |

Best Model:

```text
CatBoost Regressor
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd AI_Bus_Occupancy_Project
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

## Install Backend Dependencies

```bash
pip install -r backend/requirements.txt
```

## Install Frontend Dependencies

```bash
cd frontend
npm install
```

---

# Running the Project

## Option 1: Manual Start

### Backend

```bash
cd backend

python -m uvicorn main:app --reload
```

### Frontend

```bash
cd frontend

npm run dev
```

---

## Option 2: One Click Startup

Create a file named:

```text
Run_Project.bat
```

Paste:

```bat
@echo off

echo Starting Backend...

start cmd /k "cd /d %~dp0backend && ..\venv\Scripts\activate && python -m uvicorn main:app --reload"

timeout /t 3 > nul

echo Starting Frontend...

start cmd /k "cd /d %~dp0frontend && npm run dev"

timeout /t 5 > nul

start http://127.0.0.1:8000/docs

echo.
echo ====================================
echo AI Bus Occupancy Project Started
echo ====================================

pause
```

Now simply double-click:

```text
Run_Project.bat
```

to launch the entire application.

---

# Stop Script

Create:

```text
Stop_Project.bat
```

Paste:

```bat
@echo off

taskkill /F /IM python.exe
taskkill /F /IM node.exe

echo Project stopped successfully.

pause
```

Double-click:

```text
Stop_Project.bat
```

to stop both backend and frontend.

---

# API Endpoints

## Home

```http
GET /
```

## Predict Occupancy

```http
POST /predict
```

Sample Request:

```json
{
  "trip_id": "500D-1",
  "stop_id": "500D-1#5",
  "arrival_time": "08:30",
  "delay_min": 4,
  "is_peak_hour": 1
}
```

Sample Response:

```json
{
  "predicted_occupancy": 87.48,
  "occupancy_level": "High"
}
```

---

## Traffic Analysis

```http
POST /traffic
```

Response Example:

```json
{
  "traffic_level": 1,
  "traffic_status": "Moderate"
}
```

---

## Analytics

```http
GET /analytics
```

Returns:

* Average Occupancy
* Maximum Occupancy
* Minimum Occupancy
* Average Delay
* Peak Hour Percentage

---

## Health Check

```http
GET /health
```

---

# Route Optimization

Supported Stops:

* Majestic
* KR Market
* Lalbagh
* Jayanagar
* BTM
* Silk Board
* Electronic City

Algorithms Used:

* Dijkstra Algorithm
* A* Algorithm

---

# Future Enhancements

* Live BMTC Data Integration
* GPS Tracking
* Real-Time Traffic APIs
* Interactive Data Visualizations
* Mobile App Support

---

# Author

**Sahana Muthu**

Computer Science and Engineering

AI Bus Occupancy Prediction System
