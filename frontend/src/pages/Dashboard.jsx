import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import StatCard from "../components/StatCard";

function Dashboard() {
  return (
    <div>

      <Navbar />

      <div
        style={{
          display: "flex"
        }}
      >

        <Sidebar />

        <div
          style={{
            padding: "30px",
            width: "100%"
          }}
        >

          <h1
            style={{
              fontSize: "40px"
            }}
          >
            Dashboard
          </h1>

          <p>
            Smart Transportation Analytics
          </p>

          <br />

          <div
            style={{
              display: "flex",
              gap: "20px",
              flexWrap: "wrap"
            }}
          >

            <StatCard
              title="Occupancy"
              value="72%"
              color="#2563eb"
            />

            <StatCard
              title="Traffic"
              value="Moderate"
              color="#ea580c"
            />

            <StatCard
              title="ETA"
              value="28 min"
              color="#16a34a"
            />

            <StatCard
              title="Routes"
              value="12"
              color="#9333ea"
            />

          </div>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;