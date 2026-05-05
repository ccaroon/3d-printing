from solid2 import *

from units import Tile


def build():
    model = cube(Tile.size, Tile.size, Tile.thk)
    model = model.translate(-Tile.size / 2, -Tile.size / 2, 0)

    return model
