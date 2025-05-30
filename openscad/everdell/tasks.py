from invoke import task

from object_factory import EverdellObjectFactory as factory

@task
def build(ctx, model):
    """
    Build Everdell Model: bowl | twig | twig-rack
    """
    match model:
        case "bowl":
            object = factory.bowl()
        case "twig":
            object = factory.twig()
        case "twig-rack":
            object = factory.twig_rack()
        case _:
            raise ValueError(f"Unknown Model: '{model}'")

    out_file = f"./models/everdell-{model}.scad"
    object.save_as_scad(out_file)

    print(out_file)
