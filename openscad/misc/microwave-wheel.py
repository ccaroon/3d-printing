#!/usr/bin/env python

"""
NOTE:
PLA is apparently NOT microwave safe. :(
"""

from solid2 import *

from lib import units

WHEEL_H = 7.9 * units.mm
WHEEL_DIA = 14.9 * units.mm
WHEEL_HOLE_DIA = 7.5 * units.mm

WHEEL_HUB_H = 2 * units.mm
WHEEL_HUB_DIA = 10.5 * units.mm

def microwave_wheel():
    wheel = cylinder(d=WHEEL_DIA, h=WHEEL_H)
    hub = cylinder(d=WHEEL_HUB_DIA, h=WHEEL_HUB_H+1)
    hole = cylinder(d=WHEEL_HOLE_DIA, h=WHEEL_H + 5)

    return wheel - hub.up(WHEEL_H-WHEEL_HUB_H) - hole.down(2.5)


if __name__ == "__main__":
    set_global_fn(150)
    drain_plug = microwave_wheel()
    drain_plug.save_as_scad("./models/microwave-wheel.scad")
