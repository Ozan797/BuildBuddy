import { useState, useEffect } from "react";
import Card from "../../components/Card/Card";


const PowerSupplies = () => {
  const [psuData, setPsuData] = useState([]);

  useEffect(() => {
    fetchPSUData();
  }, []);

  const fetchPSUData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/psu_info");
      const psuApiResponse = await response.json();
      setPsuData(psuApiResponse);
    } catch (error) {
      console.error("Error fetching Power Supplies Data: ", error);
    }
  };

  return (
    <div>
      <h1>Power Supplies Page</h1>
      <Card data={psuData} />
    </div>
  );
};


export default PowerSupplies