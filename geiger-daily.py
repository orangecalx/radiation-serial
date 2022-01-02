import serial
import csv
from datetime import date

ser = serial.Serial('/dev/ttyUSB0', 9600) 
ser.xonxoff=1
ser.isOpen()


ser_bytes = ser.readline() # make sure this is after the above while loop, otherwise it repeats last read value
decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("ascii"))
out = decoded_bytes.split(",")
map(float,out)

print(out[5])

with open('usvmin.csv', mode='a') as csvout:
	now = date.today()

	csvwrite = csv.writer(csvout)
	
	csvwrite.writerow([now, out[5] + " usv/hr"])

