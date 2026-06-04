import { Link } from "react-router-dom";

function Sidebar() {

  return (

    <div
      style={{
        width: "250px",
        height: "100vh",
        background: "#1e293b",
        color: "white",
        padding: "20px"
      }}
    >

      <h2>Navigation</h2>

      <hr />

      <div style={{ marginTop: "20px" }}>

        <p>
          <Link
            to="/"
            style={{ color: "white" }}
          >
            Dashboard
          </Link>
        </p>

        <p>
          <Link
            to="/prediction"
            style={{ color: "white" }}
          >
            Occupancy Prediction
          </Link>
        </p>

        <p>
          <Link
            to="/traffic"
            style={{ color: "white" }}
          >
            Traffic Analysis
          </Link>
        </p>

        <p>
          <Link
            to="/route"
            style={{ color: "white" }}
          >
            Route Optimization
          </Link>
        </p>

        <p>
          <Link
            to="/analytics"
            style={{ color: "white" }}
          >
            Analytics
          </Link>
        </p>

        <p>
          <Link
            to="/admin"
            style={{ color: "white" }}
          >
            Admin
          </Link>
        </p>

      </div>

    </div>

  );
}

export default Sidebar;