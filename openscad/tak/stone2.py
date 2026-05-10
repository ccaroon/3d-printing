from solid2 import *

from units import Stone


def build():
    top = cylinder(d=Stone.width, h=Stone.thk)
    bottom = cube(Stone.width, Stone.height * 0.6, Stone.thk)

    model = bottom + top.right(Stone.width / 2).forward(Stone.height * 0.6)

    return model
