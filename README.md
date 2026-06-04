# AI Bus Occupancy Prediction System

## Overview

The AI Bus Occupancy Prediction System is a smart transportation analytics project that predicts bus seat occupancy, analyzes traffic conditions, and recommends optimized routes using Machine Learning and Graph Algorithms.

The system consists of:

* FastAPI Backend
* React Frontend
* Machine Learning Models
* Route Optimization Module
* Analytics Dashboard

---

## Features

### Occupancy Prediction

Predicts bus occupancy based on:

* Trip ID
* Stop ID
* Arrival Time
* Delay Minutes
* Peak Hour Information

### Traffic Analysis

Analyzes traffic conditions and categorizes them as:

* Low Traffic
* Moderate Traffic
* High Traffic

### Route Optimization

Uses:

* Dijkstra Algorithm
* A* Algorithm

to determine the most efficient route between bus stops.

### Analytics Dashboard

Provides:

* Average Occupancy
* Maximum Occupancy
* Minimum Occupancy
* Average Delay
* Peak Hour Percentage

---

## Technologies Used

### Frontend

* React.js
* React Router
* Axios
* Vite

### Backend

* FastAPI
* Pandas
* NumPy
* Joblib

### Machine Learning

* Random Forest Regressor
* XGBoost Regressor
* CatBoost Regressor

### Graph Algorithms

* NetworkX
* Dijkstra Algorithm
* A* Algorithm

---

## Project Structure

```text
AI_Bus_Occupancy_Project/

├── backend/
│   ├── main.py
│   ├── train_models.py
│   ├── route_optimizer.py
│   ├── requirements.txt
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
└── README.md
```

---

## Machine Learning Models

The following models were trained and evaluated:

| Model         | R² Score |
| ------------- | -------- |
| Random Forest | 0.7996   |
| XGBoost       | 0.7860   |
| CatBoost      | 0.8130   |

Best Model Selected:

```text
CatBoost Regressor
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI_Bus_Occupancy_Project
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Install Backend Dependencies

```bash
pip install -r backend/requirements.txt
```

### Install Frontend Dependencies

```bash
cd frontend
npm install
```

---

## Run Backend

```bash
cd backend

python -m uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
cd frontend

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## API Endpoints

### Home

```http
GET /
```

### Predict Occupancy

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

### Traffic Analysis

```http
POST /traffic
```

### Analytics

```http
GET /analytics
```

### Health Check

```http
GET /health
```

---

## Route Optimization

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

## Sample Output

### Occupancy Prediction

```json
{
  "predicted_occupancy": 87.48,
  "occupancy_level": "High"
}
```

### Traffic Prediction

```json
{
  "traffic_level": 1,
  "traffic_status": "Moderate"
}
```

---

## Future Enhancements

* Real-time BMTC data integration
* GPS-based route tracking
* Live traffic API integration
* Interactive charts and visualizations
* Mobile application support

---

## Author

Sahana Muthu

Computer Science and Engineering

AI Bus Occupancy Prediction System
