import logo from './logo.svg';
import './App.css';
import '@fontsource/roboto';
import RgbSlider from './components/RgbSlider';
import RgbBox from './components/RgbBox';
import { Button } from '@mui/material';
import axios from 'axios';
import React, { useState } from 'react';

const  App = () => {
  
  const [r, setR] = useState(30);
  const [g, setG] = useState(30);
  const [b, setB] = useState(30);

  const onClick = () => {
    axios.post(`http://192.168.0.2:5000/mqtt/rgb`, {r, g, b}).then(res => {
      console.log(res);
      console.log(res.data)
    })
  }

  const handleR = (childData) => {
    setR(childData)
  }

  const handleG = (childData) => {
    setG(childData)
  }

  const handleB = (childData) => {
    setB(childData)
  }

  return (
      <div className="App">
        <RgbSlider colorname="Red" color="red" valueCallback={handleR} value={r}/>
        <RgbSlider colorname="Green" color="green"  valueCallback={handleG} value={g}/>
        <RgbSlider colorname="Blue" color="blue"  valueCallback={handleB} value={b}/>
        <RgbBox r={r} g={g} b={b}/>
        <Button onClick={onClick}>Submit</Button>

      </div>
  );
}

export default App;
