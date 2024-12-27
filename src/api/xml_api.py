def fetch_xml_data(api_url):
    import requests

    response = requests.get(api_url)
    if response.status_code == 200:
        return response.content
    else:
        response.raise_for_status()