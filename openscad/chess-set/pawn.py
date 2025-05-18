from solid2 import *

import common
from units import Base, Pawn

def build():
    bottom = common.pawn_base()

    x = Pawn.base_dia * 0.60
    middle1 = cube([x,x,5], center=True)
    middle2 = cylinder(
        d1=Pawn.base_dia*.5,
        d2=Pawn.base_dia*.25,
        h=Pawn.height
    )
    middle = middle1 + middle2

    top = sphere(d=Base.dia/2)

    piece = bottom              + \
            middle.up(Base.thk) + \
            top.up(Base.thk + Pawn.height)

    return piece
