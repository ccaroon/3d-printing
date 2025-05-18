from solid2 import *

import common
from units import Crown, Middle, Queen

# TODO: Shorten. Less forehead.

def crown():
    c1 = circle(d=Crown.base_thk)
    bottom = c1.left(Crown.base_dia).rotate_extrude(angle=360)

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

    return bottom + middle + top.up(top_offset) + pom.up(pom_offset)


def build():
    top = crown()

    queen_prf = import_dxf("./images/queen/Queen-Profile.dxf")
    middle_part = queen_prf.rotate_extrude(angle=360, _fn=250)

    bottom = common.court_base()

    piece =  bottom + middle_part.up(Queen.base_thk) + top.up(Middle.height+2)

    return piece
