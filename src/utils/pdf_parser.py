from typing import str


def parse_pdf(pdf_path: str) -> str:
    """
    Parses the content of a PDF file and extracts the text.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF file.
    """
    from PyPDF2 import PdfReader

    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"

    except Exception as e:
        print(f"Error reading PDF file: {e}")

    return text
