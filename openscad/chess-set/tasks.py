from invoke import task
from solid2 import *

import common
import king
import pawn
import queen
import tile


@task
def build(ctx, piece):
    """
    Build the named chess piece.

    :param piece: The name of the chess piece to build.
    """
    set_global_fn(150)

    model = None
    # --- Pawns ---
    if piece == "pawn":
        model = pawn.build()
    # --- Queen ---
    elif piece == "queen":
        model = queen.build()
    # --- King ---
    elif piece == "king":
        model = king.build()
    # --- Tiles ---
    elif piece == "tile":
        model = tile.build()
    elif piece == "common":
        model = common.build()
    else:
        print(f"Unknown piece: '{piece}'")

    if model:
        file_name = f"./{piece}.scad"
        model.save_as_scad(file_name)
        print(f"=> {file_name}")

@task
def clean(ctx):
    """ Clean up generated files"""
    ctx.run("rm -f *.stl")
    ctx.run("rm -rf __pycache__")
