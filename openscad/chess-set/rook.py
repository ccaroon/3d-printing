import math
from solid2 import *

import common
from units import Brick, Rook

def brick_layer():
    """
    A layer of brick laid out in a circle.

    *** No Pun Intended ***
    """
    dist = (Rook.base_dia / 2) - Brick.width

    brick = (
        cube([Brick.length, Brick.width, Brick.height])
        .translate([-Brick.length / 2, -Brick.width / 2, 0])
        .color("red")
    )

    hv_delta = (dist / 2) + Brick.width
    diag_delta = (dist / 2) + 1
    layer = (
        brick.forward(hv_delta) +
        brick.rotateZ(-45).forward(diag_delta).right(diag_delta) +
        brick.rotateZ(-90).right(hv_delta) +
        brick.rotateZ(45).back(diag_delta).right(diag_delta) +
        brick.back(hv_delta) +
        brick.rotateZ(-45).back(diag_delta).left(diag_delta) +
        brick.rotateZ(90).left(hv_delta) +
        brick.rotateZ(45).forward(diag_delta).left(diag_delta)
    )

    return layer


def __build_top():
    lip_dia = Rook.base_dia * 0.75
    lip_h = Brick.height / 2
    lip = cylinder(d=lip_dia, h=lip_h)

    parapet_h = Rook.height * 0.25
    parapet = cylinder(d1=lip_dia, d2=lip_dia+2, h=parapet_h)
    cutout = sphere(d=lip_dia).up(lip_dia/2)

    slice_w = 2
    slice_l = 8
    slice_h = parapet_h * 0.75
    slice = cube([slice_w, slice_l, slice_h], center=False)

    return (
        lip +
        (parapet - cutout) -
        slice.translate([-slice_w/2, (lip_dia/2) - (slice_l/2), lip_h + (parapet_h * .25)]) -
        slice.translate([-slice_w/2, (-lip_dia/2) - (slice_l/2), lip_h + (parapet_h * .25)]) -
        slice.translate([-slice_w/2, (-lip_dia/2) - (slice_l/2), lip_h + (parapet_h * .25)]).rotateZ(90) -
        slice.translate([-slice_w/2, (-lip_dia/2) - (slice_l/2), lip_h + (parapet_h * .25)]).rotateZ(-90)
    )


def __build_middle():
    num_layers = int(Rook.height // Brick.height)

    middle = brick_layer()
    for count in range(1, num_layers-1):
        layer = brick_layer().up(Brick.height * count)

        if count % 2 != 0:
            middle += layer.rotateZ(-22.5)
        else:
            middle += layer

    return middle


def build():
    base = common.court_base()

    top = __build_top()
    middle = __build_middle()

    return base + middle.up(Rook.base_thk) + top.up(Rook.height - 0.25)






#
