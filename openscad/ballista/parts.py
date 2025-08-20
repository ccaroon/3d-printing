from solid2 import *

from units import Standard, \
                    PartA,  PartB,  PartC, \
                    PartD,  PartEF, PartG, \
                    PartHI, PartJ,  PartK, \
                    PartL, PartM,   PartQ, \
                    PartS, PartT,   PartU, \
                    PartV, PartW,   PartX, \
                    PartY, PartZ

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
        [0, PartEF.width - Standard.unit_3_8],
        [Standard.unit_3_4, PartEF.width],
        [PartEF.length - Standard.unit_1_4, PartEF.width],
        [PartEF.length, PartEF.width - Standard.unit_1_4],
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
            Standard.unit_1_2,
            PartEF.height - PartEF.hole_depth
        ])
        - hole.translate([
            PartEF.length - Standard.unit_1_2,
            PartEF.width - Standard.unit_3_8,
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
            Standard.unit_1_2,
            PartEF.height - PartEF.hole_depth
        ])
        - hole.translate([
            Standard.unit_1_2,
            PartEF.width - Standard.unit_3_8,
            PartEF.height - PartEF.hole_depth
        ])
    )

    return part


def part_G(opts=None):
    piece = polygon([
        [0, 0],
        [0, Standard.unit_1_2],
        [Standard.unit_1_2, PartG.width],
        [PartG.length - Standard.unit_1_2, PartG.width],
        [PartG.length, Standard.unit_1_2],
        [PartG.length, 0]
    ]).linear_extrude(height=PartG.height)

    hole = cylinder(d=PartG.hole_dia, h=PartG.hole_depth)

    part = (
        piece
        - hole.translate([
            PartG.length - (1.5 * Standard.unit),
            Standard.unit_3_8,
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
            Standard.unit_1_2,
            PartJ.hole_z
        )
    )

    return part


def part_K(opts=None):
    left1 = polygon([
        [0, 0],
        [0, PartK.width],
        # top notch
        [PartK.notch_x - (PartK.notch_w / 2), PartK.width],
        [PartK.notch_x, PartK.width - PartK.notch_d],
        [PartK.notch_x + (PartK.notch_w / 2), PartK.width],
        # bottom notch
        [PartK.notch_x + (PartK.notch_w / 2), 0],
        [PartK.notch_x, PartK.notch_d],
        [PartK.notch_x - (PartK.notch_w / 2), 0],
    ]).linear_extrude(height=PartG.height).color("#00ff77")

    left2 = cube([
        PartK.non_taper_l - (PartK.notch_x + PartK.notch_w / 2),
        PartK.width,
        PartK.height
    ]).color("#0077ff")

    taper_len = PartK.length - PartK.non_taper_l
    taper_l = cube([1, PartK.width, PartK.height])
    taper_r = cylinder(d=PartK.height, h=1).rotateY(90).translate([
        taper_len - 1, # -1 for height/thkness of cylinder
        PartK.width / 2,
        PartK.height / 2
    ])

    taper_piece = hull()(
        taper_l, taper_r
    ).color("#770077")

    hole = cylinder(d=PartK.hole_dia, h=PartK.hole_depth)
    taper_piece -= hole.translate([
        PartK.taper_l - Standard.unit_1_2,
        Standard.unit_3_8,
        PartK.hole_z
    ])

    part = (
        left1
        + left2.translateX(PartK.notch_x + PartK.notch_w / 2)
        + taper_piece.translateX(PartK.non_taper_l)
    )

    # Stand on the square end for better printing
    return part.rotateY(-90)


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


def part_M(opts=None):
    taper_l = (PartM.length - PartM.front_l) / 2
    base_piece = polygon([
        [taper_l, 0],
        [0, 1.0 * Standard.unit],
        [0, PartM.width],
        [PartM.length, PartM.width],
        [PartM.length, 1.0 * Standard.unit],
        [PartM.length - taper_l, 0]
    ]).linear_extrude(height=PartM.height)

    hole = cylinder(d=PartM.hole_dia, h=PartM.hole_depth).rotateY(90)

    piece = (
        base_piece
        - hole.translate([PartM.hole_x, 1.0 * Standard.unit, PartM.height / 2])
        - hole.translate([PartM.hole_x, Standard.unit_1_2, PartM.height / 2])
    )


    cutout = cylinder(r=PartM.cutout_rad, h=PartM.height + 2)

    part = (
        piece
        - cutout.translate(Standard.unit_3_4, PartM.width, -1)
    )

    return part


def part_Q(opts=None):
    piece = polygon([
        [0, 0],
        [PartQ.length - PartQ.back_l, PartQ.width],
        [PartQ.length, PartQ.width],
        [PartQ.length, 0]
    ]).linear_extrude(height=PartQ.height)

    hole = cylinder(d=PartQ.hole_dia, h=PartQ.hole_depth)

    part = (
        piece
        - hole.translate([
            PartQ.length - Standard.unit_1_2,
            Standard.unit_3_8,
            PartQ.hole_z
        ])
    )

    return part


def part_S(opts=None):
    piece = polygon([
        [0, 0],
        [0, PartS.width],
        [PartS.length - Standard.unit_1_4, PartS.width],
        [PartS.length, PartS.width - Standard.unit_1_4],
        [PartS.length, Standard.unit_1_4],
        [PartS.length - Standard.unit_1_4, 0]
    ]).linear_extrude(height=PartS.height)

    hole = cylinder(d=PartS.hole_dia, h=PartS.hole_depth)

    part = (
        piece
        - hole.translate([
            PartS.length - Standard.unit_1_2,
            Standard.unit_3_8,
            PartS.hole_z
        ])
    )

    return part


def part_T(opts=None):
    piece = cube([PartT.length, PartT.width, PartT.height])
    hole = cylinder(d=PartT.hole_dia, h=PartT.hole_depth + 1)

    part = (
        piece
        - hole.translate([
            Standard.unit_3_8,
            PartT.width - 2.0 * Standard.unit,
            PartT.height - PartT.hole_depth
        ])
        - hole.translate([
            Standard.unit_3_8,
            PartT.width - 4.5 * Standard.unit,
            PartT.height - PartT.hole_depth
        ])
        - hole.translate([
            Standard.unit_3_8,
            PartT.width - 7.75 * Standard.unit,
            PartT.height - PartT.hole_depth
        ])
        - hole.translate([
            Standard.unit_3_8,
            PartT.width - 10.5 * Standard.unit,
            PartT.height - PartT.hole_depth
        ])
    )

    return part


def part_U(opts=None):
    piece = cube([PartU.length, PartU.width - PartU.radius, PartU.height])
    tip = cylinder(d=PartU.radius * 2, h=PartU.height)
    hole = cylinder(d=PartU.hole_dia, h=PartU.hole_depth)

    part = (
        piece
        + tip.translate([
            PartU.length / 2,
            PartU.width - PartU.radius,
            0
        ])
        - hole.translate([
            Standard.unit_3_4,
            PartU.width - Standard.unit_1_2,
            PartU.hole_z
        ])
    )

    return part


def part_V(opts=None):
    back_pt_l = (PartV.length - PartV.back_l) / 2.0
    piece = polygon([
        [0, 0],
        [back_pt_l, PartV.width],
        [PartV.length - back_pt_l, PartV.width],
        [PartV.length, 0]
    ]).linear_extrude(height=PartV.height)

    part = (
        piece
    )

    return part


def part_W(opts=None):
    back_pt_l = (PartW.length - PartW.back_l) / 2.0
    piece = polygon([
        [0, 0],
        [back_pt_l, PartW.width],
        [PartW.length - back_pt_l, PartW.width],
        [PartW.length, 0]
    ]).linear_extrude(height=PartW.height)

    part = (
        piece
    )

    return part


def part_X(opts=None):
    part = cube([PartX.length, PartX.width, PartX.height])
    return part


def part_Y(opts=None):
    part = cylinder(d=PartY.dia, h=PartY.length)
    return part


def part_Z(opts=None):
    part = cylinder(d=PartZ.dia, h=PartZ.length)
    return part


def ruler(opts=None):
    """ A ruler in Standard.unit(s) to help assemble the Ballista """
    dims = {k: float(v) for k,v in (opt.split("=", 2) for opt in opts)}

    length = dims.get("l", 10)
    width = dims.get("w", 1)
    height = dims.get("h", 1)

    return cube([length * Standard.unit, width * Standard.unit, height])


# ------------------------------------------------------------------------------
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
    "K": { "builder": part_K },
    "L": { "builder": part_L },
    "M": { "builder": part_M },
    # N: Jute Cord
    # O: Nylon Cord
    # P: Nylon Cord
    "Q": { "builder": part_Q },
    # R: Jute Cord
    "S": { "builder": part_S },
    "T": { "builder": part_T },
    "U": { "builder": part_U },
    "V": { "builder": part_V },
    "W": { "builder": part_W },
    "X": { "builder": part_X },
    "Y": { "builder": part_Y },
    "Z": { "builder": part_Z },
    "RULER": {"builder": ruler}
}
# ------------------------------------------------------------------------------
def build(part_name, opts=None):
    parts = {}
    if part_name == "ALL":
        for name, data in PART_LIST.items():
            part = data["builder"](opts)
            parts[name] = part
    else:
        data = PART_LIST.get(part_name)
        if data:
            part = data["builder"](opts)
            parts[part_name] = part
        else:
            print(f"=> Part with name '{part_name}' has not been implemented!")

    if parts:
        for part_name, part in parts.items():
            base_name = f"ballista-p{part_name}"
            if opts:
                opts_sfx = "-".join(opts)
                base_name += f"-{opts_sfx}"

            file_name = f"./models/{base_name}.scad"
            part.save_as_scad(file_name)
            print(f"=> {file_name}")





#
