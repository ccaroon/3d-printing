#!/usr/bin/env python
from solid2 import *

from lib import units

CAP_DIA = 7.75 * units.mm
CAP_HOLE_DIA = 6.75 * units.mm
CAP_HEIGHT = 1.25 * units.cm

def mech_pencil_cap():
    cap = cylinder(d=CAP_DIA, h=CAP_HEIGHT)
    hole = cylinder(d=CAP_HOLE_DIA, h=CAP_HEIGHT)

    return cap - hole.up(2 * units.mm)


if __name__ == "__main__":
    set_global_fn(150)
    cap = mech_pencil_cap()
    cap.save_as_scad("./models/mech_pencil_cap.scad")
