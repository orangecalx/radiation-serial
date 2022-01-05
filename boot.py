## boot.py file for adafruit metro M4 express (or any circuitpython device?) for radiation-serial 

import board
import digitalio
import storage


switch = digitalio.DigitalInOut(board.D2)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

storage.remount("/", switch.value)
