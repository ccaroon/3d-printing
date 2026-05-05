from solid2 import *

from units import Tile


# TODO:
# * [ ] use Tile.build()
# * [ ] 1mm sunken grid over entire board
def build():
    model = cube(Tile.size * 5, Tile.size * 5, Tile.thk)

    return model
