from solid2 import *

import common
from units import king, middle

# ------------------------------------------------------------------------------
# TODO:
# [ ] NO cross - small cube instead?
# ------------------------------------------------------------------------------

def cross():
    size = 2.75
    v_height = 11
    h_len = 9
    v_bar = cube([size,size,v_height]).left(size/2).back(size/2)
    h_bar = cube([h_len,size,size]).left(h_len/2).back(size/2).up(v_height*0.5)

    return v_bar + h_bar


def crown():
    c1 = circle(d=king.crown_base_thk)
    bottom = c1.left(king.crown_base_dia).rotate_extrude(angle=360)

    mid_outer = cylinder(
        d1=king.crown_dia1,
        d2=king.crown_dia2,
        h=king.crown_height,
        _fn=5
    )
    mid_inset = circle(d=8).left(8.5).rotate_extrude(angle=360).up(10.5)

    middle = mid_outer - mid_inset

    top = sphere(d=king.crown_dome_dia)
    top_offset = (king.crown_dome_dia / 2) + (king.crown_height * 0.25)

    pom = cross()
    pom_offset = king.crown_height * 1.20

    return bottom + middle + top.up(top_offset) + pom.up(pom_offset)


def build():
    top = crown()

    king_prf = import_dxf("./images/king/King-Profile.dxf")
    middle_part = king_prf.rotate_extrude(angle=360, _fn=250)

    bottom = common.court_base()

    piece = bottom + middle_part.up(king.base_thk) + top.up(middle.height - 1)

    return piece
