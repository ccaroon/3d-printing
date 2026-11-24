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
        """A Flat Circular Platter/Plate with a Lip"""
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
    def magplate(self, **kwargs):
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

    @model
    def nameplate(self, **kwargs):
        """A Basic Nameplate"""

        # 1/16 of an inch border on W & L
        width = 3.0625 * units.inch
        length = 1.5625 * units.inch
        thickness = 1.0 * units.mm
        nameplate = self.plate(width=width, length=length, thickness=thickness)

        return nameplate

    @model
    def rplate(self, **kwargs):
        """A Flat Rectangular Plate"""
        width = units.parse_size(kwargs.get("width"))
        length = units.parse_size(kwargs.get("length"))
        thk = units.parse_size(kwargs.get("thk", "1mm"))

        plate = cube(width, length, thk)

        return plate

    @model
    def cplate(self, **kwargs):
        """A Flat Circular Plate"""
        dia = units.parse_size(kwargs.get("dia"))
        thk = units.parse_size(kwargs.get("thk", "1mm"))

        model = cylinder(d=dia, h=thk)

        return model

    @model
    def ring(self, **kwargs):
        """A circular frame with optional # sides"""
        dia = units.parse_size(kwargs.get("dia"))
        border = units.parse_size(kwargs.get("border"))
        sides = int(kwargs.get("sides", 0))
        thk = units.parse_size(kwargs.get("thk", "1mm"))

        sides = None if not sides else sides

        outer_ring = cylinder(d=dia, h=thk, _fn=sides)
        inner_ring = cylinder(d=dia - (border * 2), h=thk + 2, _fn=sides)

        model = outer_ring - inner_ring.down(1)

        return model

    @model
    def clock_ring(self, **kwargs):
        """A Ring with Markings at Major Clock Numbers"""
        dia = units.parse_size(kwargs.get("dia"))
        border = units.parse_size(kwargs.get("border"))
        thk = units.parse_size(kwargs.get("thk", "1mm"))

        main_ring = self.ring(**kwargs)

        size = border * 1.10
        marker = cube([size, size, thk]).left(size / 2).back(size / 2).rotate(45)

        model = main_ring

        # 12
        model += marker.forward((dia / 2) - (border / 2))
        # 3
        model += marker.right((dia / 2) - (border / 2))
        # 6
        model += marker.back((dia / 2) - (border / 2))
        # 9
        model += marker.left((dia / 2) - (border / 2))

        # 1
        model += marker.forward((dia / 2) - (border / 2)).rotateZ(-30)
        # 2
        model += marker.forward((dia / 2) - (border / 2)).rotateZ(-60)

        # 4
        model += marker.right((dia / 2) - (border / 2)).rotateZ(-30)
        # 5
        model += marker.right((dia / 2) - (border / 2)).rotateZ(-60)

        # 7
        model += marker.back((dia / 2) - (border / 2)).rotateZ(-30)
        # 8
        model += marker.back((dia / 2) - (border / 2)).rotateZ(-60)

        # 10
        model += marker.left((dia / 2) - (border / 2)).rotateZ(-30)
        # 11
        model += marker.left((dia / 2) - (border / 2)).rotateZ(-60)

        return model

    @model
    def frame(self, **kwargs):
        """A rectangular frame"""
        length = units.parse_size(kwargs.get("length"))
        width = units.parse_size(kwargs.get("width"))
        thk = units.parse_size(kwargs.get("thk", "1.0mm"))
        border = units.parse_size(kwargs.get("border"))

        outer_rect = cube(length, width, thk)
        inner_rect = cube(length - (border * 2), width - (border * 2), thk + 2)

        return outer_rect - inner_rect.right(border).forward(border).down(1)

    @model
    def seven_segment_tmpl(self, **kwargs):
        sg_len = units.parse_size(kwargs.get("length"))
        sg_width = units.parse_size(kwargs.get("width"))
        thk = units.parse_size(kwargs.get("thk", "1.0mm"))

        padding = sg_width * 0.85
        base_w = sg_len + (padding * 4)
        base_l = (sg_len * 2) + (padding * 4)

        tmpl_base = cube([base_w, base_l, thk])

        sg_h1 = sg_len
        sg_h2 = sg_len * 0.90
        segment_half = (
            polygon(
                [
                    [0, 0],
                    [0, sg_h1],
                    [(sg_width / 2), sg_h2],
                    [(sg_width / 2), sg_h1 - sg_h2],
                ]
            )
            .linear_extrude(height=thk + 2)
            .translate([0, -sg_h1 / 2, 0])
        )

        segment_cutout = segment_half + segment_half.rotateZ(180).right(0.001)

        model = tmpl_base

        # top / center
        model -= segment_cutout.rotateZ(-90).translate(
            [
                base_w / 2,
                base_l - (sg_width / 2) - padding,
                -1,
            ]
        )

        # top / left
        model -= segment_cutout.translate(
            [
                (sg_width / 2) + padding / 2,
                base_l - (sg_h1 / 2) - (sg_width / 2) - padding,
                -1,
            ]
        )

        # top / right
        model -= segment_cutout.translate(
            [
                base_w - (sg_width / 2) - padding / 2,
                base_l - (sg_h1 / 2) - (sg_width / 2) - padding,
                -1,
            ]
        )

        # center / center
        model -= segment_cutout.rotateZ(-90).translate(
            [
                base_w / 2,
                (base_l / 2),
                -1,
            ]
        )

        # bottom / center
        model -= segment_cutout.rotateZ(-90).translate(
            [
                base_w / 2,
                (sg_width / 2) + padding,
                -1,
            ]
        )

        # bottom / left
        model -= segment_cutout.translate(
            [
                (sg_width / 2) + padding / 2,
                (sg_h1 / 2) + (sg_width / 2) + padding,
                -1,
            ]
        )

        # bottom / right
        model -= segment_cutout.translate(
            [
                base_w - (sg_width / 2) - padding / 2,
                (sg_h1 / 2) + (sg_width / 2) + padding,
                -1,
            ]
        )

        blk_w = base_w * 0.70
        blk_l = base_l * 0.30
        blackout = cube([blk_w, blk_l, 3])

        # cutout some more "whitespace" so less to print
        model -= blackout.translate(
            [
                (base_w / 2) - (blk_w / 2),
                base_l / 2 - blk_l - sg_width - (padding * 2),
                -1,
            ]
        )

        model -= blackout.translate([(base_w / 2) - (blk_w / 2), base_l - blk_l - sg_width - (padding * 3), -1])

        return model
        # return segment_cutout

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
