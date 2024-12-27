def parse_xml_data(xml_data):
    import xml.etree.ElementTree as ET

    root = ET.fromstring(xml_data)
    parsed_data = []

    for item in root.findall('.//item'):
        title = item.find('title').text
        id = item.find('id').text
        published_date = item.find('published_date').text
        summary = item.find('summary').text
        urls = [url.text for url in item.findall('url')]

        parsed_data.append({
            'title': title,
            'id': id,
            'published_date': published_date,
            'summary': summary,
            'urls': urls
        })

    return parsed_data