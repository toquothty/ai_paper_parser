def parse_pdf(pdf_path):
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
