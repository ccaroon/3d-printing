from solid2 import *

import common
from units import Bishop


def __build_top():
    head_size = Bishop.base_dia * 0.60
    pom_size = head_size * 0.25

    pom = sphere(d=pom_size).resize([pom_size * 1.5, pom_size * 1.5, 0])

    head = sphere(d=head_size).resize(
        [0, 0, Bishop.base_dia * 0.75]
    )

    cut = cylinder(d=head_size, h=1).rotate([0, -50, 0])

    return (
        head.up(head_size * 0.25) - cut.translate(3, 0, 5) +
        pom.up(head_size - pom_size * 0.33)

    )


def __build_middle_twist():
    center = circle(
        d=Bishop.base_dia * 0.50,
        _fn=5
    ).linear_extrude(
        height=Bishop.height,
        twist=360,
        # slices=50
        # scale=[1,1.33]
    )

    collar_h = 2
    collar1 = cylinder(
        d1=Bishop.base_dia * 0.40,
        d2=Bishop.base_dia * 0.66,
        h=collar_h
    )
    collar2 = cylinder(
        d1=Bishop.base_dia * 0.66,
        d2=Bishop.base_dia * 0.48,
        h=collar_h
    )

    collar = collar1 + collar2.up(collar_h)

    footer1 = minkowski()(
        sphere(d=2.0),
        cylinder(d=Bishop.base_dia * 0.75, h=1)
    )

    # footer2 = minkowski()(
    #     sphere(d=2.0),
    #     cylinder(d=Bishop.base_dia * 0.66, h=1)
    # )
    footer2 = cylinder(
        d1=Bishop.base_dia * 0.66,
        d2=Bishop.base_dia * 0.50,
        h=Bishop.height * 0.25
    )

    # part = center.rotate([0, 180, 0]).up(Bishop.height)
    part = center + collar.up(Bishop.height *.90) + footer1 + footer2.up(1)

    return part


def __build_middle_profile():
    profile = import_dxf("./images/bishop/Bishop-Profile.dxf")
    middle_part = profile.rotate_extrude(angle=360, _fn=250)

    return middle_part


def build():
    bottom = common.court_base()
    middle = __build_middle_profile()
    top = __build_top()

    piece = bottom                     + \
            middle.up(Bishop.base_thk) + \
            top.up(Bishop.base_thk + Bishop.height - 1)
    # piece = middle

    return piece
