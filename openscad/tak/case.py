from solid2 import *

from units import Board, CapStone, Case, Magnet, Stone


def __box(width, length, height, wall_thk):
    box = cube(width, length, height)
    cutout = cube(width - (wall_thk * 2), length - (wall_thk * 2), height)

    return box - cutout.translate(wall_thk, wall_thk, wall_thk)


def __post():
    post = cube(Case.post.width, Case.post.length, Case.height)
    # magnet = cylinder(d=Magnet.dia, h=Magnet.thk+1)

    # offset = (Magnet.dia / 2) + Board.magnet_offset

    return post  # - magnet.translate(offset, offset, Case.height - Magnet.thk)


def build(opts):
    # overall box
    base = __box(Case.width, Case.length, Case.height, Case.wall_thk)

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

    # stone1 compartment
    cmp_wall = Case.wall_thk / 2
    cmp_width = Stone.height + (cmp_wall * 2) + 5
    # based on number of stones to fit in compartment
    cmp_length = (Stone.thk * 25) + (cmp_wall * 2)
    stone1_cmp1 = __box(
        cmp_width,
        cmp_length,
        Case.height,
        cmp_wall,
    )

    left_over_space = Case.length - (Case.wall_thk * 2) - (Stone.thk * 25)
    cmp_offset = (Case.wall_thk + left_over_space) / 2
    base += stone1_cmp1.color("white").right(Case.post.width).forward(cmp_offset)

    # stone1 1/2 compartment
    capstone_height = CapStone.base_h + CapStone.mid_height + CapStone.top_dia
    cmp2_length = (Stone.thk * 5) + (capstone_height) + (cmp_wall * 2)
    stone1_cmp2 = __box(
        cmp_width,
        cmp2_length,
        Case.height,
        cmp_wall
    )
    base += stone1_cmp2.color("white").right(Case.post.width + cmp_width - cmp_wall).forward(cmp_offset)

    # TODO: stone2 box

    # TODO: stone2 1/2 box
    stone2_cmp2 = __box(
        cmp_width,
        cmp2_length,
        Case.height,
        cmp_wall
    )
    base += stone2_cmp2.color("black").right(Case.post.width + cmp_width - cmp_wall).forward(cmp_offset + cmp2_length - cmp_wall)

    piece = base

    return piece
