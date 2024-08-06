import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import { TextField } from "@mui/material";
import InputAdornment from "@mui/material/InputAdornment";
import Divider from "@mui/material/Divider";
import { useState } from "react";
import moment from "moment";

const isValid = (productData) => {
  Object.entries(productData).forEach(([key, val]) => {
    if (val == "" || !val) {
      return false;
    }
  });
  return true;
};

const initialProductDetails = {
  deliver_date: moment().format("YYYY-MM-DD"),
  length: "",
  breadth: "",
  height: "",
  weight: "",
  destination: "",
};

const ProductForm = (props) => {
  const { productData, setProductData, setVehicleModalOpen } = props;
  const [productDetails, setProductsDetails] = useState(initialProductDetails);
  const addProductData = (e) => {
    e.preventDefault();
    if (!isValid(productDetails)) {
      return;
    }
    setProductData([...productData, productDetails]);
    setProductsDetails({
      ...initialProductDetails,
      deliver_date: productDetails.deliver_date,
    });
  };
  const handleChange = (e) => {
    const { name, value } = e.target;
    setProductsDetails({ ...productDetails, [name]: value });
  };
  return (
    <div style={{ margin: "10px" }}>
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <Typography variant="h6" sx={{ fontWeight: "bold" }}>
          Product
        </Typography>
        <Button
          disabled={productData.length == 0}
          color="success"
          variant="contained"
          onClick={() => setVehicleModalOpen(true)}
        >
          Visualize
        </Button>
      </div>
      <Divider
        style={{
          margin: "15px 15px 0 0",
          fontSize: "15px",
          fontWeight: "bold",
          color: "grey",
        }}
      >
        Add Product Details
      </Divider>
      <form onSubmit={addProductData} style={{ marginTop: "10px" }}>
        <TextField
          label="Length"
          name="length"
          value={productDetails.length}
          id="outlined-start-adornment"
          type="number"
          sx={{ m: 1, width: "25ch" }}
          InputProps={{
            endAdornment: <InputAdornment position="end">m</InputAdornment>,
          }}
          onChange={handleChange}
          required
        />
        <TextField
          label="Breadth"
          name="breadth"
          value={productDetails.breadth}
          id="outlined-start-adornment"
          type="number"
          sx={{ m: 1, width: "25ch" }}
          InputProps={{
            endAdornment: <InputAdornment position="end">m</InputAdornment>,
          }}
          onChange={handleChange}
          required
        />
        <TextField
          label="Height"
          name="height"
          value={productDetails.height}
          id="outlined-start-adornment"
          type="number"
          sx={{ m: 1, width: "25ch" }}
          InputProps={{
            endAdornment: <InputAdornment position="end">m</InputAdornment>,
          }}
          onChange={handleChange}
          required
        />
        <TextField
          label="Weight"
          name="weight"
          value={productDetails.weight}
          id="outlined-start-adornment"
          type="number"
          sx={{ m: 1, width: "25ch" }}
          InputProps={{
            endAdornment: <InputAdornment position="end">kg</InputAdornment>,
          }}
          onChange={handleChange}
          required
        />
        <TextField
          label="Destination"
          name="destination"
          value={productDetails.destination}
          id="outlined-start-adornment"
          sx={{ m: 1, width: "25ch" }}
          onChange={handleChange}
          required
        />
        <TextField
          label="Deliver Date"
          name="deliver_date"
          value={productDetails.deliver_date}
          sx={{ m: 1, width: "25ch" }}
          type="date"
          onChange={handleChange}
          required
        />
        <Button
          sx={{ margin: "5px 0 0 10px", display: "block" }}
          variant="outlined"
          type="submit"
        >
          Add Product
        </Button>
      </form>
    </div>
  );
};

export default ProductForm;
