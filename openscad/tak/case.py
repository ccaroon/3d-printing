from solid2 import *

from lib.box import Box
from units import Board, CapStone, CaseS1, CaseS2, CasePost, Magnet, Stone


def __post(style):
    height = CaseS1.height if style == "s1" else CaseS2.height

    post = cube(CasePost.width, CasePost.length, height)
    # magnet = cylinder(d=Magnet.dia, h=Magnet.thk+1)

    # offset = (Magnet.dia / 2) + Board.magnet_offset

    return post  # - magnet.translate(offset, offset, CaseS1.height - Magnet.thk)


def __style1(opts):
    # overall box
    case_box = Box(
        CaseS1.width,
        CaseS1.length,
        CaseS1.height,
        CaseS1.wall_thk,
        Box.DIMS_OUTER,
    )
    case = case_box.build()

    # corner posts with magnet cutouts
    mag_radius = Magnet.dia / 2
    for row in range(2):
        for col in range(2):
            x = CaseS1.width * col
            y = CaseS1.length * row

            # Magnet cutout
            magnet = cylinder(d=Magnet.dia, h=Magnet.thk + 0.25)
            magx_offset = mag_radius + Board.magnet_offset
            magx_offset *= -1 if col == 1 else 1
            mag_x = x + magx_offset

            magy_offset = mag_radius + Board.magnet_offset
            magy_offset *= -1 if row == 1 else 1
            mag_y = y + magy_offset

            # Post
            post = __post("s1")
            postx_offset = CasePost.width * col
            postx_offset *= -1 if col == 1 else 1
            post_x = x + postx_offset

            posty_offset = CasePost.length * row
            posty_offset *= -1 if row == 1 else 1
            post_y = y + posty_offset

            case = (
                case
                + post.translate(post_x, post_y, 0)
                - magnet.translate(
                    mag_x,
                    mag_y,
                    CaseS1.height - Magnet.thk,
                )
            )

    # Stones Compartments
    ## Sizes
    capstone_h = CapStone.base_h + CapStone.mid_height + CapStone.top_dia
    cmp_width = Stone.height + 2
    # hold stone_cnt1 stones+1 (extra room)
    cmp_length = Stone.thk * (CaseS1.stone_cnt1 + 1)
    cmp_height = CaseS1.height
    cmp_wall = CaseS1.wall_thk / 2

    stone_box_lg = Box(
        cmp_width,
        cmp_length,
        cmp_height,
        cmp_wall,
        Box.DIMS_INNER,
    )

    # stone_cnt2 stones+1 (extra room) + 1 capstone
    cmp_length_sm = (Stone.thk * (CaseS1.stone_cnt2 + 1)) + capstone_h
    stone_box_sm = Box(
        cmp_width,
        cmp_length_sm,
        cmp_height,
        cmp_wall,
        Box.DIMS_INNER,
    )

    # Stone1 / Compartment 1
    stone1_cmp1 = stone_box_lg.build()
    xoff = (case_box.width / 2) - (stone_box_lg.width * 2)
    yoff = (case_box.length - stone_box_lg.length) / 2
    case += stone1_cmp1.color("white").translate(xoff, yoff, 0)

    # Stone1 / Compartment 2
    stone1_cmp2 = stone_box_sm.build()
    xoff = (case_box.width / 2) - stone_box_sm.width - cmp_wall
    yoff = (case_box.length - stone_box_sm.length) / 2
    case += stone1_cmp2.color("white").translate(xoff, yoff, 0)

    # Stone2 / Compartment 1
    stone2_cmp1 = stone_box_lg.build()
    xoff = (case_box.width / 2) + stone_box_lg.width
    yoff = (case_box.length - stone_box_lg.length) / 2
    case += stone2_cmp1.color("grey").translate(xoff, yoff, 0)

    #  Stone2 / Compartment 2
    stone2_cmp2 = stone_box_sm.build()
    xoff = (case_box.width / 2) + cmp_wall
    yoff = (case_box.length - stone_box_sm.length) / 2
    case += stone2_cmp2.color("grey").translate(xoff, yoff, 0)

    return case


def __style2(opts):
    stone_padding = 2.5
    tray_size = CaseS2.wall_thk + Stone.width + stone_padding + CaseS2.wall_thk

    case = cube(CaseS2.width, CaseS2.length, CaseS2.height)

    center_cutout = cube(
        CaseS2.width - (tray_size * 2),
        CaseS2.length - (tray_size * 2),
        CaseS2.height + 2,
    )
    case -= center_cutout.right(tray_size).forward(tray_size).down(1)

    # corner posts with magnet cutouts
    mag_radius = Magnet.dia / 2
    for row in range(2):
        for col in range(2):
            x = CaseS2.width * col
            y = CaseS2.length * row

            # Magnet cutout
            magnet = cylinder(d=Magnet.dia, h=Magnet.thk + 0.25)
            magx_offset = mag_radius + Board.magnet_offset
            magx_offset *= -1 if col == 1 else 1
            mag_x = x + magx_offset

            magy_offset = mag_radius + Board.magnet_offset
            magy_offset *= -1 if row == 1 else 1
            mag_y = y + magy_offset

            # Post
            post = __post("s2")
            postx_offset = CasePost.width * col
            postx_offset *= -1 if col == 1 else 1
            post_x = x + postx_offset

            posty_offset = CasePost.length * row
            posty_offset *= -1 if row == 1 else 1
            post_y = y + posty_offset

            case = (
                case
                + post.translate(post_x, post_y, 0)
                - magnet.translate(
                    mag_x,
                    mag_y,
                    CaseS2.height - Magnet.thk,
                )
            )

    # cutouts/trays for stones
    tray_width = Stone.width + stone_padding

    # -> left
    tray_left = cube(
        tray_width,
        CaseS2.length - (CasePost.width * 2),
        Stone.height + CaseS2.wall_thk + 1,
    )
    case -= (
        tray_left.right(CaseS2.wall_thk).up(CaseS2.wall_thk).forward(CasePost.width)
    )

    # -> right
    tray_right = cube(
        tray_width,
        CaseS2.length - (CasePost.width * 2),
        Stone.height + CaseS2.wall_thk + 1,
    )
    case -= (
        tray_right.right(CaseS2.width - tray_size + CaseS2.wall_thk)
        .up(CaseS2.wall_thk)
        .forward(CasePost.width)
    )

    # -> top
    tray_top = cube(
        CaseS2.length - (CasePost.width * 2),
        tray_width,
        Stone.height + CaseS2.wall_thk + 1,
    )
    case -= (
        tray_top.forward(CaseS2.length - tray_size + CaseS2.wall_thk).right(CasePost.width).up(CaseS2.wall_thk)
    )

    # -> bottom
    tray_bottom = cube(
        CaseS2.length - (CasePost.width * 2),
        tray_width,
        Stone.height + CaseS2.wall_thk + 1,
    )
    case -= (
        tray_bottom.forward(CaseS2.wall_thk)
        .up(CaseS2.wall_thk)
        .right(CasePost.width)
    )

    return case


def build(opts):
    style = opts.get("style", "s1")

    case = None
    match style:
        case "s1":
            case = __style1(opts)
        case "s2":
            case = __style2(opts)

    return case
