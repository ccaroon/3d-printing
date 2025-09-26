from solid2 import *

from units import Pawn

def build():
    model = cube(Pawn.width, Pawn.width, Pawn.width)
    return model
