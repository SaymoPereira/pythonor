from .yaml import read as read_yaml, write as write_yaml
from . import TemplateFileFormat
from os import getcwd
from os.path import abspath, join, exists as path_exists
from string import Template


def get_path_for_read(filepath):
    if path_exists(filepath):
        return filepath
    else:
        path = abspath(join(getcwd(), filepath))
        if path_exists(path):
            return path
        else:
            raise ValueError(
                "Specified template file not found.\n"
                f"Checked relative path: '{filepath}' "
                f"and absolute path: '{path}'"
            )


def get_path_for_write(filepath):
    if not filepath:
        raise ValueError("Invalid filepath specified")

    if filepath[0] == ".":
        return abspath(join(getcwd(), filepath))

    return filepath


def read_templates_from_file(
    filepath, template_format: TemplateFileFormat = TemplateFileFormat.YAML
):
    return read_yaml(get_path_for_read(filepath))


def write_templates_to_file(
    labels,
    filepath,
    template_format: TemplateFileFormat = TemplateFileFormat.YAML,
):
    return write_yaml({"labels": labels}, get_path_for_write(filepath))
