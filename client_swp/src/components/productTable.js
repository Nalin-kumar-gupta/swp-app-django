import * as React from "react";
import { styled } from "@mui/material/styles";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell, { tableCellClasses } from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    fontWeight: "bold",
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 14,
  },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  "&:nth-of-type(odd)": {
    backgroundColor: theme.palette.action.hover,
  },
  // hide last border
  "&:last-child td, &:last-child th": {
    border: 0,
  },
}));

export default function CustomizedTables(props) {
  const { productData = [] } = props;
  return (
    <TableContainer sx={{ maxHeight: "calc(100vh - 70px)" }} component={Paper}>
      <Table stickyHeader sx={{ minWidth: 700 }} aria-label="sticky table">
        <TableHead>
          <TableRow>
            <StyledTableCell align="center">Length (m)</StyledTableCell>
            <StyledTableCell align="center">Breadth (m)</StyledTableCell>
            <StyledTableCell align="center">Height (m)</StyledTableCell>
            <StyledTableCell align="center">Weight (kg)</StyledTableCell>
            <StyledTableCell align="center">Destination</StyledTableCell>
            <StyledTableCell align="center">Status</StyledTableCell>
            <StyledTableCell align="center">Deliver Date</StyledTableCell>
            <StyledTableCell align="center">Allocation</StyledTableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {productData?.map((row, ind) => (
            <StyledTableRow key={ind}>
              <StyledTableCell align="center">{row.length}</StyledTableCell>
              <StyledTableCell align="center">{row.breadth}</StyledTableCell>
              <StyledTableCell align="center">{row.height}</StyledTableCell>
              <StyledTableCell align="center">{row.weight}</StyledTableCell>
              <StyledTableCell align="center">
                {row.destination}
              </StyledTableCell>
              <StyledTableCell align="center">
                {row.status}
              </StyledTableCell>
              <StyledTableCell align="center">
                {row.deliver_date}
              </StyledTableCell>
              <StyledTableCell align="center">
                {row.allocation}
              </StyledTableCell>
            </StyledTableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
