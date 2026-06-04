import React, { useState } from "react";
import axios from "axios";

function Traffic() {
  const [delay, setDelay] = useState("");
  const [result, setResult] = useState(null);

  const checkTraffic = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/traffic",
        {
          trip_id: "500D-1",
          stop_id: "500D-1#5",
          arrival_time: "08:30",
          delay_min: Number(delay),
          is_peak_hour: 1,
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Backend not running");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Traffic Prediction</h2>

      <input
        type="number"
        placeholder="Enter Delay Minutes"
        value={delay}
        onChange={(e) => setDelay(e.target.value)}
      />

      <button onClick={checkTraffic}>
        Check Traffic
      </button>

      {result && (
        <div>
          <h3>Traffic Status</h3>
          <p>Level: {result.traffic_level}</p>
          <p>Status: {result.traffic_status}</p>
        </div>
      )}
    </div>
  );
}

export default Traffic;