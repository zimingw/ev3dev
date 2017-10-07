#!/usr/bin/env python3
from ev3dev.ev3 import *

Leds.set(Leds.LEFT, brightness_pct=0.5, trigger='timer')
Leds.set(Leds.LEFT, delay_on=3000, delay_off=500)
Leds.set_color(Leds.LEFT, Leds.GREEN)
# TODO: Add code here
