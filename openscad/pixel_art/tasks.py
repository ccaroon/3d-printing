import importlib
from invoke import Collection, task

from solid2 import *

ADJUSTMENT = 0.25

# 1|X|.   = ON, no adjustment
# U|D|L|R =   ON, with .5mm adjustment in the indicated direction
STATE_ON = (
    1,  # No Adjustment
    "X",  # No Adjustment
    ".",  # No Adjustment
    # Direction Adjustments
    "U",  # Up
    "D",  # Down
    "L",  # Left
    "R",  # Right
)
STATE_OFF = (0, " ")


def pixel_art(pattern, size, **kwargs):
    """
    Args:
        pattern (dict): Must contain 'bitmap' & 'width' fields.
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

        state_code = state
        if isinstance(state, str):
            state_code = state[0]
            state_multi = 1
            if len(state) > 1 and state[1:].isdigit():
                state_multi = int(state[1:])
        if state_code in STATE_ON:
            pixel = cube(size).color("white").right(x * size).back(y * size)

            match state_code:
                case "U":
                    pixel = pixel.forward(ADJUSTMENT * state_multi)
                case "D":
                    pixel = pixel.back(ADJUSTMENT * state_multi)
                case "R":
                    pixel = pixel.right(ADJUSTMENT * state_multi)
                case "L":
                    pixel = pixel.left(ADJUSTMENT * state_multi)

            pixels.append(pixel)
        elif state in STATE_OFF and debug:
            pixel = cube(size).color("black").right(x * size).back(y * size)
            pixels.append(pixel)

    pixel_art = union()(pixels)

    return pixel_art


@task(
    help={
        "name": "The name of a pattern from the `patterns` directory; E.g. si_crab",
        "size": "Pixel size in millimeters.",
    }
)
def build(ctx, name, size=3, debug=False):
    try:
        module = importlib.import_module(f"patterns.{name}")
        pattern = module.PATTERN

        model = pixel_art(pattern, size, debug=debug)

        file_name = f"./models/{name}.scad"
        model.save_as_scad(file_name)
        print(f"=> Created '{pattern['desc']}' => {file_name}")
    except ModuleNotFoundError:
        print("Pattern not found. See the `patterns` directory for a list of patterns.")


ns = Collection()
