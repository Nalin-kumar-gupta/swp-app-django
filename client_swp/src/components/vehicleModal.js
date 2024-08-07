import { useState, useEffect } from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import Modal from "@mui/material/Modal";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";
import vehicleApi from "../utils/webApi/vehicleApi";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import { Divider } from "@mui/material";
import { TextField } from "@mui/material";
import InputAdornment from "@mui/material/InputAdornment";

const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: "80%",
  height: "70%",
  borderRadius: "10px",
  bgcolor: "background.paper",
  boxShadow: 24,
  p: 4,
  pb: 2,
};

const Vehicle = (props) => {
  const { onClick, ...vehicle } = props;
  return (
    <Card
      onClick={() => onClick(vehicle)}
      sx={{ maxWidth: 345, border: "2px solid gray", margin: "10px" }}
    >
      <CardContent>
        <Typography gutterBottom component="div">
          {vehicle.model_name}
        </Typography>
      </CardContent>
    </Card>
  );
};

const AddCard = (props) => {
  const { onClick } = props;
  console.log(onClick);
  return (
    <Card
      sx={{
        maxWidth: 345,
        border: "2px solid gray",
        margin: "10px",
        textAlign: "center",
      }}
      onClick={onClick}
    >
      <CardContent>
        <Typography gutterBottom component="div">
          Add Vehicle
        </Typography>
      </CardContent>
      <AddCircleOutlineIcon
        sx={{ fontSize: 40, marginBottom: "5px", color: "gray" }}
      />
    </Card>
  );
};

const ListInput = (props) => {
  const { inputName, prefix, list, setList } = props;

  const handleChange = (index, event) => {
    const newList = [...list];
    newList[index] = parseFloat(event.target.value) || 0;
    setList(newList);
  };

  const handleAddItem = () => {
    setList([...list, 0]);
  };

  const handleRemoveItem = (index) => {
    const newList = list.filter((_, i) => i !== index);
    setList(newList);
  };

  return (
    <div>
      <Divider sx={{ margin: "15px 15px 0 0", padding: "10px" }}>
        {inputName}
      </Divider>
      <div
        style={{
          width: "100%",
          display: "flex",
          flexWrap: "wrap",
          alignItems: "center",
        }}
      >
        {list.map((item, index) => (
          <Box
            key={index}
            sx={{ marginRight: "5%" }}
            display="flex"
            alignItems="center"
            mb={2}
          >
            <TextField
              type="number"
              label={`${prefix ?? "Axle"} ${index + 1}`}
              value={item}
              onChange={(e) => handleChange(index, e)}
              variant="outlined"
            />
            <Button
              variant="contained"
              color="secondary"
              onClick={() => handleRemoveItem(index)}
              style={{ marginLeft: 8 }}
            >
              Remove
            </Button>
          </Box>
        ))}
        <Button
          variant="contained"
          sx={{ height: "40px" }}
          onClick={handleAddItem}
        >
          Add Item
        </Button>
      </div>
    </div>
  );
};

const VehicleForm = (props) => {
  const { selectedVehicle = null } = props;

  const [vehicleDetails, setVehicleDetails] = useState({});

  const [axleList, setAxleList] = useState(
    selectedVehicle?.axle_weight_ratings
      ? selectedVehicle?.axle_weight_ratings
      : []
  );
  const [axleGroupList, setAxleGroupList] = useState(
    selectedVehicle?.axle_group_weight_ratings
      ? selectedVehicle?.axle_group_weight_ratings
      : []
  );

  useEffect(() => {
    if (selectedVehicle) setVehicleDetails(selectedVehicle);
  }, [selectedVehicle]);

  const handleChange = (e) => {
    e.preventDefault();
    const { name, value } = e.target;
    setVehicleDetails({ ...vehicleDetails, [name]: value });
  };

  const handleSubmitForm = (e) => {
    e.preventDefault();
    const newVehicleDetails = {
      ...vehicleDetails,
      axle_weight_ratings: axleList,
      axle_group_weight_ratings: axleGroupList,
    };
    console.log(newVehicleDetails, "updated");
  };

  const handleVisualize = () => {
    console.log("hello");
    console.log(selectedVehicle.id);
  }

  return (
    <form
      onSubmit={handleSubmitForm}
      style={{ marginTop: "10px", height: "100%" }}
    >
      <div style={{ height: "80%", overflowY: "scroll" }}>
        <TextField
          label="Model Name"
          name="model_name"
          value={vehicleDetails.model_name}
          id="outlined-start-adornment"
          sx={{ m: 1, width: "25ch" }}
          onChange={handleChange}
          required
        />
        <TextField
          label="Destination"
          name="destination"
          value={vehicleDetails.destination}
          id="outlined-start-adornment"
          sx={{ m: 1, width: "25ch" }}
          onChange={handleChange}
          required
        />
        <Divider sx={{ margin: "15px 15px 0 0", padding: "10px" }}>
          Dimensions (in m)
        </Divider>
        <TextField
          label="Length"
          name="length"
          value={vehicleDetails.length}
          id="outlined-start-adornment"
          type="number"
          sx={{ m: 1, width: "25ch" }}
          // min="0"
          InputProps={{
            endAdornment: <InputAdornment position="end">m</InputAdornment>,
          }}
          onChange={handleChange}
          required
        />
        <TextField
          label="Breadth"
          name="breadth"
          value={vehicleDetails.breadth}
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
          value={vehicleDetails.height}
          id="outlined-start-adornment"
          type="number"
          sx={{ m: 1, width: "25ch" }}
          InputProps={{
            endAdornment: <InputAdornment position="end">m</InputAdornment>,
          }}
          onChange={handleChange}
          required
        />
        <Divider sx={{ margin: "15px 15px 0 0", padding: "10px" }}>
          Weight Measurements (in kg)
        </Divider>
        <TextField
          label="Tare Weight"
          name="tare_weight"
          value={vehicleDetails.tare_weight}
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
          label="GVWR"
          name="gvwr"
          value={vehicleDetails.gvwr}
          id="outlined-start-adornment"
          sx={{ m: 1, width: "25ch" }}
          onChange={handleChange}
          required
        />
        <TextField
          label="Wheel Load Capacity"
          name="wheel_load_capacity"
          value={vehicleDetails.wheel_load_capacity}
          sx={{ m: 1, width: "25ch" }}
          type="number"
          onChange={handleChange}
          required
        />
        <ListInput
          prefix="Axle"
          list={axleList}
          setList={setAxleList}
          inputName="Axle Weight Ratings"
        />
        <ListInput
          prefix="Axle Group"
          list={axleGroupList}
          setList={setAxleGroupList}
          inputName="Axle Group Weight Ratings"
        />
      </div>
      <div style={{ display: "flex" }}>
        <Button
          sx={{ margin: "15px 0 0 10px", display: "block" }}
          variant="outlined"
          type="submit"
        >
          {selectedVehicle ? "Update Vehicle" : "Add Vehicle"}
        </Button>
        {selectedVehicle && (
          <Button
            sx={{ margin: "15px 0 0 10px", display: "block" }}
            variant="contained"
            color="success"
            onClick={handleVisualize}
          >
            Visualize
          </Button>
        )}
      </div>
    </form>
  );
};

export default function BasicModal(props) {
  const { open, setOpen } = props;
  const handleClose = () => setOpen(false);
  const [vehicleData, setVehicleData] = useState([]);
  const [vehicleForm, setVehicleForm] = useState(false);
  const [selectedVehicle, setSelectedVehicle] = useState(null);
  useEffect(() => {
    if (open) {
      const fetchVehicleData = async () => {
        try {
          const vehicleData = await vehicleApi.fetchVehicleData();
          console.log(vehicleData, "blablabla");
          setVehicleData(vehicleData);
        } catch (error) {
          console.error("Error fetching vehicle data:", error);
        }
      };
      fetchVehicleData();
    }
  }, [open]);
  const handleAddClick = () => {
    setVehicleForm(true);
  };
  const handleVehicleSelect = (vehicle) => {
    console.log(vehicle, "selected");
    setSelectedVehicle(vehicle);
    setVehicleForm(true);
  };
  return (
    <Modal
      open={open}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
    >
      <Box sx={style}>
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            {vehicleForm && (
              <ArrowBackIcon
                onClick={() => {
                  setVehicleForm(false);
                  setSelectedVehicle(null);
                }}
                sx={{ fontSize: 25, marginRight: 2 }}
              ></ArrowBackIcon>
            )}
            <Typography variant="h6">
              {vehicleForm
                ? selectedVehicle
                  ? selectedVehicle.model_name
                  : "Add Vehicle"
                : "Select Vehicle"}
            </Typography>
          </div>
          <Button onClick={handleClose} variant="outlined" color="error">
            Cancel
          </Button>
        </div>
        {!vehicleForm ? (
          <div style={{ display: "flex", flexWrap: "wrap", marginTop: "15px" }}>
            <AddCard onClick={handleAddClick} />
            {vehicleData.map((vehicle) => {
              return <Vehicle {...vehicle} onClick={handleVehicleSelect} />;
            })}
          </div>
        ) : (
          <VehicleForm selectedVehicle={selectedVehicle} />
        )}
      </Box>
    </Modal>
  );
}
