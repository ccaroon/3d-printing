from solid2 import *

from units import magnet,tile

def build():
    model = cube(tile.size, tile.size, tile.thk)
    model = model.translate(-tile.size/2, -tile.size/2, 0)

    cut_out = cylinder(d=magnet.dia, h=magnet.thk + 1)

    return model - cut_out.up(tile.thk - magnet.thk)
