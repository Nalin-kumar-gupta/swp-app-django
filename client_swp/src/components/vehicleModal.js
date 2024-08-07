import * as React from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import Modal from "@mui/material/Modal";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';

const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: "80%",
  height: "500px",
  borderRadius: "10px",
  bgcolor: "background.paper",
  boxShadow: 24,
  p: 4,
};

const Vehicle = (props) => {
  const { name, type } = props;
  return (
    <Card sx={{ maxWidth: 345, border: "2px solid gray", margin: "10px" }}>
      <CardContent>
        <Typography gutterBottom component="div">
          {name}
        </Typography>
        <Typography gutterBottom variant="h8" component="div">
          {type}
        </Typography>
      </CardContent>
    </Card>
  );
};

const AddCard = () => {
  return (
    <Card sx={{ maxWidth: 345, border: "2px solid gray", margin: "10px", textAlign:"center" }}>
      <CardContent>
        <Typography gutterBottom component="div">
          Add Vehicle
        </Typography>
      </CardContent>
      <AddCircleOutlineIcon sx={{ fontSize: 40, marginBottom: "5px", color:"gray" }}/>
    </Card>
  );
};

export default function BasicModal(props) {
  const { open, setOpen } = props;
  const handleClose = () => setOpen(false);
  const vehicleData = [
    { name: "Mahindra", type: "Truck" },
    { name: "Mahindra", type: "Truck" },
    { name: "Mahindra", type: "Truck" },
    { name: "Mahindra", type: "Truck" },
    { name: "Mahindra", type: "Truck" },
    { name: "Mahindra", type: "Truck" },
  ];
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
          <Typography variant="h6">Select Vehicle</Typography>
          <Button onClick={handleClose} variant="outlined" color="error">
            Cancel
          </Button>
        </div>
        <div style={{ display: "flex", flexWrap: "wrap", marginTop: "15px" }}>
          <AddCard />
          {vehicleData.map((vehicle) => {
            return <Vehicle {...vehicle} />;
          })}
        </div>
      </Box>
    </Modal>
  );
}
