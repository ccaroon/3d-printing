from solid2 import *

import tile_inset
from units import Board


def __base():
    base = cube(Board.size, Board.size, Board.thk)
    return base


def __border_insets():
    inset_len = (Board.tile.size * Board.tile_count) + (
        Board.inset.width * Board.ti_count
    )

    horizonal = cube(inset_len, Board.inset.width, Board.inset.thk + 1)
    for count in range(1, Board.ti_count):
        pos = (Board.tile.size + Board.inset.width) * count
        horizonal += cube(inset_len, Board.inset.width, Board.inset.thk + 1).forward(
            pos
        )

    vertical = cube(Board.inset.width, inset_len, Board.inset.thk + 1)
    for count in range(1, Board.ti_count):
        pos = (Board.tile.size + Board.inset.width) * count
        vertical += cube(Board.inset.width, inset_len, Board.inset.thk + 1).right(pos)

    inset = horizonal.right(Board.border.width).forward(
        Board.border.width
    ) + vertical.right(Board.border.width).forward(Board.border.width)

    return inset


def __tile_insets(style):
    extra_depth = Board.ti_s1.depth_offset
    insets = tile_inset.build(
        {"ex_h": extra_depth, "style": style}
    ).rotateY(180)

    for row in range(0, Board.ti_count):
        for col in range(0, Board.ti_count):
            # print(f"{row},{col}")
            col_offset = (Board.tile.size * col) + (Board.inset.width * col)
            row_offset = (Board.tile.size * row) + (Board.inset.width * row)
            insets += (
                tile_inset.build({"ex_h": extra_depth, "style": style})
                .rotateY(180)
                .right(col_offset)
                .forward(row_offset)
            )

    return insets


def __inset_test():
    tile = cube(Board.tile.size, Board.tile.size, Board.thk)

    inset_len = Board.tile.size + 2
    hor_border = (
        cube(inset_len, Board.inset.width, Board.inset.thk + 1)
        .forward((Board.tile.size / 2) - (Board.inset.width / 2))
        .left(1)
        .up(Board.thk - Board.inset.thk)
    )
    vert_border = (
        cube(Board.inset.width, inset_len, Board.inset.thk + 1)
        .right((Board.tile.size / 2) - (Board.inset.width / 2))
        .back(1)
        .up(Board.thk - Board.inset.thk)
    )
    borders = hor_border + vert_border

    inset = (
        tile_inset.build({"ex_h": Board.ti_s1.depth_offset})
        .rotateY(180)
        .right(Board.tile.size / 2)
        .forward(Board.tile.size / 2)
        .up(Board.thk + 0.10)
    )

    magnet_cutout = (
        cylinder(d=Board.magnet.dia, h=Board.magnet.thk + 0.5)
        .right(Board.tile.size / 2)
        .forward(Board.tile.size / 2)
    )

    model = tile - borders - inset - magnet_cutout.down(0.5)

    return model


def build(opts):
    style = opts.get("style", "s1")

    if opts.get("inset_test", False):
        piece = __inset_test()
    else:
        base = __base()
        border_insets = __border_insets()
        tile_insets = __tile_insets(style=style)

        ti_offset = Board.border.width + Board.inset.width / 2
        piece = (
            base
            - tile_insets.up(Board.thk + 0.10)
            .right(ti_offset)
            .forward(ti_offset)
            .color("#777777")
            - border_insets.up(Board.thk - Board.inset.thk)
        )

        # Magnet cut-out in each corner
        mag_radius = Board.magnet.dia / 2
        for row in range(2):
            for col in range(2):
                x = Board.size * col
                y = Board.size * row

                xoffset = mag_radius + Board.magnet_offset
                if col == 1:
                    xoffset *= -1
                x += xoffset

                yoffset = mag_radius + Board.magnet_offset
                if row == 1:
                    yoffset *= -1
                y += yoffset

                magnet_cutout = cylinder(d=Board.magnet.dia, h=Board.magnet.thk + 0.5)
                piece = piece - magnet_cutout.translate(x, y, -0.5)

    return piece
