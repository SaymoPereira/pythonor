from asyncio import gather as gather_async
from functools import reduce
from operator import concat
from letra import Label
from .github_helpers import (
    check_github_api_response_for_errors,
    get_headers,
    retrieve_labels,
)
from .http_helpers import request_json, HttpJsonResponse
from letra._parser import extract_labels


def get_base_label_api_url(owner: str, repository: str):
    return f"https://api.github.com/repos/{owner}/{repository}/labels"


async def get_labels_from_repository(
    owner: str, repository: str, token: str = ""
):
    base_url = get_base_label_api_url(owner, repository)
    url = f"{base_url}?per_page=100"
    request_headers = get_headers(token)
    response, labels = await retrieve_labels(
        url=url, headers=request_headers, owner=owner, repository=repository,
    )

    link_header = response.headers.get("link")
    if link_header:
        num_pages = link_header[link_header.find('>; rel="last"') - 1]
        paged_labels = await gather_async(
            *[
                retrieve_labels(
                    url=f"{url}&page={i}",
                    headers=request_headers,
                    owner=owner,
                    repository=repository,
                )
                for i in range(2, int(num_pages) + 1)
            ]
        )
        labels += [label for _, labels in paged_labels for label in labels]

    return labels


async def create_label(
    label: Label, owner: str, repository: str, token: str = ""
):
    url = get_base_label_api_url(owner, repository)
    headers = get_headers(token)
    data = {
        "name": label.name,
        "description": label.description,
        "color": label.color,
    }
    response = await request_json(
        url=url, http_verb="post", json=data, headers=headers
    )
    check_github_api_response_for_errors(
        response=response,
        owner=owner,
        repository=repository,
        request_headers=headers,
    )
