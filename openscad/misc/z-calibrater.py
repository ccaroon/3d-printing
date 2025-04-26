#!/usr/bin/env python
from solid2 import *

from lib import units

WIDTH = 1 * units.cm
HEIGHT = 1 * units.mm
LENGTH = 12 * units.cm

def z_calibrater():
    object = cube([WIDTH, LENGTH, HEIGHT])
    return object


if __name__ == "__main__":
    set_global_fn(150)
    cap = z_calibrater()
    cap.save_as_scad("./models/z-calibrater.scad")
