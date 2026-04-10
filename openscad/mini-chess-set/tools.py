#!/usr/bin/env python
from solid2 import *

from units import Court, Pawn, Standard


def matt_ruler():
    """ Ruler 1/8in by 3in """
    return cube([3 * Standard.inch, 0.125 * Standard.inch, 2 * Standard.mm])


def felt_template(type):
    if type == "court":
        dia = Court.base_dia
    elif type == "pawn":
        dia = Pawn.base_dia
    else:
        raise ValueError(f"felt_template: Unknown Type: {type}")

    return cylinder(d=dia - 2, h=2)


MODELS = {
    "felt-template": felt_template,
    "matt-ruler": matt_ruler
}

def build(name, *args):
    builder = MODELS.get(name)
    if builder:
        model = builder(*args)
        return model
    else:
        print(f"==> Tools: Unknown tool '{name}' // {args}")
        print(f"Available Models: {list(MODELS.keys())}")
