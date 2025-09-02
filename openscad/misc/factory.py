from solid2 import *

import lib.units as units

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
        """ A Small(ish) Water Bulb to water plants """
        # sizes
        wall_thickness = 2 * units.mm

        if kwargs.get("test", False):
            bulb_size = 1.0 * units.inch
            tube_size = 0.75 * units.cm
            tube_len  = 1.0 * units.inch
        else:
            bulb_size = 3 * units.inch
            tube_size = 1.25 * units.cm
            tube_len  = 4 * units.inch

        # bulb
        bulb_out = sphere(d=bulb_size)
        bulb_in  = sphere(d=bulb_size-wall_thickness)
        hole = cylinder(d=tube_size, h=wall_thickness)
        bulb = (bulb_out - bulb_in) - hole.up((bulb_size/2)-2)

        # tube
        tube_offset = 6
        tube_out = cylinder(d1=tube_size, d2=tube_size*.75, h=tube_len)
        tube_in  = cylinder(
            d1=(tube_size)-wall_thickness,
            d2=(tube_size*.75)-wall_thickness,
            h=(tube_len)+tube_offset
        )

        tube = tube_out - tube_in.down(tube_offset/2)

        return bulb + tube.up((bulb_size/2) - wall_thickness)


    @model
    def hollow_cube(self, **kwargs):
        """ A Hollow Cube of `size` with `walls=1` thick walls """
        size = kwargs.get("size")
        walls = kwargs.get("walls", 1)

        model = None
        if size and walls:
            outer_cube = cube([size,size,size])
            inner_cube = cube([
                size - (walls*2),
                size - (walls*2),
                size - (walls*2)
            ])

            model = outer_cube - inner_cube.translate([walls,walls,walls])
        else:
            raise ValueError("Must specify `size`")

        return model


    @model
    def color_cube(self, **kwargs):
        """ A 1in Cube; used to print filament color samples """
        return self.hollow_cube(size=1 * units.inch, walls=1)


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
