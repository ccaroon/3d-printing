#!/usr/bin/env python
import random
from solid2 import *

from lib import units

# TODO:
# * [ ] Back too thin
# * [ ] remove centering and lay flat on back
def twig_rack1():
    """
    Half-pipe style
    """
    cutout = cylinder(d=7.90*units.cm, h=30*units.mm, center=True).rotate([90,0,0])
    box = cube([8*units.cm, 25*units.mm, 4*units.cm], center=True)

    # return cutout
    return box - cutout.translate([0,-3,20])


LOG_DIA = 8 * units.mm
LOG_LEN = 22 * units.mm
TOUCH_DIFF = 0.5 * units.mm
def twig_rack2():
    """
    Built from logs

    Bottom: 8 logs
    Sides: 5 logs
    Inner Corner: 1 log

    O                 O <-- top
    O                 O
    O O             O O
    O O O         O O O
    O O O O O O O O O O <-- bottom
    """

    layers = []

    # layer 0 - bottom
    layer = twig()
    for idx in range(1, 10):
        layer += twig().right(idx * (LOG_DIA - TOUCH_DIFF))
    layers.append(layer)

    # layer 1
    layer = twig()
    for idx in (1,2,7,8,9):
        layer += twig().right(idx * (LOG_DIA - TOUCH_DIFF))
    layers.append(layer)

    # layer 2
    layer = twig()
    for idx in (1,8,9):
        layer += twig().right(idx * (LOG_DIA - TOUCH_DIFF))
    layers.append(layer)

    # layer 3
    layer = twig()
    layer += twig().right(9 * (LOG_DIA - TOUCH_DIFF))
    layers.append(layer)

    # layer 4 - top
    layer = twig()
    layer += twig().right(9 * (LOG_DIA - TOUCH_DIFF))
    layers.append(layer)

    # build rack
    rack = layers.pop(0)
    for idx, layer in enumerate(layers):
        rack += layer.forward((LOG_DIA - TOUCH_DIFF) * (idx + 1))

    return rack


def plain_twig():
    return cylinder(d=LOG_DIA, h=LOG_LEN+4)


def twig(rr=True):
    """
    A Single Twig

    Args:
        rr (bool): Random Rotation (sorta)
    """
    rotation = {
        # ANGLE: TRANSLATION
        0:   [0, 0, 0],
        45:  [4.5, -2.5, 0],
        90:  [8.6, 0, 0],
        135: [10.39, 4.5 ,0],
        180: [8.8, 8.6, 0],
        225: [4.5, 10.39, 0],
        270: [0, 8.8, 0],
        315: [-2.5, 4.4, 0]
    }

    twig = import_(file="../resources/twig.svg").linear_extrude(
        # center=True,
        height=LOG_LEN+4
    )

    if rr:
        angle = random.choice(list(rotation.keys()))
        xlate = rotation[angle]
        twig = twig.rotate(angle).translate(xlate)

    return twig


if __name__ == "__main__":
    set_global_fn(150)
    # model = twig_rack1()
    model = twig_rack2()
    # model = twig(True)
    model.save_as_scad("./models/twig_rack.scad")







#
