import React from 'react';
import TruckVisualizer from './components/truckVisualizer';
import TruckPlot from './components/truckPlot';
import PlotComponent from './components/plotComponent';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Truck Packing Visualization</h1>
        {/* <TruckVisualizer /> */}
        <PlotComponent />
        {/* <TruckPlot /> */}
      </header>
    </div>
  );
}

export default App;
