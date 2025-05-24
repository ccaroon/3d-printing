from solid2 import *

import common
from units import Bishop


def __build_top():
    head_size = Bishop.base_dia * 0.50
    pom_size = head_size * 0.25

    pom = sphere(d=pom_size).resize([pom_size * 1.5, pom_size * 1.5, 0])

    head = sphere(d=head_size).resize(
        [0, 0, Bishop.base_dia * 0.66]
    )

    cut = cylinder(d=head_size, h=1).rotate([0, -50, 0])

    return head.up(head_size * 0.25) - cut.translate(3 ,0, 3) + pom.up(head_size - pom_size / 2)
    # return head - cut.translate(3 ,0, 3)


def __build_middle():
    center = circle(
        d=Bishop.base_dia * 0.50,
        _fn=5
    ).linear_extrude(
        height=Bishop.height,
        twist=360,
        # slices=50
        # scale=[1,1.33]
    )

    footer1 = minkowski()(
        sphere(d=2.0),
        cylinder(d=Bishop.base_dia * 0.75, h=1)
    )

    footer2 = minkowski()(
        sphere(d=2.0),
        cylinder(d=Bishop.base_dia * 0.66, h=1)
    )

    # part = center.rotate([0, 180, 0]).up(Bishop.height)
    part = center + footer1 + footer2.up(1)

    return part


def build():
    bottom = common.court_base()
    middle = __build_middle()
    top = __build_top()

    piece = bottom              + \
            middle.up(Bishop.base_thk) + \
            top.up(Bishop.base_thk + Bishop.height)
    # piece = top

    return piece
