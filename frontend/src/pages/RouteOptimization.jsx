import React, { useState } from "react";

function RouteOptimization() {
  const [source, setSource] = useState("");
  const [destination, setDestination] = useState("");
  const [route, setRoute] = useState([]);

  const findRoute = () => {
    const sampleRoute = [
      source,
      "KR Market",
      "Lalbagh",
      destination,
    ];

    setRoute(sampleRoute);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Route Optimization</h2>

      <input
        type="text"
        placeholder="Source"
        value={source}
        onChange={(e) => setSource(e.target.value)}
      />

      <br />
      <br />

      <input
        type="text"
        placeholder="Destination"
        value={destination}
        onChange={(e) => setDestination(e.target.value)}
      />

      <br />
      <br />

      <button onClick={findRoute}>
        Find Route
      </button>

      {route.length > 0 && (
        <div>
          <h3>Optimal Route</h3>
          <p>{route.join(" ➜ ")}</p>
        </div>
      )}
    </div>
  );
}

export default RouteOptimization;