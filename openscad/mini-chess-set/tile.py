from solid2 import *

from units import Tile

def build():
    model = cube(Tile.width, Tile.width, Tile.thk)
    return model
