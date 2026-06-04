import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import API from "../services/api";

function Analytics() {

  const [data, setData] = useState(null);

  useEffect(() => {

    const fetchAnalytics = async () => {

      try {

        const res = await API.get("/analytics");

        setData(res.data);

      } catch (err) {

        console.log(err);

      }

    };

    fetchAnalytics();

  }, []);

  return (

    <div>

      <Navbar />

      <div style={{ display: "flex" }}>

        <Sidebar />

        <div
          style={{
            padding: "30px",
            width: "100%"
          }}
        >

          <h1>Analytics Dashboard</h1>

          <br />

          {!data ? (

            <h3>Loading Analytics...</h3>

          ) : (

            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(2, 300px)",
                gap: "20px"
              }}
            >

              <div
                style={{
                  background: "#2563eb",
                  color: "white",
                  padding: "20px",
                  borderRadius: "10px"
                }}
              >
                <h3>Average Occupancy</h3>
                <h1>{data.average_occupancy}</h1>
              </div>

              <div
                style={{
                  background: "#16a34a",
                  color: "white",
                  padding: "20px",
                  borderRadius: "10px"
                }}
              >
                <h3>Maximum Occupancy</h3>
                <h1>{data.maximum_occupancy}</h1>
              </div>

              <div
                style={{
                  background: "#ea580c",
                  color: "white",
                  padding: "20px",
                  borderRadius: "10px"
                }}
              >
                <h3>Minimum Occupancy</h3>
                <h1>{data.minimum_occupancy}</h1>
              </div>

              <div
                style={{
                  background: "#9333ea",
                  color: "white",
                  padding: "20px",
                  borderRadius: "10px"
                }}
              >
                <h3>Average Delay</h3>
                <h1>{data.average_delay} min</h1>
              </div>

              <div
                style={{
                  background: "#0891b2",
                  color: "white",
                  padding: "20px",
                  borderRadius: "10px"
                }}
              >
                <h3>Peak Hour %</h3>
                <h1>{data.peak_hour_percentage}%</h1>
              </div>

            </div>

          )}

        </div>

      </div>

    </div>

  );

}

export default Analytics;