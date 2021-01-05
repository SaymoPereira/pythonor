from letra import Label

name = "bug"
description = "Something isn't working!"
color = "#d73a4a"
test_label = Label(name=name, description=description, color=color)


def test_label_has_correct_name():
    assert test_label.name == name


def test_label_has_correct_description():
    assert test_label.description == description


def test_label_has_correct_color():
    assert test_label.color == color
