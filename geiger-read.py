import serial
import time
import random
ser = serial.Serial('COM8', 9600) # be sure to change this if running on Debian





while True:
    r = random.randint(1,2)
    ser.write(b"piss")
    time.sleep(1)