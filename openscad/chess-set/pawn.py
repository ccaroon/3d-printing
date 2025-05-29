import math
from solid2 import *

import common
from units import Pawn


def __build_top():
    pom_dia = Pawn.base_dia * 0.50
    pom = sphere(d=pom_dia).up(pom_dia / 2)

    lip0 = sphere(d=1.5)
    lip1 = cylinder(d=pom_dia, h=0.5)
    lip = minkowski()(lip0, lip1)

    collar_h = 2
    cd1 = Pawn.base_dia * 0.33
    cd2 = pom_dia
    collar = cylinder(
        d1=cd1,
        d2=cd2,
        h=collar_h
    )

    a = (cd1, 0)
    b = (cd2, collar_h)
    angle = math.atan2(b[1] - a[1], b[0] - a[0])
    print(angle * 180/math.pi)

    return collar + lip.up(2.75) + pom.up(2.5)
    # return collar + lip.up(2.75)


def __build_middle():
    center = cylinder(
        _fn=10,
        d1=Pawn.base_dia * 0.71,
        d2=Pawn.base_dia * 0.33,
        h=Pawn.height
    )

    part = center

    return part


def __test_build():
    height = 5
    middle = cylinder(
        _fn=10,
        d1=Pawn.base_dia * 0.71,
        d2=Pawn.base_dia * 0.33,
        h=height
    )
    top = __build_top()

    piece = middle + top.up(height)

    return piece


def __full_build():
    bottom = common.pawn_base()
    middle = __build_middle()
    top = __build_top()

    piece = (
        bottom +
        middle.up(Pawn.base_thk) +
        top.up(Pawn.base_thk + Pawn.height)
    )

    return piece


def build():
    return __full_build()
    # return __test_build()
