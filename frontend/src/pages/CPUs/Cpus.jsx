import { useState, useEffect } from "react";
import Card from "../../components/Card/Card";
import styles from "./Cpus.module.css";
import axios from "axios";
import SearchComponent from "../../components/Search/SearchComponent";


const Cpus = () => {
  const [cpuData, setCpuData] = useState([]);

  const backendURL = "http://127.0.0.1:5000/cpu_info";

  useEffect(() => {
    fetchCPUData();
  }, []);

  const fetchCPUData = async (searchQuery = "") => {
    try {
      const response = await axios.get(`${backendURL}?search_query=${searchQuery}`);
      setCpuData(response.data.cpu_info);
    } catch (error) {
      console.error("Error fetching CPU Data:", error);
    }
  };

  return (
    <section>
      <h1>CPU Page</h1>
      <SearchComponent fetchData={fetchCPUData} />
      <div className={styles.items}>
        <Card data={{cpu_info: cpuData}} className={styles.item} />
      </div>
    </section>
  );
};

export default Cpus;