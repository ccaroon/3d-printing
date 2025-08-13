from collections import namedtuple

# SCALE X%
# 1 inch scales down to X% of 1cm
# Example: 1" --> 0.85cm == 8.5mm
SCALE_PERCENT = 85
# In millimeters
UNIT = (SCALE_PERCENT/100) * 10

def __constant(name, **kwargs):
    const_class = namedtuple(f"{name}Const", kwargs.keys())
    return const_class(**kwargs)


# Standard Unit
Standard = __constant(
    "Standard",
    unit = UNIT,
    thickness = 0.75 * UNIT,

    # Convenience units
    unit_1_2  = (1/2) * UNIT,
    unit_1_4  = (1/4) * UNIT,
    unit_1_8  = (1/8) * UNIT,
    unit_3_4  = (3/4) * UNIT,
    unit_3_8  = (3/8) * UNIT,
    unit_3_16 = (3/16) * UNIT
)

PartA = __constant(
    "PartA",
    length   = 10 * Standard.unit,
    width    = 2.5 * Standard.unit,
    height   = Standard.thickness,
    hole_dia    = 1 * Standard.unit,
    hole_depth  = Standard.thickness + 2, # 2 b/c 1 above, 1 below
    hole_x      = 2 * Standard.unit,
    hole_y      = 1.25 * Standard.unit,
    hole_z      = -1
)

PartB = __constant(
    "PartB",
    length = 2.5 * Standard.unit,
    width  = 3 * Standard.unit,
    height = Standard.thickness
)

PartC = __constant(
    "PartC",
    length = 1.5 * Standard.unit,
    width  = 3 * Standard.unit,
    height = Standard.thickness
)

PartD = __constant(
    "PartD",
    length = 24.5 * Standard.unit,
    width  = 1.5 * Standard.unit,
    height = Standard.thickness
)

PartEF = __constant(
    "PartEF",
    length   = 3.5 * Standard.unit,
    width    = 3.0 * Standard.unit,
    height   = Standard.thickness,
    hole_dia   = Standard.unit_1_4,
    hole_depth = Standard.unit_1_4
)

PartG = __constant(
    "PartG",
    length     = 5.00 * Standard.unit,
    width      = Standard.unit_3_4,
    height     = Standard.thickness,
    hole_dia   = Standard.unit_1_4,
    hole_depth = Standard.thickness + 2,
    hole_z     = -1
)

# Dowels
PartHI = __constant(
    "PartHI",
    length = 2.0 * Standard.unit,
    dia    = Standard.unit_1_4
)

PartJ = __constant(
    "PartJ",
    length     = 2.5 * Standard.unit,
    width      = 2.5 * Standard.unit,
    height     = Standard.thickness,
    hole_dia   = Standard.unit_1_4,
    hole_depth = Standard.thickness + 2,
    hole_z     = -1,
    radius     = 1.25 * Standard.unit
)

PartK = __constant(
    "PartK",
    length = 8.0  * Standard.unit,
    width  = Standard.unit_3_4,
    height = Standard.thickness,

    # Should total `length` above
    non_taper_l = 2.0 * Standard.unit,
    taper_l     = 6.0 * Standard.unit,

    hole_dia   = Standard.unit_3_16,
    hole_depth = Standard.thickness + 2,
    hole_z     = -1,

    notch_x    = Standard.unit_3_4,
    notch_w    = Standard.unit_1_4,
    notch_d    = Standard.unit_1_8
)

PartL = __constant(
    "PartL",
    length = 2.5 * Standard.unit,
    width  = Standard.unit_1_2,
    height = Standard.unit_1_2
)

PartM = __constant(
    "PartM",
    length = 1.5 * Standard.unit,
    width  = 2.0 * Standard.unit,
    height = Standard.thickness,

    front_l    = Standard.unit_3_4,
    cutout_rad = Standard.unit_3_8,

    hole_dia   = Standard.unit_3_16,
    # holes are horizontal, not vertical
    # so depth is same as `length` + 2
    hole_depth = (1.5 * Standard.unit) + 2,
    hole_x     = -1
)

PartQ = __constant(
    "PartQ",
    length = (2.0 * Standard.unit) + Standard.unit_3_8,
    width  = Standard.unit_3_4,
    height = Standard.thickness,

    back_l = (1.0 + (5/8)) * Standard.unit,

    hole_dia   = Standard.unit_1_4,
    hole_depth = Standard.thickness + 2,
    hole_z     = -1
)

PartS = __constant(
    "PartS",
    length = (9.0 * Standard.unit) + Standard.unit_3_8,
    width  = Standard.unit_3_4,
    height = Standard.thickness,

    hole_dia   = Standard.unit_1_4,
    hole_depth = Standard.thickness + 2,
    hole_z     = -1
)

PartT = __constant(
    "PartT",
    length = Standard.unit_3_4,
    width  = 23.0 * Standard.unit,
    height = Standard.thickness,

    hole_dia   = Standard.unit_1_4,
    hole_depth = Standard.unit_1_2
)

PartU = __constant(
    "PartU",
    length = 1.5 * Standard.unit,
    width  = 8.75 * Standard.unit,
    height = Standard.thickness,

    hole_dia   = Standard.unit_1_4,
    hole_depth = Standard.thickness + 2,
    hole_z     = -1,

    radius = Standard.unit_3_4
)

PartV = __constant(
    "PartV",
    length = 7.5 * Standard.unit,
    back_l = 6.0 * Standard.unit,
    width  = Standard.unit_3_4,
    height = Standard.thickness
)

PartW = __constant(
    "PartW",
    length = 6.0 * Standard.unit,
    back_l = 4.5 * Standard.unit,
    width  = Standard.unit_3_4,
    height = Standard.thickness
)

PartX = __constant(
    "PartX",
    length = 5.25 * Standard.unit,
    width  = 1.5 * Standard.unit,
    height = Standard.thickness
)

# More Dowels
PartY = __constant(
    "PartY",
    length = 1.25 * Standard.unit,
    dia    = Standard.unit_1_4
)

PartZ = __constant(
    "PartZ",
    length = 3.0 * Standard.unit,
    dia    = Standard.unit_1_4
)










#
