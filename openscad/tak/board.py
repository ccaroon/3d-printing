from solid2 import *

import tile_inset
from units import Board


def __base():
    height = (
        (Board.tile.size * Board.tile_count) +
        (Board.inset.width * Board.inset_count) +
        (Board.border.width * 2)
    )
    width = height

    # print(f"Board Size: {width}x{height}")

    base = cube(width, height, Board.thk)
    return base


def __border_insets():
    inset_len = (
        (Board.tile.size * Board.tile_count) +
        (Board.inset.width * Board.inset_count)
    )

    horizonal = cube(inset_len, Board.inset.width, Board.inset.thk+1)
    for count in range(1, Board.inset_count):
        pos = (Board.tile.size + Board.inset.width) * count
        horizonal += cube(inset_len, Board.inset.width, Board.inset.thk+1).forward(pos)

    vertical = cube(Board.inset.width, inset_len, Board.inset.thk+1)
    for count in range(1, Board.inset_count):
        pos = (Board.tile.size + Board.inset.width) * count
        vertical += cube(Board.inset.width, inset_len, Board.inset.thk+1).right(pos)

    inset = (
        horizonal.right(Board.border.width).forward(Board.border.width) +
        vertical.right(Board.border.width).forward(Board.border.width)
    )

    return inset

def __tile_insets():
    insets = tile_inset.tile_inset()

    ti_offset = Board.tile.size + Board.inset.width/2

    for row in range(0,Board.inset_count):
        for col in range(0,Board.inset_count):
            # print(f"{row},{col}")
            col_offset = (Board.tile.size * col) + (Board.inset.width * col)
            row_offset = (Board.tile.size * row) + (Board.inset.width * row)
            insets += tile_inset.tile_inset().right(col_offset).forward(row_offset)

    return insets


def build():
    base = __base()
    border_insets = __border_insets()
    tile_insets = __tile_insets()

    ti_offset = Board.border.width + Board.inset.width/2
    piece = (
        base -
        border_insets.up(Board.thk-Board.inset.thk) -
        tile_insets.up(Board.thk - (Board.inset.thk)).right(ti_offset).forward(ti_offset).debug()
    )
    return piece
