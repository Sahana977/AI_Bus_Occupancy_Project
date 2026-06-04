
import { useState } from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import API from "../services/api";

function Prediction() {

  const [result, setResult] = useState(null);

  const [form, setForm] = useState({
    trip_id: "500D-1",
    stop_id: "500D-1#5",
    arrival_time: "08:30",
    delay_min: 4,
    is_peak_hour: 1
  });

  const predict = async () => {

    try {

      const response = await API.post(
        "/predict",
        form
      );

      setResult(response.data);

    } catch (err) {

      console.error("FULL ERROR:", err);
      console.error("RESPONSE:", err.response);
      console.error("MESSAGE:", err.message);

      alert(
        err.response?.data?.detail ||
        err.message ||
        "Prediction failed"
      );
    }
  };

  return (
    <div>

      <Navbar />

      <div style={{ display: "flex" }}>

        <Sidebar />

        <div
          style={{
            width: "100%",
            padding: "40px",
            textAlign: "center"
          }}
        >

          <h1>Occupancy Prediction</h1>

          <br />

          <div>

            <label>Trip ID</label>

            <br />

            <input
              type="text"
              value={form.trip_id}
              onChange={(e) =>
                setForm({
                  ...form,
                  trip_id: e.target.value
                })
              }
            />

            <br />
            <br />

            <label>Stop ID</label>

            <br />

            <input
              type="text"
              value={form.stop_id}
              onChange={(e) =>
                setForm({
                  ...form,
                  stop_id: e.target.value
                })
              }
            />

            <br />
            <br />

            <label>Arrival Time</label>

            <br />

            <input
              type="text"
              value={form.arrival_time}
              onChange={(e) =>
                setForm({
                  ...form,
                  arrival_time: e.target.value
                })
              }
            />

            <br />
            <br />

            <label>Delay (minutes)</label>

            <br />

            <input
              type="number"
              value={form.delay_min}
              onChange={(e) =>
                setForm({
                  ...form,
                  delay_min: Number(e.target.value)
                })
              }
            />

            <br />
            <br />

            <button
              onClick={predict}
              style={{
                padding: "12px 24px",
                background: "#2563eb",
                color: "white",
                border: "none",
                cursor: "pointer",
                borderRadius: "5px"
              }}
            >
              Predict Occupancy
            </button>

          </div>

          {result && (

            <div
              style={{
                marginTop: "30px",
                background: "#ffffff",
                padding: "20px",
                borderRadius: "10px",
                width: "350px",
                marginLeft: "auto",
                marginRight: "auto",
                boxShadow:
                  "0px 0px 10px rgba(0,0,0,0.2)"
              }}
            >

              <h2>Prediction Result</h2>

              <h1>
                {result.predicted_occupancy}
              </h1>

              <h3>
                Occupancy Level:
                {" "}
                {result.occupancy_level}
              </h3>

            </div>

          )}

        </div>

      </div>

    </div>
  );
}

export default Prediction;

