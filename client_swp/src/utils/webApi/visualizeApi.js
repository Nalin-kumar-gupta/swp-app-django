import axios from "axios";

const djangoUri = "http://localhost:8000/api";

const visualize = async (req) => {
  const { truckId } = req;
  try {
    const response = await axios.post(`${djangoUri}/visualize-packages/`, {
      truck_id: truckId,
    });
    return response.data; // Return the data as the resolved value of the promise
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error; // Reject the promise with the error
  }
};

const visualizeApi = {
  visualize,
};

export default visualizeApi;
