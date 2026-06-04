import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Prediction from "./pages/Prediction";
import Traffic from "./pages/Traffic";
import Analytics from "./pages/Analytics";
import RouteOptimization from "./pages/RouteOptimization";
import Admin from "./pages/Admin";

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Dashboard />}
        />

        <Route
          path="/prediction"
          element={<Prediction />}
        />

        <Route
          path="/traffic"
          element={<Traffic />}
        />

        <Route
          path="/analytics"
          element={<Analytics />}
        />

        <Route
          path="/route"
          element={<RouteOptimization />}
        />

        <Route
          path="/admin"
          element={<Admin />}
        />

      </Routes>

    </BrowserRouter>

  );

}

export default App;