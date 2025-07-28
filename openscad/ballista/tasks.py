from invoke import task

import parts

@task(iterable=['opts'])
def build(ctx, name, opts=None):
    """
    Build the named Ballista part.

    :param name: The name of the part.
    :param opt: Part specific options.
    """
    model = parts.build(name, opts)
    if model:
        base_name = f"ballista-p{name}"
        if opts:
            opts_sfx = "-".join(opts)
            base_name += f"-{opts_sfx}"

        file_name = f"./models/{base_name}.scad"
        model.save_as_scad(file_name)
        print(f"=> {file_name}")

@task
def clean(ctx):
    """ Clean up generated files"""
    ctx.run("rm -f *.stl")
    ctx.run("rm -rf __pycache__")
