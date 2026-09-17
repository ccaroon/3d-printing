from solid2 import *

from lib import units

# ruff: noqa: F405

set_global_fn(150)

# A decorator to track model names and descriptions
MODELS = {}


def model(func):
    MODELS[func.__name__] = func.__doc__

    def wrapper(self, **kwargs):
        return func(self, **kwargs)

    return wrapper


class Factory:
    @model
    def water_bulb(self, **kwargs):
        """A Small(ish) Water Bulb to water plants"""
        # sizes
        wall_thickness = 2 * units.mm

        if kwargs.get("test", False):
            bulb_size = 1.0 * units.inch
            tube_size = 0.75 * units.cm
            tube_len = 1.0 * units.inch
        else:
            bulb_size = 3 * units.inch
            tube_size = 1.25 * units.cm
            tube_len = 4 * units.inch

        # bulb
        bulb_out = sphere(d=bulb_size)
        bulb_in = sphere(d=bulb_size - wall_thickness)
        hole = cylinder(d=tube_size, h=wall_thickness)
        bulb = (bulb_out - bulb_in) - hole.up((bulb_size / 2) - 2)

        # tube
        tube_offset = 6
        tube_out = cylinder(d1=tube_size, d2=tube_size * 0.75, h=tube_len)
        tube_in = cylinder(
            d1=(tube_size) - wall_thickness,
            d2=(tube_size * 0.75) - wall_thickness,
            h=(tube_len) + tube_offset,
        )

        tube = tube_out - tube_in.down(tube_offset / 2)

        return bulb + tube.up((bulb_size / 2) - wall_thickness)

    @model
    def hollow_cube(self, **kwargs):
        """A Hollow Cube of `size` with `walls=1` thick walls"""
        size = float(kwargs.get("size"))
        walls = kwargs.get("walls", 1)

        model = None
        if size and walls:
            outer_cube = cube([size, size, size])
            inner_cube = cube([size - (walls * 2), size - (walls * 2), size - (walls * 2)])

            model = outer_cube - inner_cube.translate([walls, walls, walls])
        else:
            raise ValueError("Must specify `size`")

        return model

    @model
    def color_cube(self, **kwargs):
        """A 1in Cube; used to print filament color samples"""
        return self.hollow_cube(size=1 * units.inch, walls=1)

    @model
    def hollow_cylinder(self, **kwargs):
        """A Hollow Cylinder of `dia` & `height` with `walls=1` thick walls"""
        dia = float(kwargs.get("dia"))
        height = float(kwargs.get("height"))
        walls = kwargs.get("walls", 1)

        model = None
        if dia and height and walls:
            outer = cylinder(d=dia, h=height, center=True)
            inner = cylinder(d=dia - walls, h=height - (walls * 2), center=True)

            model = outer - inner
        else:
            raise ValueError("Must specify `dia` & `height`")

        return model

    @model
    def column_foot(self, **kwargs):
        """A Cylindrial Foot"""
        width = float(kwargs.get("width", 1 * units.inch))
        height = float(kwargs.get("height", 1.5 * units.inch))

        foot = cylinder(d1=width, d2=width * 0.75, h=height)

        return foot

    @model
    def platter(self, **kwargs):
        """A Flat Platter"""
        lip = 2
        dia = float(kwargs.get("dia", 11.5 * units.cm))
        height = float(kwargs.get("height", 5 * units.mm))

        platter = cylinder(d=dia, h=height)
        cutout = cylinder(d=dia - (lip * 2), h=height)

        return platter - cutout.up(2)

    @model
    def tube(self, **kwargs):
        """Hollow Tube. Bottom with optional lip. No Top."""
        dia = kwargs.get("dia", 10)
        lip_size = kwargs.get("lip", 0)
        wall = kwargs.get("wall", 1)
        length = kwargs.get("len", 20)

        bottom_dia = dia + (lip_size * 2)
        bottom = cylinder(d=bottom_dia, h=wall)

        outer = cylinder(d=dia, h=length).color("red")
        inner = cylinder(d=dia - (wall * 2), h=length + 1)
        tube = outer - inner.down(0.5)

        model = bottom + tube.up(wall)

        return model

    @model
    def nameplate(self, **kwargs):
        """A Magnetic Nameplate with Back"""

        # Nameplate
        # 1/16 of an inch border
        width = 3.0625 * units.inch
        length = 1.5625 * units.inch
        thickness = 1.5 * units.mm
        nameplate = cube(width, length, thickness)

        # Cutout for Magnet
        mag_dia = 10.25  # with padding
        mag_thk = 1
        mag_cutout = cylinder(d=mag_dia, h=mag_thk * 2)

        # Nameplate Cutout
        x = width / 6
        y = length / 2
        z = thickness - mag_thk
        nameplate = nameplate - mag_cutout.translate(x, y, z)
        nameplate = nameplate - mag_cutout.translate(width - x, y, z)

        # Backing
        offset = 5
        mag_border = 4
        backplate = cube(width, mag_dia + mag_border, thickness)
        y = offset + (mag_border / 2)
        backplate = backplate - mag_cutout.translate(x, y, z)
        backplate = backplate - mag_cutout.translate(width - x, y, z)

        model = nameplate + backplate.forward(length + offset)

        return model

    @classmethod
    def list_models(cls):
        return MODELS

    def build(cls, name, **kwargs):
        """
        Build a Model
        """
        model = None
        try:
            if name in MODELS:
                builder = getattr(cls, name)
                model = builder(**kwargs)
        except AttributeError as err:
            print(err)
            model = None

        return model
