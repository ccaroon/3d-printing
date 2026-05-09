from solid2 import *

from units import Board

TILE_COUNT = 5
INSET_COUNT = TILE_COUNT + 1

def __base():
    height = (
        (Board.tile.size * TILE_COUNT) +
        (Board.inset.width * INSET_COUNT) +
        (Board.border.width * 2)
    )
    width = height

    # print(f"Board Size: {width}x{height}")

    base = cube(width, height, Board.thk)
    return base


def __inset():
    inset_len = (
        (Board.tile.size * TILE_COUNT) +
        (Board.inset.width * INSET_COUNT)
    )

    horizonal = cube(inset_len, Board.inset.width, Board.inset.thk+1)
    for count in range(1, INSET_COUNT):
        pos = (Board.tile.size + Board.inset.width) * count
        horizonal += cube(inset_len, Board.inset.width, Board.inset.thk+1).forward(pos)

    vertical = cube(Board.inset.width, inset_len, Board.inset.thk+1)
    for count in range(1, INSET_COUNT):
        pos = (Board.tile.size + Board.inset.width) * count
        vertical += cube(Board.inset.width, inset_len, Board.inset.thk+1).right(pos)

    inset = (
        horizonal.right(Board.border.width).forward(Board.border.width) +
        vertical.right(Board.border.width).forward(Board.border.width)
    )

    return inset


def build():
    base = __base()
    inset = __inset()

    piece = base - inset.up(Board.thk-Board.inset.thk)

    return piece
