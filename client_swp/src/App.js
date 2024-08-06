import React from 'react';
import ProductsPage from './pages/ProductPage';
import TruckVisualizer from './components/truckVisualizer';
import TruckPlot from './components/truckPlot';
import PlotComponent from './components/plotComponent';
import Button from '@mui/material/Button';
import ResponsiveAppBar from './components/appBar';

function App() {
  return (
    <div className="App">
      {/* <header className="App-header"> */}
        {/* <h1>Truck Packing Visualization</h1> */}
        {/* <TruckVisualizer /> */}
        {/* <PlotComponent /> */}
        {/* <TruckPlot /> */}
      {/* </header> */}
      {/* <Button variant='contained'>Hello</Button> */}
      <ResponsiveAppBar />
      <ProductsPage />
    </div>
  );
}

export default App;
