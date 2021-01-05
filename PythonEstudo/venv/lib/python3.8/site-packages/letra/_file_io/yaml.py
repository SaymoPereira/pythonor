from yaml import dump, load, FullLoader, YAMLError, Dumper
from letra import Label


def read(filepath):
    try:
        with open(filepath) as stream:
            return load(stream, Loader=FullLoader)
    except YAMLError:
        raise ValueError("Specified template file is not valid yaml")


def represent_label(dumper, data):
    return dumper.represent_mapping(
        u"tag:yaml.org,2002:map",
        {
            "name": data.name,
            "description": data.description,
            "color": data.color,
        },
    )


Dumper.add_representer(Label, represent_label)


def write(labels, filepath):
    with open(filepath, "w+") as stream:
        dump(labels, stream, Dumper=Dumper, sort_keys=False)
