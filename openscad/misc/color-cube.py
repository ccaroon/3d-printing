#!/usr/bin/env python
# from solid2 import *

from lib import units
from lib import things


cube_size = 1 * units.inch
model = things.hollow_cube(cube_size, 1)

# item = art
model.save_as_scad("./models/color-cube.scad")
