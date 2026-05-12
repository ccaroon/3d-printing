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

    build_opts = {}
    for option in opts:
        key, value = option.split("=",1)
        build_opts[key] = value

    model = None
    match piece:
        case "stone1":
            model = stone1.build(build_opts)
        case "capstone1":
            model = cap_stone1.build(build_opts)
        case "stone2":
            model = stone2.build(build_opts)
        case "capstone2":
            model = cap_stone2.build(build_opts)
        case "tile-inset":
            model = tile_inset.build(build_opts)
        case "board":
            model = board.build(build_opts)
        case _:
            print(f"Unknown piece: '{piece}'")

    if model:
        base_name = f"tak-{piece}"
        # if opts:
        #     opts_sfx = "-".join(opts)
        #     base_name += f"-{opts_sfx}"

        file_name = f"./models/{base_name}.scad"
        model.save_as_scad(file_name)
        print(f"=> {file_name}")


@task
def clean(ctx):
    """Clean up generated files"""
    ctx.run("rm -f *.stl")
    ctx.run("rm -rf __pycache__")
