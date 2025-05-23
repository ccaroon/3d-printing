from solid2 import *

import common
from units import Knight


def __build_top():
    # TODO: just stub
    return sphere(d=Knight.base_dia * 0.75)


def __build_middle():
    torso = circle(d=Knight.base_dia, _fn=5).linear_extrude(
        height=Knight.height * 0.50,
        twist=90,
        scale=[1, 1.5],
    )
    part = torso.rotate(0,0,180)

    return part


def build():
    bottom = common.court_base()
    middle = __build_middle()
    top = __build_top()

    piece = bottom              + \
            middle.up(Knight.base_thk) + \
            top.up(Knight.base_thk + Knight.height)
    # piece = top

    return piece
