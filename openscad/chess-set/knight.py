from solid2 import *

import common
from units import Knight

# Head (left+right) in an upright position
# def __build_head():
#     head =  import_(
#         file="../images/knight/piper-profile-fill.svg"
#         ).linear_extrude(
#             height=Knight.head_thk
#         )

#     for data in ((0.8, "grey"), (0.7, "black")):
#     # for data in ((0.8, "grey"),):
#         scale = data[0]
#         tx = (Knight.head_w - (Knight.head_w * scale)) / 2
#         ty = (Knight.head_h - (Knight.head_h * scale)) / 2

#         left = head.scale([scale,scale,scale]
#             ).translate([tx,ty,Knight.head_thk]
#             ).color(data[1])

#         right = head.scale([scale,scale,scale]
#             ).translate([tx,ty,-Knight.head_thk * scale]
#             ).color(data[1])

#         head = head + left + right

#     part = head.rotateX(90).translateX(-Knight.head_w / 1.5)

#     return part

def __build_head(mirror=False):
    head =  import_(
        file="../images/knight/piper-profile-fill.svg"
        ).linear_extrude(
            height=Knight.head_thk
        )

    for data in ((0.8, "grey"), (0.7, "black")):
        scale = data[0]
        tx = (Knight.head_w - (Knight.head_w * scale)) / 2
        ty = (Knight.head_h - (Knight.head_h * scale)) / 2

        head += head.scale([scale,scale,scale]
            ).translate([tx,ty,Knight.head_thk]
            ).color(data[1])

    if mirror:
        part = head.mirrorX()
    else:
        part = head

    return part


def __cylinder_stack(height, count, dia1, dia2, **kwargs):
    """
    height - Height of stack
    count - number of cylinder in the stack
    """
    offset = kwargs.get("offset", False)
    sides = kwargs.get("sides", 150)
    scale = kwargs.get("scale", None)
    thk = height / count
    dia_delta = (dia1 - dia2) / count


    stack = cylinder(d=dia1, h=thk, _fn=sides)
    if scale:
        stack = stack.scale(scale)

    for i in range(1, count):
        slice = cylinder(d=dia1 - (dia_delta * i), h=thk, _fn=sides).up(thk * i)

        if scale:
            slice = slice.scale(scale)

        if offset:
            stack += slice.right((dia_delta / 2) * i)
        else:
            stack += slice

    return stack


def __oval_stack():
    pass


def __test():
    part1 = cylinder(
        h=Knight.mid_height,
        d1=Knight.mid_dia1,
        d2=Knight.mid_dia2
    )

    part2 = cube([Knight.mid_dia2, Knight.head_thk, Knight.mid_height])

    return part1 + part2.translate(
        [-Knight.mid_dia2 / 2.5, -Knight.mid_dia2 / 2, 0])


def __build_middle():
    return __cylinder_stack(
        Knight.mid_height, 8,
        Knight.mid_dia1, Knight.mid_dia2,
        offset=True,
        # sides=6
        scale=[1.0, .75]
    )


def __build_piece():
    pass


def build(opts):
    part_name = None
    if opts:
        part_name = opts[0]
    else:
        part_name = "entire-piece"

    piece = None
    match part_name:
        case "head":
            hleft = __build_head(False)
            hright = __build_head(True)
            piece  = hleft + hright.translate(
                [Knight.head_w,Knight.head_h + 2, 0])
        case "head-left":
            piece = __build_head(False)
        case "head-right":
            piece = __build_head(True)
            piece = piece.translateX(Knight.head_w)
        case "base":
            base = common.court_base()
            middle = __build_middle()
            piece = base + middle.up(Knight.base_thk)
        case "entire-piece":
            piece = __build_piece()
        case _:
            raise ValueError(f"Unknown part `{opts[0]}`. Valid: head | head-left | head-right | base | entire_piece (default)")


    return piece
