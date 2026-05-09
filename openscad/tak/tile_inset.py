from solid2 import *

from units import Board



def tile_inset():
    height = Board.tile.size * 0.25
    base_r = Board.tile.size * 0.10
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
    ).rotate([90,0,90])

    arm4 = cylinder(
        h=height,
        r1=base_r,
        r2=0,
        _fn=4,
    ).rotate([90,0,-90])

    bottom = cube(height*2, height*2, base_r).down(base_r).left(height).back(height)

    # print(f"Base: {base_r}mm | Height: {height}mm")

    piece = (arm1 + arm2 + arm3 + arm4) - bottom
    return piece



def build():
    return tile_inset()
