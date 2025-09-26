from solid2 import *

from units import Bishop

def build():
    model = cylinder(d1=Bishop.width, d2=1, h=Bishop.height)
    return model
