from invoke import task

import tools
import lib.things as things


@task
def build(ctx, model, opt=None):
    """ Build a Model """
    match model:
        case "tool":
            tools.build(opt)
        case "cube":
            size = int(opt) if opt else 10
            model = things.cube(size)
            model.save_as_scad(f"./models/solid-cube-{size}.scad")
        case _:
            print(f"==> Unknown model: '{model}' Try: tool | cube")
