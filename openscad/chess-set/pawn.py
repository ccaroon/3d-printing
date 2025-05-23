from solid2 import *

import common
from units import Base, Pawn


def __build_top():
    pom_dia = Pawn.base_dia * 0.50
    pom = sphere(d=pom_dia).up(pom_dia / 2)

    lip0 = sphere(d=2.0)
    lip1 = cylinder(d=pom_dia, h=0.5)
    lip = minkowski()(lip0, lip1)

    return pom + lip


def __build_middle():

    center = cylinder(
        _fn=10,
        d1=Pawn.base_dia * 0.71,
        d2=Pawn.base_dia * 0.33,
        h=Pawn.height
    )

    part = center

    return part


def build():
    bottom = common.pawn_base()
    middle = __build_middle()
    top = __build_top()

    piece = bottom              + \
            middle.up(Base.thk) + \
            top.up(Base.thk + Pawn.height)
    # piece = top

    return piece
