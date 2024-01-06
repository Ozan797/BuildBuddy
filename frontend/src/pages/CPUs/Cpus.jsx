import { useState, useEffect } from "react";
import Card from "../../components/Card/Card";
import styles from "./Cpus.module.css"
const Cpus = () => {
  const [cpuData, setCpuData] = useState([]);

  const url = "http://127.0.0.1:5000/cpu_info"
  useEffect(() => {
    fetchCPUData();
  }, []);

  const fetchCPUData = async () => {
    try {
      const response = await fetch(url);
      const cpuApiResponse = await response.json();
      setCpuData(cpuApiResponse);
    } catch (error) {
      console.error("Error fetching CPU Data:", error);
    }
  };

  return (
    <section>
      <h1>CPU Page</h1>
      
      <div className={styles.gridContainer}>
      <Card data={cpuData} />
      </div>
    </section>
  );
};

export default Cpus;
