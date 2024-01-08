import { useState, useEffect } from "react";
import Card from "../../components/Card/Card";

const Gpus = () => {
  const [gpuData, setGpuData] = useState([]);

  useEffect(() => {
    fetchGPUData();
  }, []);

  const fetchGPUData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/gpu_info");
      const gpuApiResponse = await response.json();
      setGpuData(gpuApiResponse);
    } catch (error) {
      console.error("Error fetching GPU Data: ", error);
    }
  };

  return (
    <div>
      <h1>GPU Page</h1>
      <Card data={gpuData} />
    </div>
  );
};

export default Gpus;
