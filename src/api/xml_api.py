from typing import Any


def fetch_xml_data(api_url: str) -> Any:
    """
    Fetches XML data from the given API URL.

    Args:
        api_url (str): The URL of the API endpoint to fetch XML data from.

    Returns:
        Any: The XML data fetched from the API.

    Raises:
        requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
    """
    import requests

    response = requests.get(api_url)
    if response.status_code == 200:
        return response.content
    else:
        response.raise_for_status()
