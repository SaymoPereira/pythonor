from schema import Optional, Regex, Schema, SchemaError, Or
from letra import Label

color_regex = r"^([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"

label_schema = Schema(
    {
        "name": str,
        Optional("description"): Or(str, None),
        Optional("color"): Regex(color_regex),
    },
    ignore_extra_keys=True,
)

labels_schema = Schema([label_schema], ignore_extra_keys=True)


def build_invalid_label_error(schema_error):
    return (
        "Labels must conform to the schema:\n"
        "  `name`: Required - string\n"
        "  `color`: Required - valid hex color string *without the leading #\n"
        "  `description`: Optional - string\n"
        "Error details: " + schema_error.autos[-1]
    )


def extract_label(label):
    try:
        label_schema.validate(label)
    except SchemaError as err:
        raise ValueError(("Invalid label. " + build_invalid_label_error(err)))

    return Label(
        name=label["name"],
        description=label["description"],
        color=label["color"],
    )


def parse_label(name: str, color: str, description: str):
    return extract_label(
        {"name": name, "color": color, "description": description}
    )


def extract_labels(data):
    labels = data.get("labels")
    if labels is None:
        raise ValueError(
            "Invalid label template. Root level `labels` field missing."
        )
    if len(labels) == 0:
        raise ValueError("No labels found in provided label template.")

    try:
        labels_schema.validate(labels)
    except SchemaError as err:
        msg = (
            "One or more label templates are invalid. "
            + build_invalid_label_error(err)
        )
        raise ValueError(msg)

    return [
        Label(
            name=l["name"],
            description=l.get("description"),
            color=l.get("color"),
        )
        for l in labels
    ]
