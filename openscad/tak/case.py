from solid2 import *

from lib.box import Box
from units import Board, CapStone, Case, Magnet, Stone


def __post():
    post = cube(Case.post.width, Case.post.length, Case.height)
    # magnet = cylinder(d=Magnet.dia, h=Magnet.thk+1)

    # offset = (Magnet.dia / 2) + Board.magnet_offset

    return post  # - magnet.translate(offset, offset, Case.height - Magnet.thk)


def build(opts):
    # overall box
    base_box = Box(
        Case.width,
        Case.length,
        Case.height,
        Case.wall_thk,
        Box.DIMS_OUTER,
    )
    base = base_box.build()

    # corner posts with magnet cutouts
    mag_radius = Magnet.dia / 2
    for row in range(2):
        for col in range(2):
            x = Case.width * col
            y = Case.length * row

            # Magnet cutout
            magnet = cylinder(d=Magnet.dia, h=Magnet.thk + 1)
            magx_offset = mag_radius + Board.magnet_offset
            magx_offset *= -1 if col == 1 else 1
            mag_x = x + magx_offset

            magy_offset = mag_radius + Board.magnet_offset
            magy_offset *= -1 if row == 1 else 1
            mag_y = y + magy_offset

            # Post
            post = __post()
            postx_offset = Case.post.width * col
            postx_offset *= -1 if col == 1 else 1
            post_x = x + postx_offset

            posty_offset = Case.post.length * row
            posty_offset *= -1 if row == 1 else 1
            post_y = y + posty_offset

            base = (
                base
                + post.translate(post_x, post_y, 0)
                - magnet.translate(
                    mag_x,
                    mag_y,
                    Case.height - Magnet.thk,
                )
            )

    # Stone Compartment
    ## Sizes
    capstone_h = CapStone.base_h + CapStone.mid_height + CapStone.top_dia
    cmp_width = Stone.height + 5
    cmp_length = Stone.thk * 25  # hold 25 stones
    cmp_height = Case.height
    cmp_wall = Case.wall_thk / 2

    stone_box_lg = Box(cmp_width, cmp_length, cmp_height, cmp_wall, Box.DIMS_INNER)

    cmp_length_sm = (Stone.thk * 5) + capstone_h  # 5 stones + 1 capstone
    stone_box_sm = Box(cmp_width, cmp_length_sm, cmp_height, cmp_wall)

    # Stone1 / Compartment 1
    stone1_cmp1 = stone_box_lg.build()
    xoff = Case.post.width
    yoff = (base_box.length - stone_box_lg.length) / 2
    base += stone1_cmp1.color("white").translate(xoff, yoff, 0)

    # Stone1 / Compartment 2
    stone1_cmp2 = stone_box_sm.build()
    xoff = Case.post.width + stone_box_lg.width - cmp_wall
    yoff = (base_box.length - stone_box_sm.length) / 2
    base += stone1_cmp2.color("white").translate(xoff, yoff, 0)

    # Stone2 / Compartment 1
    stone2_cmp1 = stone_box_lg.build()
    xoff = Case.post.width + stone_box_lg.width + (stone_box_sm.width * 2) - (cmp_wall * 3)
    yoff = (base_box.length - stone_box_lg.length) / 2
    base += stone2_cmp1.color("black").translate(xoff, yoff, 0)

    #  Stone2 / Compartment 2
    stone2_cmp2 = stone_box_sm.build()
    xoff = Case.post.width + stone_box_lg.width + stone_box_sm.width - (cmp_wall * 2)
    yoff = (base_box.length - stone_box_sm.length) / 2
    base += stone2_cmp2.color("black").translate(xoff, yoff, 0)

    piece = base

    return piece
