import React, { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';

const TruckVisualizer = () => {
  const [data, setData] = useState({ truck: {}, occupied_boxes: [] });

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('/api/packing-visualizer/', {
        method: 'GET',
      });
      const result = await response.json();
      setData(result);
    };

    fetchData();
  }, []);

  const truck = data.truck;
  const occupied_boxes = data.occupied_boxes;

  const plotData = occupied_boxes.map((box) => ({
    type: 'mesh3d',
    x: [box.x, box.x + box.length, box.x + box.length, box.x, box.x, box.x + box.length, box.x + box.length, box.x],
    y: [box.y, box.y, box.y + box.breadth, box.y + box.breadth, box.y, box.y, box.y + box.breadth, box.y + box.breadth],
    z: [box.z, box.z, box.z, box.z, box.z + box.height, box.z + box.height, box.z + box.height, box.z + box.height],
    i: [0, 0, 0, 1, 1, 2],
    j: [1, 2, 3, 4, 5, 6],
    k: [2, 3, 1, 3, 6, 7],
    color: 'rgba(0, 100, 200, 0.6)',
    showscale: false,
  }));

  return (
    <div>
      <Plot
        data={plotData}
        layout={{
          title: 'Truck and Boxes Visualization',
          scene: {
            xaxis: { title: 'Length', range: [0, truck.length] },
            yaxis: { title: 'Breadth', range: [0, truck.breadth] },
            zaxis: { title: 'Height', range: [0, truck.height] },
          },
          autosize: true,
        }}
        style={{ width: '100%', height: '100%' }}
      />
    </div>
  );
};

export default TruckVisualizer;
