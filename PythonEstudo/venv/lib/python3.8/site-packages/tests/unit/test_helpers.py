from letra._helpers import _check_for_duplicate_templates
from letra import Label
from ..helpers import stub_labels
from pytest import raises


def test__check_for_duplicate_templates_raises_on_duplicates():
    dup_label = Label(name="dup", description="oops", color="a24b2a")
    dup_first_copy = Label(name="dup", description="big oops", color="ffffff")
    dup_second_copy = Label(name="dup", description="so bad", color="aaaaaa")
    unique_label = Label(name="unique", description="special", color="abcdef")
    second_dup = Label(
        name="repeated", description="not again", color="bbbbbb"
    )
    second_dup_copy = Label(
        name="repeated", description="yikes", color="cccccc"
    )

    templates = [
        dup_label,
        second_dup,
        dup_first_copy,
        second_dup_copy,
        unique_label,
        dup_second_copy,
    ]

    exp_err = (
        "Found duplicative label templates. The `name` of each "
        "label template must be unique.\nDuplicate templates found:\n"
        f"{dup_label.name}: 3 instances\n"
        f"{second_dup.name}: 2 instances\n"
    )

    with raises(ValueError) as err:
        _check_for_duplicate_templates(templates)
    assert (str(err.value)) == exp_err


def test__check_for_duplicate_templates_does_not_raise_for_unique():
    _check_for_duplicate_templates(stub_labels)
