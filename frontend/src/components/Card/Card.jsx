/* eslint-disable react/prop-types */
const Card = ({ data }) => {
  // CPU Card
  const renderCPUCard = (cpu) => {
    return (
      <div className="cpuCard">
        <h2>{cpu.name}</h2>
        <p>Brand: {cpu.brand}</p>
        <p>Frequency: {cpu.frequency}MHz</p>
        <p>Price: £{cpu.price}</p>
      </div>
    );
  };
  // GPU Card
  const renderGPUCard = (gpu) => {
    return (
      <div className="gpuCard">
        <h2>{gpu.name}</h2>
        <p>Brand: {gpu.brand}</p>
        <p>Memory: {gpu.memory}GB</p>
        <p>Price: £{gpu.price}</p>
      </div>
    );
  };
  // Power Supply Card
  const renderPSUCard = (psu) => {
    return (
      <div className="psuCard">
        <h2>{psu.name}</h2>
        <p>Power: {psu.power}W</p>
        <p>Price: £{psu.price}</p>
      </div>
    );
  };
  // RAM Card
  const renderRAMCard = (ram) => {
    return (
      <div className="ramCard">
        <h2>{ram.name}</h2>
        <p>Brand: {ram.brand}</p>
        <p>RAM Type: {ram.ram_type}</p>
        <p>Frequency: {ram.frequency}MHz</p>
        <p>Price: £{ram.price}</p>
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
