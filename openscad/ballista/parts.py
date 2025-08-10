from solid2 import *

from units import Standard, \
                    PartA, PartB, PartC, \
                    PartD, PartEF, PartG, \
                    PartHI, PartJ, PartL

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


def part_G(opts=None):
    piece = polygon([
        [0, 0],
        [0, 0.5 * Standard.unit],
        [0.5 * Standard.unit, PartG.width],
        [PartG.length - 0.5 * Standard.unit, PartG.width],
        [PartG.length, 0.5 * Standard.unit],
        [PartG.length, 0]
    ]).linear_extrude(height=PartG.height)

    hole = cylinder(d=PartG.hole_dia, h=PartG.hole_depth)

    part = (
        piece
        - hole.translate([
            PartG.length - 1.5 * Standard.unit,
            0.375 * Standard.unit,
            PartG.hole_z
        ])
    )

    return part


def part_HI(opts=None):
    part = cylinder(d=PartHI.dia, h=PartHI.length)
    return part


def part_J(opts=None):
    piece1 = cube([PartJ.length, PartJ.radius, PartJ.height])
    piece2 = cylinder(d=PartJ.radius * 2, h=PartJ.height)

    hole = cylinder(d=PartJ.hole_dia, h=PartJ.hole_depth)

    part = (
        piece1
        + piece2.translate([
            PartJ.radius,
            PartJ.radius,
            0
        ])
        - hole.translate(
            PartJ.radius,
            0.5 * Standard.unit,
            PartJ.hole_z
        )
    )

    return part


def part_L(opts=None):
    piece1 = cylinder(d=PartL.height, h=PartL.length).rotateY(90).translate([
        0, PartL.width / 2, PartL.height / 2
    ])
    piece2 = cube([PartL.length, PartL.width, PartL.height * 0.5])

    part = (
        piece1 + piece2
    )

    # Stand on end for better printing of rounded edge
    return part.rotateY(-90)


# ------------------------------------------------------------------------------
PART_LIST = {
    "A": { "builder": part_A },
    "B": { "builder": part_B },
    "C": { "builder": part_C },
    "D": { "builder": part_D },
    "E": { "builder": part_E },
    "F": { "builder": part_F },
    "G": { "builder": part_G },
    "H": { "builder": part_HI },
    "I": { "builder": part_HI },
    "J": { "builder": part_J },
    # K - TODO
    "L": { "builder": part_L }
}
# ------------------------------------------------------------------------------
def build(part_name, opts=None):
    data = PART_LIST.get(part_name)

    if data:
        model = data["builder"](opts)
        return model
    else:
        print(f"=> Part with name '{part_name}' has not been implemented!")
