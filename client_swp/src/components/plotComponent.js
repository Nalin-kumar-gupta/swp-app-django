import React, { useEffect, useState } from 'react';

function PlotComponent() {
  const [plotImage, setPlotImage] = useState('');

  useEffect(() => {
    fetch('/api/demo123/')
      .then(response => response.blob())
      .then(blob => {
        // Convert the image blob to a base64-encoded data URL
        const reader = new FileReader();
        reader.readAsDataURL(blob);
        reader.onloadend = () => {
          setPlotImage(reader.result);
        };
      });
  }, []);

  return (
    <div>
      {plotImage && <img src={plotImage} alt="Matplotlib plot" />}
    </div>
  );
}

export default PlotComponent;