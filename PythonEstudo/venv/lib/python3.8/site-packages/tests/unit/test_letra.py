from pytest import mark, raises
from letra.letra import (
    get_labels_from_github,
    _create_label,
    create_github_label,
    _create_label_template_file,
    create_github_label,
    _create_label_in_github_repository,
    create_label_template_file,
    create_label_template_file_from_github,
    _retrieve_labels,
)
from letra import (
    Label,
    LabelCreationError,
    LabelTemplateCreationError,
    TemplateFileFormat,
)
from tests.helpers import stub_labels, build_schema_failure_error_message

pytestmark = mark.asyncio
sut_module_target = "letra.letra"
get_labels_mock_target = f"{sut_module_target}.get_labels"
write_templates_to_file_mock_target = (
    f"{sut_module_target}.write_templates_to_file"
)
_create_label_template_file_mock_target = (
    f"{sut_module_target}._create_label_template_file"
)
create_label_template_file_mock_target = (
    f"{sut_module_target}.create_label_template_file"
)
_retrieve_labels_mock_target = f"{sut_module_target}._retrieve_labels"
_create_label_in_github_repository_mock_target = (
    f"{sut_module_target}._create_label_in_github_repository"
)
_parse_label_mock_target = f"{sut_module_target}._parse_label"
_create_label_mock_target = f"{sut_module_target}._create_label"
target_file_name = "templates.yml"
target_owner = "swellaby"
target_repository = "letra"
exp_gh_target_name = "GitHub"
exp_default_label_template_format = TemplateFileFormat.YAML


def get_label_retrieval_input_error(target, details):
    return (
        f"Unable to retrieve labels from {target} due to invalid inputs. "
        f"Error details: {details}"
    )


def get_label_retrieval_failure_error(target, details):
    return (
        "Encountered error while attempting to retrieve "
        f"labels from {target}. Error details: {details}"
    )


def get_parse_label_validation_error(target, details):
    return (
        f"Unable to create label in {target} due to invalid "
        f"inputs. Error details: {details}"
    )


def get_label_creation_io_error(target, details):
    return (
        "Encountered error while attempting to create "
        f"label in {target}. Error details: {details}"
    )


async def test__retrieve_labels_raises_err_on_retrieval_value_err():
    act_owner = ""
    act_repository = ""
    act_token = ""
    exp_token = "abc123def"
    exp_err_details = "401 bad credentials"
    exp_err = get_label_retrieval_input_error(
        exp_gh_target_name, exp_err_details
    )

    async def mock_get_labels(**kwargs):
        nonlocal act_owner, act_repository, act_token
        act_owner = kwargs.get("owner")
        act_repository = kwargs.get("repository")
        act_token = kwargs.get("token")
        raise ValueError(exp_err_details)

    with raises(LabelTemplateCreationError) as err:
        await _retrieve_labels(
            get_labels=mock_get_labels,
            target_name=exp_gh_target_name,
            owner=target_owner,
            repository=target_repository,
            token=exp_token,
        )

    assert str(err.value) == exp_err
    assert act_owner == target_owner
    assert act_repository == target_repository
    assert act_token == exp_token


async def test__retrieve_labels_raises_err_on_retrieval_io_err():
    exp_err_details = "github api crashed"
    exp_err = get_label_retrieval_failure_error(
        exp_gh_target_name, exp_err_details
    )

    async def mock_get_labels(**kwargs):
        raise IOError(exp_err_details)

    with raises(LabelTemplateCreationError) as err:
        await _retrieve_labels(
            get_labels=mock_get_labels,
            target_name=exp_gh_target_name,
            owner=target_owner,
            repository=target_repository,
        )

    assert str(err.value) == exp_err


async def test__retrieve_labels_returns_labels_on_success():
    async def mock_get_labels(**kwargs):
        return stub_labels

    labels = await _retrieve_labels(
        get_labels=mock_get_labels,
        target_name=exp_gh_target_name,
        owner=target_owner,
        repository=target_repository,
    )

    assert labels == stub_labels


async def test_create_label_template_file_raises_err_on_invalid_filepath(
    monkeypatch,
):
    act_filepath = None
    act_labels = None
    exp_err_details = "invalid filename"
    exp_err = (
        "Failed to create label template file due to invalid inputs. "
        f"Error details: {exp_err_details}"
    )

    def mock_write_templates_to_file(filepath: str, labels, template_format):
        nonlocal act_filepath, act_labels
        act_filepath = filepath
        act_labels = labels
        raise ValueError(exp_err_details)

    monkeypatch.setattr(
        write_templates_to_file_mock_target, mock_write_templates_to_file
    )

    with raises(LabelTemplateCreationError) as err:
        await create_label_template_file(
            labels=stub_labels, filepath=target_file_name
        )

    assert str(err.value) == exp_err
    assert act_filepath == target_file_name
    assert act_labels == stub_labels


async def test_create_label_template_file_raises_err_on_file_write_err(
    monkeypatch,
):
    exp_err_details = "no permissions"
    exp_err = (
        "Encountered error while attempting to write labels to file. "
        f"Error details: {exp_err_details}"
    )

    def mock_write_templates_to_file(filepath: str, labels, template_format):
        raise IOError(exp_err_details)

    monkeypatch.setattr(
        write_templates_to_file_mock_target, mock_write_templates_to_file
    )

    with raises(LabelTemplateCreationError) as err:
        await create_label_template_file(
            labels=stub_labels, filepath=target_file_name
        )

    assert str(err.value) == exp_err


async def test_create_label_template_file_uses_correct_default_format(
    monkeypatch,
):
    act_format = None

    def mock_write_templates_to_file(filepath: str, labels, template_format):
        nonlocal act_format
        act_format = template_format

    monkeypatch.setattr(
        write_templates_to_file_mock_target, mock_write_templates_to_file
    )

    await create_label_template_file(
        labels=stub_labels, filepath=target_file_name
    )

    assert act_format == exp_default_label_template_format


async def test_create_label_template_file_uses_specified_format(monkeypatch):
    act_format = None
    exp_format = TemplateFileFormat.JSON

    def mock_write_templates_to_file(filepath: str, labels, template_format):
        nonlocal act_format
        act_format = template_format

    monkeypatch.setattr(
        write_templates_to_file_mock_target, mock_write_templates_to_file
    )

    await create_label_template_file(
        labels=stub_labels,
        filepath=target_file_name,
        template_format=exp_format,
    )

    assert act_format == exp_format


async def test__create_label_template_file_uses_right_args(monkeypatch):
    act_get_labels = None
    act_labels = None
    act_filepath = ""
    act_target_name = ""
    act_owner = ""
    act_repository = ""
    act_token = ""
    act_format = None
    exp_format = TemplateFileFormat.TOML
    exp_token = "000lmn234"

    async def mock_retrieve_labels(**kwargs):
        nonlocal act_get_labels, act_target_name, act_owner
        nonlocal act_repository, act_token

        act_get_labels = kwargs.get("get_labels")
        act_target_name = kwargs.get("target_name")
        act_owner = kwargs.get("owner")
        act_repository = kwargs.get("repository")
        act_token = kwargs.get("token")

        return stub_labels

    async def mock_create_template_file(
        filepath: str, labels: list, template_format: TemplateFileFormat
    ):
        nonlocal act_labels, act_filepath, act_format
        act_filepath = filepath
        act_labels = labels
        act_format = template_format

    async def mock_get_labels(**kwargs):
        pass

    monkeypatch.setattr(_retrieve_labels_mock_target, mock_retrieve_labels)
    monkeypatch.setattr(
        create_label_template_file_mock_target, mock_create_template_file
    )

    assert (
        await _create_label_template_file(
            get_labels=mock_get_labels,
            filepath=target_file_name,
            target_name=exp_gh_target_name,
            owner=target_owner,
            repository=target_repository,
            token=exp_token,
            template_format=exp_format,
        )
        is None
    )

    assert act_get_labels == mock_get_labels
    assert act_filepath == target_file_name
    assert act_target_name == exp_gh_target_name
    assert act_owner == target_owner
    assert act_repository == target_repository
    assert act_token == exp_token
    assert act_format == exp_format


async def test_create_label_template_file_from_github_uses_right_args(
    monkeypatch,
):
    act_get_labels = None
    act_filepath = ""
    act_target_name = ""
    act_owner = ""
    act_repository = ""
    act_token = ""
    act_format = None
    exp_format = TemplateFileFormat.TOML
    exp_token = "987zyx654"

    async def mock_create_label_template_file(**kwargs):
        nonlocal act_get_labels, act_filepath, act_target_name
        nonlocal act_owner, act_repository, act_token, act_format

        act_get_labels = kwargs.get("get_labels")
        act_filepath = kwargs.get("filepath")
        act_target_name = kwargs.get("target_name")
        act_owner = kwargs.get("owner")
        act_repository = kwargs.get("repository")
        act_token = kwargs.get("token")
        act_format = kwargs.get("template_format")

    monkeypatch.setattr(
        _create_label_template_file_mock_target,
        mock_create_label_template_file,
    )

    assert (
        await create_label_template_file_from_github(
            filepath=target_file_name,
            owner=target_owner,
            repository=target_repository,
            token=exp_token,
        )
        is None
    )

    assert act_get_labels == get_labels_from_github
    assert act_filepath == target_file_name
    assert act_target_name == exp_gh_target_name
    assert act_owner == target_owner
    assert act_repository == target_repository
    assert act_token == exp_token


async def test_create_label_template_file_from_github_uses_default_format(
    monkeypatch,
):
    act_format = None

    async def mock_create_label_template_file(**kwargs):
        nonlocal act_format
        act_format = kwargs.get("template_format")

    monkeypatch.setattr(
        _create_label_template_file_mock_target,
        mock_create_label_template_file,
    )

    await create_label_template_file_from_github(
        filepath=target_file_name,
        owner=target_owner,
        repository=target_repository,
    )

    assert act_format == exp_default_label_template_format


async def test_create_label_template_file_from_github_uses_specified_format(
    monkeypatch,
):
    act_format = None
    exp_format = TemplateFileFormat.TOML

    async def mock_create_label_template_file(**kwargs):
        nonlocal act_format
        act_format = kwargs.get("template_format")

    monkeypatch.setattr(
        _create_label_template_file_mock_target,
        mock_create_label_template_file,
    )

    await create_label_template_file_from_github(
        filepath=target_file_name,
        owner=target_owner,
        repository=target_repository,
        template_format=exp_format,
    )

    assert act_format == exp_format


async def test__create_label_raises_err_on_validation_failure(monkeypatch):
    act_name = ""
    act_description = ""
    act_color = ""
    exp_err_details = build_schema_failure_error_message("invalid color")
    exp_err = get_parse_label_validation_error(
        target=exp_gh_target_name, details=exp_err_details
    )
    exp_name = "feature request"
    exp_description = "some cool new thing"
    exp_color = "0246cc"

    def mock_parse_label(name, description, color):
        nonlocal act_name, act_description, act_color
        act_name = name
        act_description = description
        act_color = color
        raise ValueError(exp_err_details)

    async def mock_create_github_label(**kwargs):
        pass

    monkeypatch.setattr(_parse_label_mock_target, mock_parse_label)

    with raises(LabelCreationError) as err:
        await _create_label(
            create_label=mock_create_github_label,
            target_name=exp_gh_target_name,
            owner="",
            repository="",
            label_name=exp_name,
            label_color=exp_color,
            label_description=exp_description,
        )

    assert str(err.value) == exp_err
    assert act_name == exp_name
    assert act_color == exp_color
    assert act_description == exp_description


async def test__create_label_raises_err_on_io_failure(monkeypatch):
    act_label = ""
    act_owner = ""
    act_repository = ""
    act_token = ""
    exp_err_details = "unauthorized"
    exp_err = get_label_creation_io_error(
        target=exp_gh_target_name, details=exp_err_details
    )
    exp_token = "password ;)"
    exp_name = "question"
    exp_description = "what is your favorite color?"
    exp_color = "842fe3"
    exp_label = Label(
        name=exp_name, description=exp_description, color=exp_color
    )

    def mock_parse_label(**kwargs):
        return exp_label

    async def mock_create_github_label(label, owner, repository, token):
        nonlocal act_label, act_owner, act_repository, act_token
        act_label = label
        act_owner = owner
        act_repository = repository
        act_token = token
        raise IOError(exp_err_details)

    monkeypatch.setattr(_parse_label_mock_target, mock_parse_label)

    with raises(LabelCreationError) as err:
        await _create_label(
            create_label=mock_create_github_label,
            target_name=exp_gh_target_name,
            owner=target_owner,
            repository=target_repository,
            label_name=exp_name,
            label_color=exp_color,
            label_description=exp_description,
            token=exp_token,
        )

    assert str(err.value) == exp_err
    assert act_label == exp_label
    assert act_owner == target_owner
    assert act_repository == target_repository
    assert act_token == exp_token


async def test__create_label_returns_on_success(monkeypatch):
    async def mock_create_github_label(**kwargs):
        pass

    monkeypatch.setattr(
        _parse_label_mock_target, lambda **kwargs: stub_labels[0]
    )
    monkeypatch.setattr(
        _create_label_in_github_repository_mock_target,
        mock_create_github_label,
    )

    assert (
        await _create_label(
            create_label=mock_create_github_label,
            target_name=exp_gh_target_name,
            owner=target_owner,
            repository=target_repository,
            label_name="",
            label_color="",
            label_description="",
        )
        is None
    )


async def test_create_label_uses_correct_args(monkeypatch):
    act_owner = ""
    act_repository = ""
    act_token = ""
    act_name = ""
    act_description = ""
    act_color = ""
    act_target = ""
    act_label_creator = None
    exp_token = "123"
    exp_name = "dependencies"
    exp_description = "dependabot"
    exp_color = "016746"

    async def mock__create_label(
        create_label,
        target_name: str,
        owner: str,
        repository: str,
        token: str,
        label_name: str,
        label_color: str,
        label_description: str,
    ):
        nonlocal act_owner, act_repository, act_token
        nonlocal act_name, act_description, act_color
        nonlocal act_target, act_label_creator
        act_owner = owner
        act_repository = repository
        act_token = token
        act_name = label_name
        act_color = label_color
        act_description = label_description
        act_label_creator = create_label
        act_target = target_name

    monkeypatch.setattr(_create_label_mock_target, mock__create_label)

    assert (
        await create_github_label(
            owner=target_owner,
            repository=target_repository,
            label_name=exp_name,
            label_color=exp_color,
            label_description=exp_description,
            token=exp_token,
        )
        is None
    )

    assert act_owner == target_owner
    assert act_repository == target_repository
    assert act_token == exp_token
    assert act_name == exp_name
    assert act_color == exp_color
    assert act_description == exp_description
    assert act_label_creator == _create_label_in_github_repository
    assert act_target == exp_gh_target_name


async def test_create_label_uses_correct_defaults(monkeypatch):
    act_token = ""
    act_description = ""

    async def mock__create_label(token: str, label_description: str, **kwargs):
        nonlocal act_description, act_token
        act_token = token
        act_description = label_description

    monkeypatch.setattr(_create_label_mock_target, mock__create_label)

    assert (
        await create_github_label(
            owner=target_owner,
            repository=target_repository,
            label_name="",
            label_color="",
        )
        is None
    )

    assert act_token == ""
    assert act_description == ""
