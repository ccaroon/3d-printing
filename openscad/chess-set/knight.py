from solid2 import *

import common
from units import Knight

def __cylinder_stack(height, count, dia1, dia2, **kwargs):
    """
    height - Height of stack
    count - number of cylinder in the stack
    dia1 - Diameter of face 1
    dia2 - Diameter of face 2
    kwargs:
        - offset - Align to right edge instead of being centered
        - sides - Number of side for each slice in stack
        - scale - Scaling to apply to each slice
    """
    offset = kwargs.get("offset", False)
    sides = kwargs.get("sides", 150)
    scale = kwargs.get("scale", None)
    thk = height / count
    dia_delta = (dia1 - dia2) / count

    stack_info = {
        "count": count,
        "thickness": thk,
        "slices": [],
        "scale": scale,
        "model": None
    }

    count -= kwargs.get("truncate", 0)

    # First slice
    dims = {"d": dia1, "h": thk, "_fn": sides}
    stack_info["slices"].append(dims)
    stack = cylinder(**dims)
    if scale:
        stack = stack.scale(scale)

    # Rest of slices
    for i in range(1, count):
        dims = {
            "d": dia1 - (dia_delta * i), "h": thk, "_fn": sides
        }
        stack_info["slices"].append(dims)
        slice = cylinder(**dims).up(thk * i)

        if scale:
            slice = slice.scale(scale)

        if offset:
            stack += slice.right((dia_delta / 2) * i)
        else:
            stack += slice

    stack_info["model"] = stack
    return stack_info


# Phat Head in an upright position
def __build_head(**kwargs):
    head =  import_(
        file="../images/knight/piper-profile-fill.svg"
        ).linear_extrude(
            height=Knight.head_thk
        )
    head = head.resize([Knight.head_w, Knight.head_h, 0])

    if kwargs.get("upright", False):
        part = head.rotateX(90).translate(
            [-Knight.head_w / 1.5, Knight.head_thk / 2, 0]
        )
    else:
        part = head

    return part


def __build_neck(bottom, scale):
    """
    bottom - Slice data from the body stack
    scale - Scaling of given `bottom` slice
    """
    # top - part that connects to the head
    top_w = 14.5
    top_l = Knight.head_thk

    # bottom - part that connects to the body
    neck = hull()(
        cube([top_w, top_l, .25]).translate([
            -Knight.head_thk / 2,
            -Knight.head_thk / 2,
            Knight.neck_h
        ]),
        cylinder(d=bottom["d"], h=.25, _fn=bottom["_fn"]).scale(scale)
    )

    return neck

def __build_body():
    stack_data = __cylinder_stack(
        Knight.body_height, 7,
        Knight.body_dia1, Knight.body_dia2,
        offset=True,
        sides=8,
        scale=[1.0, .75],
        truncate=0
    )

    return stack_data


def __build_piece(**kwargs):
    # base
    base = common.court_base()

    # body
    body_data = __build_body()
    body = body_data["model"]

    # head
    head = __build_head(upright=True)

    # neck
    body_slice_count = body_data["count"]
    neck = __build_neck(
        body_data["slices"][body_slice_count - 2],
        body_data["scale"]
    )

    peg_dia = 5
    peg_h = 3
    peg_dist = 6
    peg = cylinder(d=peg_dia, h=peg_h).translateX(-0.5)
    pegs =  peg + peg.translateX(peg_dist)

    peg_hole = cylinder(d=peg_dia + .5, h=peg_h+1.5).translateX(-0.5)
    peg_holes = peg_hole + peg_hole.translateX(peg_dist)

    head_pos = [
        4.85,
        0,
        Knight.base_thk + Knight.body_height + Knight.neck_h - body_data["thickness"]
    ]
    neck_pos = [
        3.57,
        0,
        Knight.base_thk + Knight.body_height - body_data["thickness"]
    ]

    part_to_build = kwargs.get("part")
    match part_to_build:
        case "body":
            piece = (
                base +
                body.up(Knight.base_thk) +
                neck.translate(neck_pos) +
                pegs.translate(neck_pos).translateZ(Knight.neck_h)
                # + head.translate(head_pos)
            )
        case "head":
            piece = (
                head.translateX(head_pos[0]) -
                peg_holes.translate(neck_pos[0], 0, -1)
            )
            # Rotate head onto ear and back of neck for printing
            # piece = piece.rotateY(101.75)
        case _:
            piece = (
                base +
                body.up(Knight.base_thk) +
                neck.translate(neck_pos) +
                head.translate(head_pos)
            )

    return piece


def build(opts):
    part_name = None
    if opts:
        part_name = opts[0]
    else:
        part_name = "entire-piece"

    piece = None
    match part_name:
        case "head":
            piece = __build_piece(part="head")
        case "body":
            piece = __build_piece(part="body")
        case "entire-piece":
            piece = __build_piece()
        case _:
            raise ValueError(f"Unknown part `{opts[0]}`. Valid: head | body | entire_piece (default)")


    return piece
