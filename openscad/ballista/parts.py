from solid2 import *

from units import Standard, PartA

set_global_fn(150)

def part_A(opts=None):
    piece = cube([PartA.length, PartA.width, PartA.height])
    hole = cylinder(d=PartA.hole_dia, h=PartA.hole_h)

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


# ------------------------------------------------------------------------------
PART_LIST = {
    "A": {
        "builder": part_A
    }
}
# ------------------------------------------------------------------------------
def build(part_name, opts=None):
    data = PART_LIST.get(part_name)

    if data:
        model = data["builder"](opts)
        return model
    else:
        print(f"=> Part with name '{part_name}' has not been implemented!")
