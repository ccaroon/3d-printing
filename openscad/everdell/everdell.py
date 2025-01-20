#!/usr/bin/env python
import argparse

from object_factory import EverdellObjectFactory as factory

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Everdell Models")

    parser.add_argument("object", choices=("bowl", "twig", "twig_rack"))

    args = parser.parse_args()

    model = None
    notes = []
    match args.object:
        case "bowl":
            model = factory.bowl()
            notes.append("* Slicer => Bed X: ?? | Bed Y: ??")
        case "twig":
            model = factory.twig()
        case "twig_rack":
            model = factory.twig_rack()
            notes.append("Slicer -> Bed X: 4 | Bed Y: 6")
        case _:
            raise ValueError(f"Unknown Model: '{args.object}'")

    out_file = f"./models/{args.object}.scad"
    model.save_as_scad(out_file)
    print(f"--- {args.object} | {out_file} ---")

    for note in notes:
        print(f"=> {note}")
