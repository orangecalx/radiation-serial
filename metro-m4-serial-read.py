# little flickering candle thing, but with the neopixel

import time
import board
import busio
import neopixel
import digitalio

ser = busio.UART(board.TX, board.RX, baudrate=9600)
led = neopixel.NeoPixel(board.NEOPIXEL, 1)



while True:
   dat = ser.read(64)

   if dat is not None:
       datastr = ''.join([chr(b) for b in dat])
       print(datastr)


