from os import environ
from datetime import datetime
from .http_helpers import request_json, HttpJsonResponse
from letra._parser import extract_labels


def get_headers(token: str = "", auth_required: bool = False):
    headers = {"Accept": "application/vnd.github.symmetra-preview+json"}

    def create_auth_header(pat):
        headers["Authorization"] = f"token {pat}"
        return headers

    if token:
        return create_auth_header(token)
    else:
        token = environ.get("LETRA_GITHUB_PAT")
        if token:
            return create_auth_header(token)
        else:
            if not auth_required:
                return headers
            raise ValueError(
                (
                    "GitHub PAT is required for operation, but no token "
                    "was specified. Please provide a valid GitHub PAT for "
                    "the `token` parameter, or set the LETRA_GITHUB_PAT "
                    "environment variable with a valid GitHub PAT."
                )
            )


def raise_github_repository_not_found_error(
    owner: str, repository: str, request_headers: dict
):
    base_not_found_err = (
        f"Specified GitHub repository: {owner}/{repository} not found. "
        "Please check that you have specified the correct owner "
        "and repository name."
    )
    if "Authorization" not in request_headers:
        raise ValueError(
            (
                f"{base_not_found_err} If you were trying to reference "
                "a private GitHub repository, then authentication must "
                "be provided."
            )
        )
    raise ValueError(base_not_found_err)


def get_throttle_reset_message(end_epoch):
    base_message = "The GitHub API will start accepting requests again at: "
    if end_epoch:
        reset_date_time = datetime.fromtimestamp(end_epoch)
        if reset_date_time:
            return (
                f"{base_message} "
                f"{reset_date_time.strftime('%Y-%m-%d %H:%M:%S')}"
            )

    return f"{base_message} unknown"


def raise_github_unauthorized_error(
    response: HttpJsonResponse,
    owner: str,
    repository: str,
    request_headers: dict,
):
    response_headers = response.headers
    if response_headers.get("X-RateLimit-Remaining") == 0:
        throttle_end_epoch = response_headers.get("X-RateLimit-Reset")
        throttle_end_message = get_throttle_reset_message(throttle_end_epoch)
        throttling_err = (
            "GitHub API requests are being rejected due to rate limiting. "
        )

        if "Authorization" not in request_headers:
            raise IOError(
                (
                    f"{throttling_err}"
                    "You can increase the number of requests that can be "
                    "made by including GitHub authentication information. "
                    f"{throttle_end_message}"
                )
            )

        raise IOError(f"{throttling_err}{throttle_end_message}")

    raise IOError(
        f"Not authorized to access GitHub repository: {owner}/{repository}"
    )


def check_github_api_response_for_errors(
    response: HttpJsonResponse,
    owner: str,
    repository: str,
    request_headers: dict,
):
    status_code = response.status
    if status_code >= 200 and status_code <= 204:
        return

    if status_code == 404:
        raise_github_repository_not_found_error(
            owner=owner, repository=repository, request_headers=request_headers
        )

    if status_code == 401:
        raise ValueError(
            (
                f"Invalid authentication. Unable "
                f"to access GitHub repository: {owner}/{repository}"
            )
        )

    if status_code == 403:
        raise_github_unauthorized_error(
            response=response,
            owner=owner,
            repository=repository,
            request_headers=request_headers,
        )

    raise IOError(
        (
            "Unexpected HTTP error encountered from GitHub API. "
            f"HTTP response status code: {status_code}"
        )
    )


async def retrieve_labels(owner: str, repository: str, url: str, headers: {}):
    response = await request_json(url=url, http_verb="get", headers=headers)
    check_github_api_response_for_errors(
        response=response,
        owner=owner,
        repository=repository,
        request_headers=headers,
    )

    labels = extract_labels({"labels": response.data})
    return response, labels
