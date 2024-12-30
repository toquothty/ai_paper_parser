from typing import Any


def download_pdf(pdf_url: str, title: str) -> str:
    """
    Downloads a PDF from the given URL and saves it with the specified title.

    Args:
        pdf_url (str): The URL of the PDF to download.
        title (str): The title to save the PDF as.

    Returns:
        str: The path to the downloaded PDF.
    """
    import requests

    response = requests.get(pdf_url)
    pdf_path = f"papers/{title}.pdf"
    with open(pdf_path, "wb") as f:
        f.write(response.content)
    return pdf_path
