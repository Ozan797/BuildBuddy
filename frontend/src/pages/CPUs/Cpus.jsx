import { useState, useEffect } from "react";
import Card from "../../components/Card/Card";

const Cpus = () => {
  const [cpuData, setCpuData] = useState([]);

  useEffect(() => {
    fetchCPUData();
  }, []);

  const fetchCPUData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/cpu_info");
      const cpuApiResponse = await response.json();
      setCpuData(cpuApiResponse);
    } catch (error) {
      console.error("Error fetching CPU Data:", error);
    }
  };

  return (
    <>
      <h1>CPU Page</h1>
      <Card data={cpuData} />
    </>
  );
};

export default Cpus;
