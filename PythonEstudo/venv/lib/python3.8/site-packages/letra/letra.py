from ._file_io import write_templates_to_file
from ._label_platform_provider import (
    create_label_in_github_repository as _create_label_in_github_repository,
    get_labels_from_github,
)
from letra import (
    Label,
    LabelCreationError,
    LabelTemplateCreationError,
    TemplateFileFormat,
)
from typing import List
from ._parser import parse_label as _parse_label

__default_label_template_format = TemplateFileFormat.YAML
__github_target = "GitHub"


async def create_label_template_file(
    labels: List[Label],
    filepath: str,
    template_format: TemplateFileFormat = __default_label_template_format,
):
    try:
        write_templates_to_file(
            labels=labels, filepath=filepath, template_format=template_format
        )
    except ValueError as err:
        raise LabelTemplateCreationError(
            (
                "Failed to create label template file due to invalid inputs. "
                f"Error details: {str(err)}"
            )
        )
    except Exception as err:
        raise LabelTemplateCreationError(
            (
                "Encountered error while attempting to write labels to file. "
                f"Error details: {str(err)}"
            )
        )


async def _retrieve_labels(get_labels, target_name: str, **kwargs):
    try:
        labels = await get_labels(**kwargs)
        return labels
    except ValueError as err:
        details = str(err)
        msg = (
            f"Unable to retrieve labels from {target_name} due to invalid "
            f"inputs. Error details: {details}"
        )
        raise LabelTemplateCreationError(msg)
    except Exception as err:
        details = str(err)
        msg = (
            "Encountered error while attempting to retrieve "
            f"labels from {target_name}. Error details: {details}"
        )
        raise LabelTemplateCreationError(msg)


async def _create_label_template_file(
    get_labels,
    filepath: str,
    target_name: str,
    template_format: TemplateFileFormat,
    **kwargs,
):
    labels = await _retrieve_labels(
        get_labels=get_labels, target_name=target_name, **kwargs
    )
    await create_label_template_file(
        filepath=filepath, labels=labels, template_format=template_format
    )


async def create_label_template_file_from_github(
    filepath: str,
    owner: str,
    repository: str,
    token: str = "",
    template_format: TemplateFileFormat = __default_label_template_format,
):
    await _create_label_template_file(
        get_labels=get_labels_from_github,
        filepath=filepath,
        template_format=template_format,
        target_name=__github_target,
        owner=owner,
        repository=repository,
        token=token,
    )


async def _create_label(
    create_label,
    target_name: str,
    label_name: str,
    label_color: str,
    label_description: str,
    **kwargs,
):
    label = None
    try:
        label = _parse_label(
            name=label_name, color=label_color, description=label_description
        )
    except ValueError as err:
        details = str(err)
        msg = (
            f"Unable to create label in {target_name} due to invalid "
            f"inputs. Error details: {details}"
        )
        raise LabelCreationError(msg)

    try:
        await create_label(label=label, **kwargs)
    except Exception as err:
        details = str(err)
        msg = (
            "Encountered error while attempting to create "
            f"label in {target_name}. Error details: {details}"
        )
        raise LabelCreationError(msg)


async def create_github_label(
    owner: str,
    repository: str,
    label_name: str,
    label_color: str,
    label_description: str = "",
    token: str = "",
):
    await _create_label(
        create_label=_create_label_in_github_repository,
        target_name=__github_target,
        owner=owner,
        repository=repository,
        label_name=label_name,
        label_color=label_color,
        label_description=label_description,
        token=token,
    )
