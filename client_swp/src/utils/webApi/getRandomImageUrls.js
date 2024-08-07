const getRandomImageUrls = (numberOfImages, width, height) => {
    const imageIds = [
      '10', '11', '49', '61', '74', 
      '76', '122', '142', '164'
    ];


  
    // Shuffle the array of image IDs
    const shuffledIds = shuffleArray(imageIds);
  
    // Select the first 'numberOfImages' from the shuffled array
    const selectedIds = shuffledIds.slice(0, numberOfImages);
  
    // Generate image URLs using the selected IDs
    const imageUrls = selectedIds.map(id => `https://picsum.photos/${width}/${height}?image=${id}`);
  
    return imageUrls;
  };
  
  const shuffleArray = (array) => {
    // Fisher-Yates shuffle algorithm
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  };
  
  export default getRandomImageUrls;