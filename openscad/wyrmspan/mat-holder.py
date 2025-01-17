#!/usr/bin/env python
from solid2 import *

from lib import units

RING_THICKNESS = 2.00*units.mm
RING_INNER_DIA = 4.50*units.cm
RING_OUTER_DIA = RING_INNER_DIA + RING_THICKNESS
RING_HGT = 3.00*units.cm


def mat_holder():
    """
    Ring to hold rolled up rubber mats.
    """
    outer = cylinder(d=RING_OUTER_DIA, h=RING_HGT)
    inner = cylinder(d=RING_INNER_DIA, h=RING_HGT + 5)

    holder = outer - inner.down(2.5)

    return holder


if __name__ == "__main__":
    set_global_fn(150)
    holder = mat_holder()
    holder.save_as_scad("./models/mat-holder.scad")
