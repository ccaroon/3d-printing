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


def build(opt):
    model = None

    match opt:
        case "twist1":
            model = twist1()
        case "twist2":
            model = twist2()
        case _:
            raise ValueError(f"Unknown option: '{opt}'")

    return model
