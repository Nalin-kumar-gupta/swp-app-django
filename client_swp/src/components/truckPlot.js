import React, { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';

const TruckPlot = () => {
  const [plotData, setPlotData] = useState([]);
  const [plotLayout, setPlotLayout] = useState({});

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/demo/')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Data received:', data);

        // Validate the data structure for 3D plots
        if (Array.isArray(data.data) && data.layout && data.layout.scene) {
          setPlotData(data.data);
          setPlotLayout(data.layout);
        } else {
          console.error('Unexpected data format:', data);
        }
      })
      .catch(error => {
        console.error('Error fetching plot data:', error);
      });
  }, []);

  return (
    <div>
      {plotData.length > 0 && plotLayout ? (
        <Plot
          data={plotData}
          layout={plotLayout}
          style={{ width: '100%', height: '100%' }}
          config={{ responsive: true }} // Ensures the plot resizes correctly
        />
      ) : (
        <p>Loading plot...</p>
      )}
    </div>
  );
};

export default TruckPlot;
