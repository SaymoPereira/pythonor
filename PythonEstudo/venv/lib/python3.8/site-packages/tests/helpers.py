from letra import Label
from letra._parser import color_regex
from letra._label_platform_provider.http_helpers import HttpJsonResponse
from io import StringIO, TextIOWrapper
from string import Template

bug_name = "bug"
bug_description = "Something isn't working!"
bug_color = "d73a4a"
bug_label = Label(name=bug_name, description=bug_description, color=bug_color)

other_name = "other"
other_description = "Something different"
other_color = "a24b2a"
other_label = Label(
    name=other_name, description=other_description, color=other_color
)

stub_labels = [bug_label, other_label]
bug_label_contents = {
    "name": bug_name,
    "description": bug_description,
    "color": bug_color,
}

stub_template_file_contents = {
    "labels": [
        bug_label_contents,
        {
            "name": other_name,
            "description": other_description,
            "color": other_color,
        },
    ]
}

stub_empty_template_file_contents = {"labels": []}
stub_template_label_missing_name = {"labels": [{"description": "foo"}]}


def mock_empty(*unused):
    return ""


def mock_false(*unused):
    return False


def mock_true(*unused):
    return True


stub_stream = TextIOWrapper(StringIO("", "\n"), "utf8", "", "\n", True, True)
stub_request_json_response = HttpJsonResponse(
    status=200, headers={}, data=stub_template_file_contents["labels"]
)


def mock_stream(*unused):
    return stub_stream


async def async_enter(self):
    return self


async def async_exit(self, *unused):
    return self


stub_context_manager = type(
    "", (object,), {"__enter__": mock_stream, "__exit__": mock_empty}
)()


def build_async_http_mock(json_content):
    async def json(self):
        return json_content

    return type(
        "",
        (object,),
        {"__aenter__": async_enter, "__aexit__": async_exit, "json": json},
    )()


def build_schema_failure_error_message(details):
    return (
        "Labels must conform to the schema:\n"
        "  `name`: Required - string\n"
        "  `color`: Required - valid hex color string *without the leading #\n"
        "  `description`: Optional - string\n"
        "Error details: " + details
    )


def build_invalid_label_template_error(details):
    return "Invalid label. " + build_schema_failure_error_message(details)


def build_invalid_label_templates_error(details):
    return (
        "One or more label templates are invalid. "
        + build_schema_failure_error_message(details)
    )


def build_label_templates_invalid_color_schema_error(color):
    return build_invalid_label_templates_error(
        f"Regex('{color_regex}') does not match '{color}'"
    )


missing_name_key_details = "Missing key: 'name'"
label_templates_name_schema_error = build_invalid_label_templates_error(
    missing_name_key_details
)
label_template_name_schema_error = build_invalid_label_template_error(
    missing_name_key_details
)
