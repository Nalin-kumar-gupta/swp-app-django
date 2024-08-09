import axios from "axios";

const djangoUri = "http://localhost:8000/api";

const fetchApproval = async (truckId) => {
  try {
    console.log("truck_id", truckId)
    const response = await axios.get(`${djangoUri}/approval/`, {
      params: { truck_id: truckId }, // Send truck_id as a query parameter
    });
    return response.data; // Return the data as the resolved value of the promise
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error; // Reject the promise with the error
  }
};

const fetchApprovalApi = {
  fetchApproval,
};

export default fetchApprovalApi;


