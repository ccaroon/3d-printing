#!/usr/bin/env python
from solid2 import *

from lib import things, units

if __name__ == "__main__":
    set_global_fn(150)
    die = things.blank_die(1 * units.inch)
    die.save_as_scad("./models/blank_die.scad")
