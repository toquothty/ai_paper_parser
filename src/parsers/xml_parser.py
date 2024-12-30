def parse_xml_data(xml_data):
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
