import axios from "axios";

const djangoUri = "http://localhost:8000/api";

const fetchProductData = async () => {
  try {
    const response = await axios.get(`${djangoUri}/packages/`);
    return response.data; // Return the data as the resolved value of the promise
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error; // Reject the promise with the error
  }
};

const productApi = {
  fetchProductData,
};

export default productApi;