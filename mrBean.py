#!/usr/bin/env python3
from ev3dev.ev3 import *

# Connect infrared and touch sensors to any sensor ports
# and check they are connected.

ir = InfraredSensor()
btn = Button()
mA = MediumMotor('outA')
cs = ColorSensor()
assert ir.connected, "Connect a single infrared sensor to any sensor port"
assert cs.connected, "Connect a color sensor to any sensor port"

# Put the infrared sensor into proximity mode.
ir.mode = 'IR-PROX'
cs.mode = 'COL-COLOR'

colors = ('unknown', 'black', 'blue', 'green', 'yellow', 'red', 'white', 'brown')
color = -1

while True:  # Stop program by pressing touch sensor button
    # Infrared sensor in proximity mode will measure distance to the closest
    # object in front of it.
    if btn.any():
        Sound.beep().wait()  # Wait for the beep to finish.
        # make sure left led is green before exiting
        Leds.set_color(Leds.LEFT, Leds.GREEN)
        mA.stop(stop_action="coast")
        exit()  # Stop the program.

    distance = ir.value()

    if distance < 25:
        Leds.set_color(Leds.LEFT, Leds.RED)
        mA.run_forever(speed_sp=-200)
        newColor = cs.value()
        if color != newColor:
            print("Color=" + colors[newColor])
            Sound.speak(colors[newColor]).wait()
            color = newColor
    else:
        Leds.set_color(Leds.LEFT, Leds.GREEN)
        mA.stop(stop_action="coast")
