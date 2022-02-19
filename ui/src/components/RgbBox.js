import { rgbToHex } from "@mui/material";

const RgbBox = ({r, g, b}) => {
    return(
        <div style={{backgroundColor: `rgb(${r}, ${g}, ${b})`, height: '500px', width: '500px'}}>

        </div>
    );
}

export default RgbBox