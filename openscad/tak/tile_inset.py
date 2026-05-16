from solid2 import *

from units import Board


def tile_inset():
    # cylinder height -> star arm
    height = Board.tile_inset.length
    # cylinder radius -> star arm base height
    base_r = Board.tile_inset.height

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
    return tile_inset()
