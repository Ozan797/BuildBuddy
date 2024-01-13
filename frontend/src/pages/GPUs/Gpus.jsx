import { useState, useEffect } from "react";
import Card from "../../components/Card/Card";
import styles from "./Gpus.module.css"
import SearchComponent from "../../components/Search/SearchComponent";
import axios from "axios"
const Gpus = () => {
  const [gpuData, setGpuData] = useState([]);
  const backendURL = "http://127.0.0.1:5000/gpu_info";

  useEffect(() => {
    fetchGPUData();
  }, []);

  const fetchGPUData = async (searchQuery = "") => {
    try {
      const response = await axios.get(`${backendURL}?search_query=${searchQuery}`);
      setGpuData(response.data.gpu_info);
    } catch (error) {
      console.error("Error fetching GPU Data: ", error);
    }
  };

  return (
    <section>
      <h1>GPU Page</h1>
      <SearchComponent fetchData={fetchGPUData}/>
      <div className={styles.items}>
      <Card data={{gpu_info: gpuData}} className={styles.item} />
      </div>
    </section>
  );
};

export default Gpus;
