from solid2 import *

from units import CapStone


def build():
    top = cylinder(d=CapStone.width, h=CapStone.thk)
    bottom = cube(CapStone.width, CapStone.height * 0.6, CapStone.thk)

    model = bottom + top.right(CapStone.width/2).forward(CapStone.height * 0.6)

    return model
