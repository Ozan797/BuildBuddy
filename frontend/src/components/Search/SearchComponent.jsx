import React, { useState } from "react";

const SearchComponent = ({ fetchData }) => {
  const [searchQuery, setSearchQuery] = useState("");

  const handleSearch = () => {
    fetchData(searchQuery);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Search..."
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
};

export default SearchComponent;