# src/main.py

from api.xml_api import fetch_xml_data
from parsers.xml_parser import parse_xml_data
from utils.pdf_parser import parse_pdf
from utils.chatgpt_api import summarize_pdf_with_chatgpt
from utils.download_pdf import download_pdf
from pprint import pprint


def main():
    # Fetch XML data from the API
    api_url = "http://export.arxiv.org/api/query?search_query=cat:cs.AI&start=0&max_results=1&sortBy=submittedDate&sortOrder=descending"
    xml_data = fetch_xml_data(api_url)

    # Parse the XML data to extract required parameters
    parsed_data = parse_xml_data(xml_data)

    for pdf in parsed_data:
        """
        Take the parsed data back and download the PDFs from the URLs. Name the PDFs with the version number for easy reference.
        """
        url = pdf["url"]  # Extract the URL from the parsed data
        url_version = url[21:]  # Extract the version number from the URL
        pdf_path = download_pdf(
            pdf_url=url, title=url_version
        )  # Download the PDF for further reviewing
        pdf_text = parse_pdf(
            pdf_path
        )  # Parse the PDF content to extract the text, this will be sent to OpenAI ChatGPT for summarization

        # Use ChatGPT to summarize the PDF content
        chatgpt_summary = summarize_pdf_with_chatgpt(pdf_text)

    # Print the results
    pprint(parsed_data)
    print("ChatGPT Summary:", chatgpt_summary)


if __name__ == "__main__":
    main()
