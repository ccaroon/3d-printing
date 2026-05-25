from solid2 import *

from units import Stone


def __style1():
    hscale = 0.575
    top = cylinder(d=Stone.width, h=Stone.thk, _fn=6)
    bottom = cube(Stone.width, Stone.height * hscale, Stone.thk)

    model = bottom + top.right(Stone.width / 2).forward(Stone.height * hscale)

    return model


def __style2():
    model = cylinder(d=Stone.width, h=Stone.thk, _fn=5)

    return model


def build(opts):
    piece = None

    match opts.get("style"):
        case "style1":
            piece = __style1()
        case "style2":
            piece = __style2()
        case _:
            piece = __style1()

    return piece
