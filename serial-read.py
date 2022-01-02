import serial

ser = serial.Serial('/dev/ttyUSB0')

out = ser.readline()

