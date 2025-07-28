from solid2 import *

set_global_fn(150)

# SCALE X%
# 1 inch scales down to X% of 1cm
# Example: 1" --> 0.85cm == 8.5mm
SCALE_PERCENT = 85
# In millimeters
SCALE = (SCALE_PERCENT/100) * 10


def part_A(opts=None):
    return cube([10*SCALE, 2.5*SCALE, 0.75*SCALE])

# ------------------------------------------------------------------------------
PART_LIST = {
    "A": {
        "builder": part_A
    }
}
# ------------------------------------------------------------------------------
def build(name, opts=None):

    data = PART_LIST.get(name)

    if data:
        model = data["builder"](opts)
        return model
    else:
        raise ValueError(f"Part with name '{name}' has not been implemented!")
