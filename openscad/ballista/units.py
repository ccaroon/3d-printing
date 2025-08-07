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
    hole_dia = 1 * Standard.unit,
    hole_h   = Standard.thickness + 2, # 2 b/c 1 above, 1 below
    hole_x   = 2 * Standard.unit,
    hole_y   = 1.25 * Standard.unit,
    hole_z   = -1
)
