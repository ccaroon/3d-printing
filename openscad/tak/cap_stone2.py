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


# def __build_top():
#     pom_dia = CapStone.
#     pom = sphere(d=pom_dia).up(pom_dia / 2)

#     lip0 = sphere(d=1.5)
#     lip1 = cylinder(d=pom_dia, h=0.5)
#     lip = minkowski()(lip0, lip1)

#     collar_h = 2
#     cd1 = Pawn.base_dia * 0.33
#     cd2 = pom_dia
#     collar = cylinder(
#         d1=cd1,
#         d2=cd2,
#         h=collar_h
#     )

#     a = (cd1, 0)
#     b = (cd2, collar_h)
#     angle = math.atan2(b[1] - a[1], b[0] - a[0])
#     print(angle * 180/math.pi)

#     return collar + lip.up(2.75) + pom.up(2.5)
#     # return collar + lip.up(2.75)


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
