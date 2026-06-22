from solid2 import *

from units import Board


def __hexagon(opts):
    padding = opts.get("padding", 0)
    piece = cylinder(r=Board.ti_s2.radius + padding, h=Board.ti_s2.height, _fn=6)

    return piece


def __star_ghoti(opts):
    # cylinder height -> star arm
    height = Board.ti_s1.length
    # cylinder radius -> star arm base height
    base_r = Board.ti_s1.height + opts.get("ex_h", 0)

    arm1 = cylinder(
        h=height,
        r1=base_r,
        r2=0,
        _fn=4,
    ).rotateX(-90)

    arm2 = cylinder(
        h=height,
        r1=base_r,
        r2=0,
        _fn=4,
    ).rotateX(90)

    arm3 = cylinder(
        h=height,
        r1=base_r,
        r2=0,
        _fn=4,
    ).rotate([90, 0, 90])

    arm4 = cylinder(
        h=height,
        r1=base_r,
        r2=0,
        _fn=4,
    ).rotate([90, 0, -90])

    bottom = cube(height * 2, height * 2, base_r).down(base_r).left(height).back(height)

    # print(f"Base: {base_r}mm | Height: {height}mm")

    piece = (arm1 + arm2 + arm3 + arm4) - bottom
    return piece


def build(opts):
    style = opts.get("style", "s1")

    model = None
    match style:
        case "s1":
            model = __star_ghoti(opts)
        case "s2":
            model = __hexagon(opts)

    return model
