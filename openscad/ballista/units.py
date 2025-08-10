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
    thickness = 0.75 * UNIT
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
    hole_dia   = 0.25 * Standard.unit,
    hole_depth = 0.25 * Standard.unit,
)

PartG = __constant(
    "PartG",
    length     = 5.00 * Standard.unit,
    width      = 0.75 * Standard.unit,
    height     = Standard.thickness,
    hole_dia   = 0.25 * Standard.unit,
    hole_depth = Standard.thickness + 2,
    hole_z     = -1
)

PartJ = __constant(
    "PartJ",
    length     = 2.5 * Standard.unit,
    width      = 2.5 * Standard.unit,
    height     = Standard.thickness,
    hole_dia   = 0.25 * Standard.unit,
    hole_depth = Standard.thickness + 2,
    hole_z     = -1,
    radius     = 1.25 * Standard.unit
)

PartL = __constant(
    "PartL",
    length = 2.5 * Standard.unit,
    width  = 0.5 * Standard.unit,
    height = 0.5 * Standard.unit
)

# Dowels
PartHI = __constant(
    "PartHI",
    length = 2.0 * Standard.unit,
    dia    = 0.25 * Standard.unit
)












#
