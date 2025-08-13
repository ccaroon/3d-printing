#!/usr/bin/env python
from solid2 import *
import lib.units as units


def square1():
    """ Cube: 1.5in x 1.5in """
    return cube([1.5 * units.inch, 1.5 * units.inch, 1 * units.mm])


def circle1():
    """ Circle: 1.5in x 1mm """
    return cylinder(d=1.5 * units.inch, h=1 * units.mm)


def barrel():
    """ Cylinder to help test Z-Seam modes """
    return cylinder(d=1.5 * units.cm, h=2.0 * units.cm)


def rod():
    """ Long Cylinder to help test Z-Seam modes """
    return cylinder(d=1.0 * units.cm, h=5.0 * units.cm)

def small_rect():
    return cube([0.75 * units.cm, 2.0 * units.cm, 0.5 * units.cm])

def star():
    """
    Large star shop for testing printing on varios parts of the build plate
    """
    center = cylinder(d=2.0 * units.cm, h=1.0 * units.mm, center=True)
    arm = cube([10.0*units.cm, .5*units.cm, 1.0*units.mm], center=True)

    arms = arm
    for count in range(1,4):
        arms += arm.rotateZ(count * 45)

    return center + arms


MODELS = {
    "square1": square1,
    "circle1": circle1,
    "barrel": barrel,
    "rod": rod,
    "star": star,
    "small_rect": small_rect
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
