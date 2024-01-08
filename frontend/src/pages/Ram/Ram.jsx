import { useState, useEffect } from "react";
import Card from "../../components/Card/Card";

const Ram = () => {

  const [ramData, setRamData] = useState([]);

  useEffect(() => {
    fetchRAMData();
  }, []);

  const fetchRAMData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/ram_info");
      const ramApiResponse = await response.json();
      setRamData(ramApiResponse);
    } catch (error) {
      console.error("Error fetching GPU Data: ", error);
    }
  };

  return (
    <div>
      <h1>RAM Page</h1>
      <Card data={ramData} />
    </div>
  )
}

export default Ram