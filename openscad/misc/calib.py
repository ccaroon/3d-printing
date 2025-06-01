#!/usr/bin/env python
from solid2 import *
import lib.units as units

def square1():
    """ Cube: 1.5in x 1.5in """
    return cube([1.5 * units.inch, 1.5 * units.inch, 1 * units.mm])

def circle1():
    return cylinder(d=1.5 * units.inch, h=1 * units.mm)


MODELS = {
    "square1": square1,
    "circle1": circle1
}

def build(model):
    set_global_fn(150)

    builder = MODELS.get(model)
    if builder:
        obj = builder()

        filename = f"./models/calib-{model}.scad"
        obj.save_as_scad(filename)
        print(f"==> Saved: {filename}")
    else:
        print(f"==> Calib: Unknown model '{model}'")
        print(f"Available Models: {list(MODELS.keys())}")
