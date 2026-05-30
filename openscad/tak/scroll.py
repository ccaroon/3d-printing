from solid2 import *

from units import Scroll


def __band():
    outside = cylinder(d=Scroll.dia, h=Scroll.height)
    inside = cylinder(d=Scroll.dia - Scroll.thk, h=Scroll.height + 2)

    band = outside - inside.down(1).debug()

    return band


def __core():
    # tip_thk = 5

    outer = cylinder(d=Scroll.dia - Scroll.thk, h=Scroll.core_length).color(
        "white", alpha=0.5
    )
    # inner = cylinder(
    #     d=Scroll.dia - Scroll.thk - 3, h=Scroll.core_length - (tip_thk * 2)
    # ).color("yellow")
    # core = outer - inner.up(tip_thk)

    core = outer
    return core


def build(opts):
    part = opts.get("part")
    if part == "band":
        return __band()
    elif part == "core":
        return __core()
