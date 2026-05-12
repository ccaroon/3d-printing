from solid2 import *

from units import Stone


def __style1():
    top = cylinder(d=Stone.width, h=Stone.thk)
    bottom = cube(Stone.width, Stone.height * 0.6, Stone.thk)

    model = bottom + top.right(Stone.width / 2).forward(Stone.height * 0.6)

    return model


def __style2():
    model = cylinder(d=Stone.width, h=Stone.thk)
    cut = cube(Stone.width, Stone.height/2, Stone.thk+2, center=True)

    return model - cut.up(Stone.thk / 2).back(Stone.width*0.5)



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
