// Loader.js
import React from 'react';
import './Loader.css'; // Import the CSS for the loader

const Loader = () => (
  <div className="loader-container">
    <div className="loader">
      <div className="cell d-0"></div>
      <div className="cell d-1"></div>
      <div className="cell d-2"></div>
      <div className="cell d-1"></div>
      <div className="cell d-2"></div>
      <div className="cell d-2"></div>
      <div className="cell d-3"></div>
      <div className="cell d-3"></div>
      <div className="cell d-4"></div>
    </div>
  </div>
);

export default Loader;
