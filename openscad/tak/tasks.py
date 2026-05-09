from invoke import task
from solid2 import *

import board
import cap_stone_1
import tile_inset


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
        case "stone-1":
            print(f"-> {piece} ... not yet implemented!")
        case "cap-stone-1":
            model = cap_stone_1.build()
        case "stone-2":
            print(f"-> {piece} ... not yet implemented!")
        case "cap-stone-2":
            print(f"-> {piece} ... not yet implemented!")
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
