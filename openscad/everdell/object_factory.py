import random

from solid2 import *
set_global_fn(150)

from lib import units

class EverdellObjectFactory:
    # Resource Bowl
    BOWL_CUTOUT_DIA = 5.5 * units.cm
    BOWL_CUTOUT_ADJ = 3.0 * units.cm
    BOWL_ROUNDING = 0.5 * units.cm
    BOWL_BOT_DIA = 2.00 * units.cm
    BOWL_TOP_DIA = 2.85 * units.cm
    BOWL_HEIGHT = 3.0 * units.cm

    # Twig & Twig Rack
    TWIG_DIA = 8 * units.mm
    TWIG_LEN = 22 * units.mm
    TWIG_OVLP = 0.40 * units.mm
    TWIG_RACK_WIDTH = TWIG_LEN + 4

    # TODO:
    # [x] Insert 1 more log to length (total 11)
    # [x] Use a matrix/pattern for rows/cols instead of range(10) with skips
    # [ ] Consistent "random" log rotation so get same results all the time.
    @classmethod
    def twig_rack(cls):
        """
        Built from individual twigs
        """

        pattern = [
            ['O',' ',' ',' ',' ',' ',' ',' ',' ',' ','O'],
            ['O',' ',' ',' ',' ',' ',' ',' ',' ',' ','O'],
            ['O','O',' ',' ',' ',' ',' ',' ',' ','O','O'],
            ['O','O','O',' ',' ',' ',' ',' ','O','O','O'],
            ['O','O','O','O','O','O','O','O','O','O','O'],
        ]
        # To model bottom layer first
        pattern.reverse()

        twig_opts = {
            "length": cls.TWIG_RACK_WIDTH,
            "aidx": 0
        }
        layers = []

        for ridx, row in enumerate(pattern):
            layer = cls.twig(**twig_opts)
            for cidx, col in enumerate(row):
                twig_opts["aidx"] = ridx + cidx + 7
                if col == "O":
                    layer += cls.twig(**twig_opts).right(
                        cidx * (cls.TWIG_DIA - cls.TWIG_OVLP)
                    )
            layers.append(layer)

        # build rack
        rack = layers.pop(0)
        for idx, layer in enumerate(layers):
            rack += layer.forward(
                (cls.TWIG_DIA - cls.TWIG_OVLP) * (idx + 1)
            )

        return rack


    @classmethod
    def twig(cls, **kwargs):
        """
        A Single Twig

        KWArgs:
            aidx (int): Angle Index for rotation. Default: 0
            length (int): Length of the twig. Defaut: TWIG_LEN
        """
        # The imported object is NOT centered in middle of the SVG, but
        # instead is centered at 0,0.
        # Therefore, rotating the object causes it to move around the 0,0 coord.
        # So, after rotation we have to move the object back to 0,0
        angles = (
            # (angle, [translation])
            (0,   [0, 0, 0]),
            (45,  [4.5, -2.5, 0]),
            (90,  [8.6, 0, 0]),
            (135, [10.39, 4.5 ,0]),
            (180, [8.8, 8.6, 0]),
            (225, [4.5, 10.39, 0]),
            (270, [0, 8.8, 0]),
            (315, [-2.5, 4.4, 0])
        )

        length = kwargs.get("length", cls.TWIG_LEN)

        twig = import_(file="../resources/twig.svg").linear_extrude(
            # center=True,
            height=length
        )

        aidx = kwargs.get("aidx", 0)
        aidx %= len(angles)
        rotation = angles[aidx]
        # angle = random.choice(list(rotation.keys()))
        angle = rotation[0]
        xlate = rotation[1]
        twig = twig.rotate(angle).translate(xlate)

        return twig

    @classmethod
    def bowl(cls):
        """
        Bowl - Can be used to store supply resources or by individual players
               to store their collected resources.
        """
        cutout = sphere(d=cls.BOWL_CUTOUT_DIA)
        rounder = sphere(d=cls.BOWL_ROUNDING)
        bowl = cylinder(
            r1=cls.BOWL_BOT_DIA, r2=cls.BOWL_TOP_DIA, h=cls.BOWL_HEIGHT)

        round_bowl = minkowski()(rounder, bowl)

        return round_bowl - cutout.up(cls.BOWL_CUTOUT_ADJ)
