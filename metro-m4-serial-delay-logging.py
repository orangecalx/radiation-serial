
# ---- brandon's geiger interval logger -----

# in a nutshell, a metro m4 takes pulses from a mightyohm geiger counter, measures the delay between pulses,
# and records it to "delays.txt" on the metro's memory. this results in a truly random dataset.


# pinout (geiger - metro)

# pulse pin 1 (bottom) - 3.3v
# pulse pin 3 (top) - GND (analog side)
# pulse pin 2 (or off pin 16 on ATTiny) - A0

# bridge D2 and GND for write mode (needed to access internal flash)

import time
import board
import digitalio
from analogio import AnalogIn

led = digitalio.DigitalInOut(board.LED)     # gonna switch this to the onboard neopixel eventually
led.switch_to_output()

geiger = AnalogIn(board.A0)

def get_voltage(pin):
    return (pin.value * 3.3) / 65536        # this maps the analogIn reading to a 3.3v range


pulse = geiger.value
timr = 0
eltimr = 0


try:
    with open("/delays.txt", "a") as fp:
        while True:
            if get_voltage(geiger) > 2.0:   # if the signal goes above 2v
                timr = time.time()          # grab you a time
                print("\nPULSE")

                print("delay: ", eltimr)
                fp.write('{0:f}\n'.format(eltimr))
                fp.flush()
                time.sleep(0.01)
            else:
                eltimr = time.time() - timr # otherwise, between pulses where there isn't signal, find the
                time.sleep(0.01)            # difference between the two times as an integer

except OSError as e:                        # slowly blink LED to indicate "standby / not-logging" mode
    delay = 0.5
    if e.args[0] == 28:                     # blink it twice as fast if there's no space left
        delay = 0.25
    while True:
        led.value = not led.value
        time.sleep(delay)

