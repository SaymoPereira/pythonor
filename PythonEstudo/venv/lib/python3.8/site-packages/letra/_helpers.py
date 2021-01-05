from . import Label
from typing import List


def _check_for_duplicate_templates(templates: List[Label]):
    processed = {}
    duplicates = {}

    for template in templates:
        if template.name in processed:
            duplicates[template.name] = duplicates.get(template.name, 1) + 1
        else:
            processed[template.name] = 0

    if duplicates:
        base_msg = (
            "Found duplicative label templates. The `name` of each "
            "label template must be unique.\nDuplicate templates found:\n"
        )
        duplicate_msg = ""
        for label, count in duplicates.items():
            duplicate_msg = f"{duplicate_msg}{label}: {count} instances\n"

        raise ValueError(f"{base_msg}{duplicate_msg}")
