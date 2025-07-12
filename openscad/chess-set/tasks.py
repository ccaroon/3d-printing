from invoke import task
from solid2 import *

import bishop
import king
import knight
import pawn
import queen
import rook
import test
import tile
import tools

@task(iterable=['opts'])
def build(ctx, piece, opts=None):
    """
    Build the named chess piece.

    :param piece: The name of the chess piece to build.
    :param opt: Piece specific option.
    """
    set_global_fn(150)

    model = None
    match piece:
        case "pawn":
            model = pawn.build()
        case "queen":
            model = queen.build()
        case "king":
            model = king.build()
        case "knight":
            model = knight.build()
        case "bishop":
            model = bishop.build()
        case "rook":
            model = rook.build()
        case "tile":
            model = tile.build()
        case "tool":
            model = tools.build(*opts)
        case "test":
            model = test.build(opts)
        case _:
            print(f"Unknown piece: '{piece}'")

    if model:
        base_name = f"chess-{piece}"
        if opts:
            opts_sfx = "-".join(opts)
            base_name += f"-{opts_sfx}"

        file_name = f"./models/{base_name}.scad"
        model.save_as_scad(file_name)
        print(f"=> {file_name}")

@task
def clean(ctx):
    """ Clean up generated files"""
    ctx.run("rm -f *.stl")
    ctx.run("rm -rf __pycache__")
