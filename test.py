import serial

ser = serial.Serial('/dev/ttyACM0', 57600)
loopVar = True

if (ser.isOpen()):
    while (loopVar):
        redVal = input('Red value:')
        ser.write(str("r" + chr(int(redVal))).encode())
        greenVal = input('Green value:')
        ser.write(str("g" + chr(int(greenVal))).encode())
        blueVal = input('Blue value:')
        ser.write(str("b" + chr(int(blueVal))).encode())
        loopCheck = input('Loop (Y/N):')
        if(loopCheck == 'N'):
            loopVar = False
    ser.close()


#ser.write(("r" + "150").encode())
#ser.write(("g" + "50").encode())
#ser.write(("b" + "500").encode())