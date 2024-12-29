def download_pdf(pdf_url):
    import requests

    response = requests.get(pdf_url)
    pdf_path = "downloaded_paper.pdf"
    with open(pdf_path, "wb") as f:
        f.write(response.content)
    return pdf_path
