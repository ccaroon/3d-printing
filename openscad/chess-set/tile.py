from solid2 import *

from units import Magnet,Tile

def build():
    model = cube(Tile.size, Tile.size, Tile.thk)
    model = model.translate(-Tile.size/2, -Tile.size/2, 0)

    cut_out = cylinder(d=Magnet.dia, h=Magnet.thk + 1)

    return model - cut_out.up(Tile.thk - Magnet.thk)
