from solid2 import *

from units import CapStone

import math
from solid2 import *

from units import CapStone


def __build_bottom():
    bottom = cylinder(d=CapStone.base_dia, h=CapStone.base_h)

    return bottom


def __build_top():
    top = sphere(d=CapStone.top_dia)

    return top


def __build_middle():
    center = cylinder(
        d1=CapStone.base_dia,
        d2=CapStone.base_dia * 0.50,
        h=CapStone.mid_height,
    )

    part = center

    return part


def build(opts):
    bottom = __build_bottom()
    middle = __build_middle()
    top = __build_top()

    piece = (
        bottom
        + middle.up(CapStone.base_h)
        + top.up(
            CapStone.base_h
            + CapStone.mid_height
            + (CapStone.top_dia / 2)
            - CapStone.top_dia * 0.25
        )
    )

    return piece
