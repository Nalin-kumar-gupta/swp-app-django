import axios from "axios";

const djangoUri = "http://localhost:8000/api";

const fetchVehicleData = async () => {
  try {
    const response = await axios.get(`${djangoUri}/trucks-boarding/`);
    return response.data; // Return the data as the resolved value of the promise
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error; // Reject the promise with the error
  }
};

const vehicleApi = {
  fetchVehicleData,
};

export default vehicleApi;