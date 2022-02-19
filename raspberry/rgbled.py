from inspect import CO_ASYNC_GENERATOR
import serial
import time
import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
  
    if rc == 0:
  
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
  
    else:
  
        print("Connection failed")

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    y = json.loads(message.payload)
    print(y["r"])
    print(y["g"])
    print(y["b"])
    ser.write(str("r" + chr(int(y["r"]))).encode())
    ser.write(str("g" + chr(int(y["g"]))).encode())
    ser.write(str("b" + chr(int(y["b"]))).encode())
    #r.write(y["r"])
    #g.write(y["g"])
    #b.write(y["b"])
    

#Arduino
#board = pyfirmata.Arduino('/dev/ttyACM0')
#it = pyfirmata.util.Iterator(board)
#it.start()

#r = board.get_pin('d:3:p')
#g = board.get_pin('d:5:p')
#b = board.get_pin('d:6:p')

ser = serial.Serial('/dev/ttyACM0', 57600)

#MQTT
Connected = False
BROKER_ADDRESS = "localhost"
client = mqtt.Client("Arduino Client")
client.on_connect= on_connect
client.on_message= on_message
client.connect(BROKER_ADDRESS) #connect to broker
client.loop_start()

while Connected != True:    #Wait for connection
    time.sleep(0.1)
  
client.subscribe("arduino/rgb")
  
try:
    while True:
        if(ser.readline().decode()):
            message = ser.readline().decode().partition("#")
            jsonMessage = {
                "humidity": message[0], 
                "celcius": message[2].rstrip()
            }
            client.publish("arduino/temp", json.dumps(jsonMessage))
            print(json.dumps(jsonMessage))
        #print(str(ser.readline().decode())) #b'21.00#25.60\r\n'
        time.sleep(1)
  
except KeyboardInterrupt:
    print("exiting")
    ser.close()
    client.disconnect()
    client.loop_stop()


# while True:
#     r.write(brightness1a)
#     g.write(brightness1b)
#     time.sleep(1)
#     r.write(dunkel)
#     g.write(dunkel)
#     g.write(brightness1b)
#     time.sleep(1)
#     g.write(dunkel)
#     b.write(brightness1c)
#     time.sleep(1)
#     b.write(dunkel)
