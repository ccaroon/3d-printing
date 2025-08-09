from solid2 import *

from units import Standard, PartA, PartB, PartC, PartD, PartEF

set_global_fn(150)

def part_A(opts=None):
    piece = cube([PartA.length, PartA.width, PartA.height])
    hole = cylinder(d=PartA.hole_dia, h=PartA.hole_depth)

    part = (
        piece
        - hole.translate([
            PartA.hole_x,
            PartA.width - PartA.hole_y,
            PartA.hole_z
        ])
        - hole.translate([
            PartA.length - PartA.hole_x,
            PartA.width - PartA.hole_y,
            PartA.hole_z
        ])
    )

    return part


def part_B(opts=None):
    return cube([PartB.length, PartB.width, PartB.height])


def part_C(opts=None):
    piece = cube([PartC.length/2, PartC.width, PartC.height])
    rounded_edge = (
        cylinder(d=PartC.height, h=PartC.width)
        .rotateX(-90)
        .translate([PartC.length - (PartC.height / 2), 0, PartC.height / 2])
    )

    part = hull()(
        piece, rounded_edge
    )

    # Uncomment to see bounding box for size verfication
    # bnd_box = cube([PartC.length, PartC.width, PartC.height]).debug()
    # return part + bnd_box

    return part.rotateX(90)



def part_D(opts=None):
    return cube([PartD.length, PartD.width, PartD.height])


def __EF_base(opts=None):
    part = polygon([
        [0, 0],
        [0, PartEF.width - ((3/8)*Standard.unit)],
        [0.75*Standard.unit, PartEF.width],
        [PartEF.length - (0.25*Standard.unit), PartEF.width],
        [PartEF.length, PartEF.width - (0.25*Standard.unit)],
        [PartEF.length, 0]
    ]).linear_extrude(height=PartEF.height)

    return part


def part_E(opts=None):
    piece = __EF_base(opts)

    hole = cylinder(d=PartEF.hole_dia, h=PartEF.hole_depth+1)

    part = (
        piece
        - hole.translate([
            1.75 * Standard.unit,
            0.50 * Standard.unit,
            PartEF.height - PartEF.hole_depth
        ])
        - hole.translate([
            PartEF.length - 0.50 * Standard.unit,
            PartEF.width - (3/8) * Standard.unit,
            PartEF.height - PartEF.hole_depth
        ])
    )

    return part


def part_F(opts=None):
    piece = __EF_base(opts)
    piece = piece.rotateY(180).translate([
        PartEF.length, 0, PartEF.height
    ])

    hole = cylinder(d=PartEF.hole_dia, h=PartEF.hole_depth+1)

    part = (
        piece
        - hole.translate([
            1.75 * Standard.unit,
            0.50 * Standard.unit,
            PartEF.height - PartEF.hole_depth
        ])
        - hole.translate([
            0.50 * Standard.unit,
            PartEF.width - (3/8) * Standard.unit,
            PartEF.height - PartEF.hole_depth
        ])
    )

    return part


# ------------------------------------------------------------------------------
PART_LIST = {
    "A": { "builder": part_A },
    "B": { "builder": part_B },
    "C": { "builder": part_C },
    "D": { "builder": part_D },
    "E": { "builder": part_E },
    "F": { "builder": part_F }
}
# ------------------------------------------------------------------------------
def build(part_name, opts=None):
    data = PART_LIST.get(part_name)

    if data:
        model = data["builder"](opts)
        return model
    else:
        print(f"=> Part with name '{part_name}' has not been implemented!")
