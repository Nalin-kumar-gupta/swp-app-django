import * as React from "react";

const RandomImage = ({ ...props }) => {
  const imageUrls = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpc1YZzr3vRd0mjk1eJ4z_44CdAj6yGPGLYA&s", // Replace with your actual image URLs
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlLg_CU5d_XiA6JEC1XjKDY8qYRZHZtbI7292-uSQc5ocy4olCo9qu6vQ1PDOWYl_Mby4&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS90_cUgTLDY4sp9AqWPH3r_tA-yhPo1hP-HA&s",
  ];
  const randomImageUrl = imageUrls[Math.floor(Math.random() * imageUrls.length)];
  return <img src={randomImageUrl} {...props} alt="Random truck" />;
};

export default RandomImage;
