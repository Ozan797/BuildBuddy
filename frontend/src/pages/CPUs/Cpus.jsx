import { useState, useEffect } from "react";
import Card from "../../components/Card/Card";
import styles from "./Cpus.module.css";
import axios from "axios";

const Cpus = () => {
  const [cpuData, setCpuData] = useState([]);
  const [searchQuery, setSearchQuery] = useState(""); // State to store the search query

  const backendURL = "http://127.0.0.1:5000/cpu_info";

  useEffect(() => {
    fetchCPUData();
  }, []);

  const fetchCPUData = async () => {
    try {
      const response = await axios.get(backendURL); // Fetch all CPU data initially
      setCpuData(response.data.cpu_info);
    } catch (error) {
      console.error("Error fetching CPU Data:", error);
    }
  };

  const handleSearch = async () => {
    try {
      const response = await axios.get(`${backendURL}?search_query=${searchQuery}`); // Fetch CPU data based on search query
      setCpuData(response.data.cpu_info);
    } catch (error) {
      console.error("Error fetching CPU Data:", error);
    }
  };

  const handleInputChange = (e) => {
    setSearchQuery(e.target.value); // Update searchQuery state as the user types
  };

  return (
    <section>
      <h1>CPU Page</h1>
      <div>
        <input
          type="text"
          placeholder="Search CPUs"
          value={searchQuery}
          onChange={handleInputChange}
        />
        <button onClick={handleSearch}>Search</button>
      </div>
      <div className={styles.items}>
        <Card data={{ cpu_info: cpuData }} />
      </div>
    </section>
  );
};

export default Cpus;
