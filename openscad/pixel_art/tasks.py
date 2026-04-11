import importlib
from invoke import Collection, task

from solid2 import *


def pixel_art(pattern, size, **kwargs):
    """
    Args:
        pattern (dict): With 'width', 'height' & 'bitmap' fields.
        size (float): The size of each 'pixel' in mm.

    KWArgs:
        debug (bool): Draw "empty" / "background" pixels in black
    """
    debug = kwargs.get("debug", False)

    width = pattern["width"]
    bitmap = pattern["bitmap"]
    pixels = []
    for idx, state in enumerate(bitmap):
        x = idx % width
        y = idx // width

        if state == 1:
            pixel = cube(size).color("white").right(x * size).back(y * size)
            pixels.append(pixel)
        elif debug:
            pixel = cube(size).color("black").right(x * size).back(y * size)
            pixels.append(pixel)

    pixel_art = union()(pixels)

    return pixel_art


@task(
    help={
        "pattern": "A Pattern from the `patterns` directory.",
        "size": "Pixel size in millimeters.",
    }
)
def build(ctx, pattern, size=2, debug=False):
    try:
        module = importlib.import_module(f"patterns.{pattern}")
        ptr_data = module.PATTERN

        model = pixel_art(ptr_data, size, debug=debug)

        file_name = f"./models/{pattern}.scad"
        model.save_as_scad(file_name)
        print(f"=> {file_name}")
    except ModuleNotFoundError:
        print("Pattern not found. See the `patterns` directory for a list of patterns.")


ns = Collection()
