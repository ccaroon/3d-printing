from solid2 import *
from invoke import task

from .factory import Factory

WALL = 1
BAND_DIA = 68.5
IO_WIDTH = 27.5
ROTOR_WIDTH = 45
REFLECTOR_WIDTH = 38
# I/O + Rotor x 3 + Reflector + Padding
TUBE_LEN = IO_WIDTH + (ROTOR_WIDTH * 3) + REFLECTOR_WIDTH + 2
# Inner dims of the bands - some padding/spacing
TUBE_DIA = BAND_DIA - WALL - WALL - 0.10


@task
def band(ctx, width, name=None):
    """Band of the given width"""
    width = int(width)

    outer = cylinder(d=BAND_DIA, h=width)
    inner = cylinder(d=BAND_DIA - (WALL * 2), h=width + 2)

    band = outer - inner.down(1)

    model_name = None
    if not name:
        model_name = f"band-{width}"
    else:
        model_name = f"{name}-band"

    __save(band, model_name)


@task
def all_bands(ctx):
    """Create all Tube Bands: IO, Rotor, Reflector"""
    band(ctx, IO_WIDTH, "io")
    band(ctx, ROTOR_WIDTH, "rotor")
    band(ctx, REFLECTOR_WIDTH, "reflect")


@task
def tube(ctx):
    """
    Tube for Paper Enigma...

    ...printed on US Letter

    http://wiki.franklinheath.co.uk/index.php/Enigma/Paper_Enigma
    """
    factory = Factory()

    # Tube with fixed end cap/bottom
    lip = 2
    tube_dia = TUBE_DIA
    tube_len = TUBE_LEN
    # ..FOR TESTING...
    tube_len = 10

    tube = factory.tube(
        dia=tube_dia,
        len=tube_len,
        lip=lip,
        wall=WALL,
    )

    # Removable end cap
    scale = 0.075
    cap_len = tube_len * scale
    if cap_len < 3:
        cap_len = 3

    if cap_len > 10:
        cap_len = 10

    cap = factory.tube(
        dia=tube_dia - (WALL * 2),
        len=cap_len,
        lip=lip + WALL,
        wall=WALL,
    )

    # model = tube
    model = tube + cap.right(tube_dia + 10)

    __save(model, "tube")


def __save(model, name):
    filename = f"./models/enigma-{name}.scad"
    model.save_as_scad(filename)
    print(f"=> {filename}")
