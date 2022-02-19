// DHT11
#include "DHT.h"
#define DHTPIN 2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);

// RGB
int colorRGB[3];
int redPin = 3;
int greenPin = 5;
int bluePin = 6;
int r=0, g=0, b=0;

void setup() {
  
  Serial.begin(57600); 
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  
  dht.begin();
}

void loop() {
  
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  Serial.print(h);
  Serial.print(F("#"));
  Serial.println(t);
  
  if(Serial.available() >= 2){
    
    switch( byte( Serial.read() )) {
      case 'r':
        colorRGB[0] = Serial.read();
        break;
      case 'g':
        colorRGB[1] = Serial.read();
        break;   
      case 'b':
        colorRGB[2] = Serial.read();
        break;
      case 'c':
        Serial.flush();
        break;
      }
   }
   analogWrite(redPin, colorRGB[0]); 
   analogWrite(greenPin, colorRGB[1]);
   analogWrite(bluePin, colorRGB[2]);
   delay(2000);
}
