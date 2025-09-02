import re
from invoke import task

from factory import Factory

@task(iterable=["options"])
def build(ctx, name, options=[]):
    """
    Build the named Model.

    :param name: The name of the component.
    :param options: Comp. specific options in KEY=VALUE format.
    """
    factory = Factory()

    kwargs = {}
    for opt in options:
        if "=" in opt:
            (key, value) = opt.split("=", 2)
            kwargs[key] = value
        else:
            kwargs[opt] = True

    model = factory.build(name, **kwargs)

    if model:
        base_name = name
        if options:
            opts_sfx = "-".join(options)
            opts_sfx = re.sub(r"\W", "-", opts_sfx)
            base_name += f"-{opts_sfx}"

        file_name = f"./models/{base_name}.scad"
        model.save_as_scad(file_name)
        print(f"=> {file_name}")
    else:
        print(f"=> Unknown model: {name}")


@task
def list_models(ctx):
    models = Factory.list_models()
    for name, desc in models.items():
        print(f"* {name} - {desc}")


@task
def clean(ctx):
    """ Clean up generated files"""
    with ctx.cd("models"):
        ctx.run("rm -f *.stl")
