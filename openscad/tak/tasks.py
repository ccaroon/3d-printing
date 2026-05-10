from invoke import task
from solid2 import *

import board
import tile_inset
import stone1
import stone2
import cap_stone1
import cap_stone2


@task(iterable=["opts"])
def build(ctx, piece, opts=None):
    """
    Build the named tak piece.

    :param piece: The name of the tak piece to build.
    :param opt: Piece specific option.
    """
    set_global_fn(150)

    model = None
    match piece:
        case "stone1":
            model = stone1.build()
        case "cap-stone1":
            model = cap_stone1.build()
        case "stone2":
            model = stone2.build()
        case "cap-stone2":
            model = cap_stone2.build()
        case "tile-inset":
            model = tile_inset.build()
        case "board":
            model = board.build()
        case _:
            print(f"Unknown piece: '{piece}'")

    if model:
        base_name = f"tak-{piece}"
        if opts:
            opts_sfx = "-".join(opts)
            base_name += f"-{opts_sfx}"

        file_name = f"./models/{base_name}.scad"
        model.save_as_scad(file_name)
        print(f"=> {file_name}")


@task
def clean(ctx):
    """Clean up generated files"""
    ctx.run("rm -f *.stl")
    ctx.run("rm -rf __pycache__")
