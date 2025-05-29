import math
from solid2 import *

from units import Base

def twist1():
    tw = circle(d=Base.dia, _fn=5).linear_extrude(
        height=30,
        twist=90,
        # convexity=10,
        # slices=10
    )
    return tw


def twist2():
    tw = circle(d=Base.dia, _fn=5).linear_extrude(
        height=30,
        twist=90,
        scale=[1, 1.25],
        # convexity=10,
        # slices=10
    )
    return tw


def rook_middle():
    center = circle(
        d=Bishop.base_dia * 0.50,
        _fn=5
    ).linear_extrude(
        height=Bishop.height,
        twist=360,
        slices=10
        # scale=[1,1.33]
    )

    return center



def collar():
    collar_h = 2
    d1 = Base.dia * 0.50
    d2 = Base.dia * 0.66
    collar1 = cylinder(
        d1=d1,
        d2=d2,
        h=collar_h
    )
    collar2 = cylinder(
        d1=d2,
        d2=d1,
        h=collar_h
    )

    # atan2(y2 - y1, x2 - x1)
    # a = (1,0) # (x1, y1)
    # b = (2,1) # (x2, y2)
    # --------------------
    a = (d1, 0)
    b = (d2, collar_h)
    angle = math.atan2(b[1] - a[1], b[0] - a[0])
    print(angle * 180/math.pi)

    return collar1 + collar2.up(collar_h)


def build(opt):
    model = None

    match opt:
        case "twist1":
            model = twist1()
        case "twist2":
            model = twist2()
        case "rook_middle":
            model = rook_middle()
        case "collar":
            model = collar()
        case _:
            raise ValueError(f"Unknown option: '{opt}'")

    return model
