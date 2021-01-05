from letra._parser import parse_label, extract_labels, extract_label
from letra import Label
from schema import SchemaError
from tests.helpers import (
    bug_label,
    bug_label_contents,
    build_invalid_label_template_error,
    build_label_templates_invalid_color_schema_error,
    build_invalid_label_template_error,
    label_template_name_schema_error,
    label_templates_name_schema_error,
    stub_empty_template_file_contents,
    stub_labels,
    stub_template_file_contents,
    stub_template_label_missing_name,
)
from pytest import raises

sut_module_target = "letra._parser"
label_schema_mock_target = f"{sut_module_target}.label_schema.validate"
labels_schema_mock_target = f"{sut_module_target}.labels_schema.validate"


def test_extract_label_raises_error_when_label_is_invalid(monkeypatch):
    def mock_validate(*unused):
        raise SchemaError(autos=["Missing key: 'name'"])

    monkeypatch.setattr(label_schema_mock_target, mock_validate)

    with raises(ValueError) as err:
        extract_label({})
    assert str(err.value) == label_template_name_schema_error


def test_extract_label_returns_label_when_label_is_valid(monkeypatch):
    def mock_validate(data):
        assert data == bug_label_contents
        return bug_label

    monkeypatch.setattr(label_schema_mock_target, mock_validate)
    label = extract_label(bug_label_contents)
    assert label == bug_label


def test_extract_labels_raises_error_when_template_missing_root_label():
    exp = "Invalid label template. Root level `labels` field missing."
    with raises(ValueError) as err:
        extract_labels({})
    assert str(err.value) == exp


def test_extract_labels_raises_error_when_template_contains_no_labels():
    with raises(ValueError) as err:
        extract_labels(stub_empty_template_file_contents)
    assert str(err.value) == "No labels found in provided label template."


def test_extract_labels_raises_error_when_template_is_invalid(monkeypatch):
    def mock_validate(*unused):
        raise SchemaError(autos=["Missing key: 'name'"])

    monkeypatch.setattr(labels_schema_mock_target, mock_validate)

    with raises(ValueError) as err:
        extract_labels({"labels": [{}]})
    assert str(err.value) == label_templates_name_schema_error


def test_extract_labels_returns_labels_when_template_is_valid(monkeypatch):
    def mock_validate(data):
        assert data == stub_template_file_contents["labels"]
        return stub_labels

    monkeypatch.setattr(labels_schema_mock_target, mock_validate)
    labels = extract_labels(stub_template_file_contents)
    assert labels == stub_labels


def test_parse_label_passes_correct_object(monkeypatch):
    act_label_param = None
    label_name = "bug"
    label_color = "ffffff"
    label_description = "bad things happened"
    exp_label = Label(
        name=label_name, description=label_description, color=label_color
    )

    def mock_extract_label(label):
        nonlocal act_label_param
        act_label_param = label
        return exp_label

    monkeypatch.setattr(
        f"{sut_module_target}.extract_label", mock_extract_label
    )
    act_label = parse_label(
        name=label_name, description=label_description, color=label_color
    )

    assert act_label == exp_label
    assert act_label_param == {
        "name": label_name,
        "description": label_description,
        "color": label_color,
    }
