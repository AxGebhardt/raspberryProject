import React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Slider from '@mui/material/Slider';
import MuiInput from '@mui/material/Input';
import SquareIcon from '@mui/icons-material/Square';

const Input = styled(MuiInput)`
  width: 42px;
`;

const RgbSlider = ({colorname, color, valueCallback, value}) => {
    //const [value, setValue] = React.useState(30);

    const handleSliderChange = (event, newValue) => {
      //setValue(newValue);
      console.log("NewValue:", newValue);
      valueCallback(newValue);
    };
  
    const handleInputChange = (event) => {
      valueCallback(event.target.value === '' ? '' : Number(event.target.value));
    };
  
    const handleBlur = () => {
      if (value < 0) {
        valueCallback(0);
      } else if (value > 255) {
        valueCallback(255);
      }
    };
    
    console.log("value:", value);
    return (
      <Box sx={{ width: 400 }}>
        <Grid container spacing={2} alignItems="center">
          <Grid item>
            <SquareIcon sx={{ color: color }}/>
          </Grid>
          <Grid item xs>
            <Slider
              value={typeof value === 'number' ? value : 0}
              onChange={handleSliderChange}
              aria-labelledby="input-slider"
              step = {1}
              min = {0}
              max = {255}
            />
          </Grid>
          <Grid item>
            <Input
              value={value}
              sx = {{color: "white"}}
              size="medium"
              onChange={handleInputChange}
              onBlur={handleBlur}
              inputProps={{
                step: 10,
                min: 0,
                max: 255,
                type: 'number',
                'aria-labelledby': 'input-slider',
              }}
            />
          </Grid>
        </Grid>
      </Box>
    );
}

export default RgbSlider