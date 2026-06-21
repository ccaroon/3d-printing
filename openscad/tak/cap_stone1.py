from solid2 import *

from units import CapStone

import math
from solid2 import *

from units import CapStone


def __build_bottom(style):
    bottom = cylinder(d=CapStone.base_dia, h=CapStone.base_h)

    return bottom


def __build_top(style):
    sides = 8
    if style == "s2":
        sides = 6

    top = sphere(d=CapStone.top_dia, _fn=sides)

    return top


def __build_middle(style):
    sides = 8
    if style == "s2":
        sides = 6

    center = cylinder(
        d1=CapStone.base_dia,
        d2=CapStone.base_dia * 0.50,
        h=CapStone.mid_height,
        _fn=sides,
    )

    part = center

    return part


def build(opts):
    style = opts.get("style", "s1")
    bottom = __build_bottom(style=style)
    middle = __build_middle(style=style)
    top = __build_top(style=style)

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
