from typing import List, Dict


def parse_xml_data(xml_data: str) -> List[Dict[str, str]]:
    """
    Parses the given XML data to extract information about research papers.

    Args:
        xml_data (str): The XML data as a string.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing parsed data for each paper.
            Each dictionary contains the following keys:
            - "title": The title of the paper.
            - "id": The ID of the paper.
            - "published_date": The published date of the paper.
            - "summary": The summary of the paper.
            - "url": The URL to the PDF of the paper.
    """
    import xml.etree.ElementTree as ET

    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_data)

    entries = root.findall("atom:entry", namespaces=namespace)
    parsed_data = []

    for item in entries:
        title = item.find("atom:title", namespaces=namespace).text
        id = item.find("atom:id", namespaces=namespace).text
        published_date = item.find("atom:published", namespaces=namespace).text
        summary = item.find("atom:summary", namespaces=namespace).text
        pdf_link = item.find("atom:link[@title='pdf']", namespaces=namespace)
        url = pdf_link.attrib["href"]

        parsed_data.append(
            {
                "title": title,
                "id": id,
                "published_date": published_date,
                "summary": summary,
                "url": url,
            }
        )

    return parsed_data
