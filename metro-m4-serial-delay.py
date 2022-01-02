# little flickering candle thing, but with the neopixel

import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn



geiger = AnalogIn(board.A0)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536



led = neopixel.NeoPixel(board.NEOPIXEL, 1)
pulse = geiger.value
timr = 0
eltimr = 0

while True:

   if get_voltage(geiger) > 2.0:


       timr = time.monotonic()
       print("\nPULSE")
       print("delay: ", round(eltimr, 2))
       time.sleep(0.01)



   else:
       eltimr = time.monotonic() - timr
       time.sleep(0.01)





# todo

# - figure out how to store eltimr var





# Write your code here :-)
