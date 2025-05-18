from solid2 import *

from units import Court, Pawn, Magnet

def pawn_base():
    bottom = cylinder(d=Pawn.base_dia, h=Pawn.base_thk)
    cut_out = cylinder(d=Magnet.dia, h=Magnet.thk + 1)

    return bottom - cut_out.down(1)


def court_base():
    bottom = cylinder(d=Court.base_dia, h=Court.base_thk)
    cut_out = cylinder(d=Magnet.dia, h=Magnet.thk + 1)

    return bottom - cut_out.down(1)


def build():
    model = court_base()
    # model = pawn_base()

    return model
