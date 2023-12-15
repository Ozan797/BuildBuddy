import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [responseData, setResponseData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/psu_info'); // Replace this URL with your API endpoint
        setResponseData(response.data); // Assuming the response is JSON
      } catch (error) {
        // Handle error, for instance, set an error state
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);
  return (
    
    <>
      <div>
      {responseData ? (
        <pre>{JSON.stringify(responseData, null, 2)}</pre>
      ) : (
        <p>Loading...</p>
      )}
    </div>
    </>
  )
}

export default App
