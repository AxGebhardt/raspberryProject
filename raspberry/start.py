import serial
import json
import time
import paho.mqtt.client as mqtt

BROKER_ADDRESS = "localhost"

arduino = serial.Serial("/dev/ttyACM0", 9600)
client = mqtt.Client("P1")
client.connect(BROKER_ADDRESS) #connect to broker


while True:
    temp = str(arduino.readline())
    print(temp)
    client.publish("Temperatur", temp)#publish
    time.sleep(10)

time.sleep(1)
