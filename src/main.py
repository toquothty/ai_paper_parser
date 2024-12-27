# src/main.py

import requests
from api.xml_api import fetch_xml_data
from parsers.xml_parser import parse_xml_data
from parsers.pdf_parser import parse_pdf
from utils.chatgpt_api import summarize_pdf_with_chatgpt


def main():
    # Fetch XML data from the API
    xml_data = fetch_xml_data()

    # Parse the XML data to extract required parameters
    parsed_data = parse_xml_data(xml_data)

    # Download the PDF and save it locally (assuming a function to handle this)
    pdf_path = download_pdf(parsed_data["pdf_url"])

    # Use ChatGPT to summarize the PDF content
    chatgpt_summary = summarize_pdf_with_chatgpt(pdf_path)

    # Print the results
    print("Parsed Data:", parsed_data)
    print("ChatGPT Summary:", chatgpt_summary)


def download_pdf(pdf_url):
    response = requests.get(pdf_url)
    pdf_path = "downloaded_paper.pdf"
    with open(pdf_path, "wb") as f:
        f.write(response.content)
    return pdf_path


if __name__ == "__main__":
    main()
