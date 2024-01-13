/* eslint-disable react/prop-types */
import styles from "./Card.module.css"
const Card = ({ data }) => {
  const openGoogleSearch = (name) => {
    window.open(`https://www.google.com/search?q=${encodeURIComponent(name)}`, "_blank");
  };
  
  // CPU Card
  const renderCPUCard = (cpu) => {
    return (
      <div className={styles.card}>
        <h2 className={styles.name}>{cpu.name}</h2>
        <p className={styles.space}>Brand: {cpu.brand}</p>
        <p className={styles.space}>Frequency: {cpu.frequency}MHz</p>
        <p className={styles.space}>Price: £{cpu.price}</p>
        <button onClick={() => openGoogleSearch(cpu.name)}>Search on Google</button>
      </div>
    );
  };
  // GPU Card
  const renderGPUCard = (gpu) => {
    return (
      <div className={styles.card}>
        <h2 className={styles.name}>{gpu.name}</h2>
        <p className={styles.space}>Brand: {gpu.brand}</p>
        <p className={styles.space}>Memory: {gpu.memory}GB</p>
        <p className={styles.space}>Price: £{gpu.price}</p>
        <button onClick={() => openGoogleSearch(gpu.name)}>Search on Google</button>
      </div>
    );
  };
  // Power Supply Card
  const renderPSUCard = (psu) => {
    return (
      <div className={styles.card}>
        <h2 className={styles.name}>{psu.name}</h2>
        <p className={styles.space}>Power: {psu.power}W</p>
        <p className={styles.space}>Price: £{psu.price}</p>
        <button onClick={() => openGoogleSearch(psu.name)}>Search on Google</button>
      </div>
    );
  };
  // RAM Card
  const renderRAMCard = (ram) => {
    return (
      <div className={styles.card}>
        <h2 className={styles.name}>{ram.name}</h2>
        <p className={styles.space}>Brand: {ram.brand}</p>
        <p className={styles.space}>RAM Type: {ram.ram_type}</p>
        <p className={styles.space}>Frequency: {ram.frequency}MHz</p>
        <p className={styles.space}>Price: £{ram.price}</p>
        <button onClick={() => openGoogleSearch(ram.name)}>Search on Google</button>
      </div>
    );
  };

  // Determine the type of data and render the appropriate card
  if (data.cpu_info) {
    return data.cpu_info.map((cpu, index) => (
      <div key={index}>{renderCPUCard(cpu)}</div>
    ));
    // PSU
  } else if (data.psu_info) {
    return data.psu_info.map((psu, index) => (
      <div key={index}>{renderPSUCard(psu)}</div>
    ));
    // GPU
  } else if (data.gpu_info) {
    return data.gpu_info.map((gpu, index) => (
      <div key={index}>{renderGPUCard(gpu)}</div>
    ));
    // RAM
  } else if (data.ram_info) {
    return data.ram_info.map((ram, index) => (
      <div key={index}>{renderRAMCard(ram)}</div>
    ));
  } else {
    return <div>No data available</div>;
  }
};

export default Card;
