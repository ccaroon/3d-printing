from solid2 import *

from units import court, pawn, magnet

def pawn_base():
    bottom = cylinder(d=pawn.base_dia, h=pawn.base_thk)
    cut_out = cylinder(d=magnet.dia, h=magnet.thk + 1)

    return bottom - cut_out.down(1)


def court_base():
    bottom = cylinder(d=court.base_dia, h=court.base_thk)
    cut_out = cylinder(d=magnet.dia, h=magnet.thk + 1)

    return bottom - cut_out.down(1)


def build():
    model = court_base()
    # model = pawn_base()

    return model
