#!/usr/bin/env python3
from ev3dev.ev3 import *

# Connect infrared and touch sensors to any sensor ports
# and check they are connected.

ir = InfraredSensor()
btn = Button();
mA = MediumMotor('outA')
cs = ColorSensor()
assert ir.connected, "Connect a single infrared sensor to any sensor port"
assert cs.connected, "Connect a color sensor to any sensor port"

# Put the infrared sensor into proximity mode.
ir.mode = 'IR-PROX'

while True:    # Stop program by pressing touch sensor button
    # Infrared sensor in proximity mode will measure distance to the closest
    # object in front of it.
    if btn.any():
        Sound.beep().wait()  # Wait for the beep to finish.
        #make sure left led is green before exiting
        Leds.set_color(Leds.LEFT, Leds.GREEN)
        mA.stop(stop_action="coast")
        exit()  # Stop the program.

    distance = ir.value()
    color = cs.value()
    print("Color=" + str(color))

    if distance < 25:
        Leds.set_color(Leds.LEFT, Leds.RED)
        mA.run_forever(speed_sp=-200)
    else:
        Leds.set_color(Leds.LEFT, Leds.GREEN)
        mA.stop(stop_action="coast")



