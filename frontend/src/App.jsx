import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Cpus, Gpus, Ram, PowerSupplies, ErrorPage } from "./pages";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" />
          <Route path="/cpus" element={<Cpus />} />
          <Route path="/gpus" element={<Gpus />} />
          <Route path="/ram" element={<Ram />} />
          <Route path="/power-supplies" element={<PowerSupplies />} />
          <Route path="/*" element={<ErrorPage />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
