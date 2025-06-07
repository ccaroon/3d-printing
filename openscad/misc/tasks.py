from invoke import task

import tools


@task
def build(ctx, model, opt=None):
    """ Build a Model """
    match model:
        case "tool":
            tools.build(opt)
        case _:
            print(f"==> Unknown model: '{model}'")
