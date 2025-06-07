#!/usr/bin/env python
from solid2 import *
import lib.units as units

def square1():
    """ Cube: 1.5in x 1.5in """
    return cube([1.5 * units.inch, 1.5 * units.inch, 1 * units.mm])

def circle1():
    """ Circle: 1.5in x 1mm """
    return cylinder(d=1.5 * units.inch, h=1 * units.mm)


def ruler18x3():
    """ Ruler 1/8in by 3in """
    return cube([3 * units.inch, 0.125 * units.inch, 2 * units.mm])


MODELS = {
    "square1": square1,
    "circle1": circle1,
    "ruler18x3": ruler18x3
}

def build(model):
    set_global_fn(150)

    builder = MODELS.get(model)
    if builder:
        obj = builder()

        filename = f"./models/tool-{model}.scad"
        obj.save_as_scad(filename)
        print(f"==> Saved: {filename}")
    else:
        print(f"==> Tools: Unknown model '{model}'")
        print(f"Available Models: {list(MODELS.keys())}")
