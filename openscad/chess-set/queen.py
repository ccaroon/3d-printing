from solid2 import *

import common
from units import Crown, Queen

def crown():
    c1 = circle(d=Crown.base_thk)
    left_shift = Crown.base_dia + .5
    bottom = c1.left(left_shift).rotate_extrude(angle=360)

    mid_outer = cylinder(
        d1=Crown.dia1,
        d2=Crown.dia2,
        h=Crown.height,
        _fn=15
    )
    mid_inner = circle(d=8).left(8.5).rotate_extrude(angle=360).up(10.5)

    middle = mid_outer - mid_inner

    top = sphere(d=Crown.dome_dia)
    top_offset = (Crown.dome_dia / 2) + (Crown.height * 0.25)
    pom = sphere(d=Queen.pom_dia)
    pom_offset = top_offset + Crown.dome_dia / 2

    return bottom.up(0.25) + middle + top.up(top_offset) + pom.up(pom_offset)
    # return bottom.up(0.25)


def build():
    top = crown()

    queen_prf = import_dxf("./images/queen/Queen-Profile.dxf")
    middle_part = queen_prf.rotate_extrude(angle=360, _fn=250)

    bottom = common.court_base()

    piece =  bottom + middle_part.up(Queen.base_thk) + top.up(Queen.base_thk + Queen.height)

    # block = cube([40,40,Queen.height * 1.00]).down(2).left(20).back(20)
    # return piece - block

    return piece
