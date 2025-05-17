from solid2 import *

import common
from units import base, pawn

def build():
    bottom = common.pawn_base()

    x = pawn.base_dia * 0.60
    middle1 = cube([x,x,5], center=True)
    middle2 = cylinder(
        d1=pawn.base_dia*.5,
        d2=pawn.base_dia*.25,
        h=pawn.height
    )
    middle = middle1 + middle2

    top = sphere(d=base.dia/2)

    piece = bottom              + \
            middle.up(base.thk) + \
            top.up(base.thk + pawn.height)

    return piece
