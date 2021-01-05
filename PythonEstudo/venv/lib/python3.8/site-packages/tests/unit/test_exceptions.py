from letra.exceptions import LabelCreationError, LabelTemplateCreationError
from pytest import raises


def test_label_template_creation_error():
    exp_err = "failed to create label template"
    with raises(LabelTemplateCreationError) as err:
        raise LabelTemplateCreationError(exp_err)
    assert str(err.value) == exp_err


def test_label_creation_error():
    exp_err = "failed to create label"
    with raises(LabelCreationError) as err:
        raise LabelCreationError(exp_err)
    assert str(err.value) == exp_err
