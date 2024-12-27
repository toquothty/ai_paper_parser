def parse_pdf(pdf_path):
    import PyPDF2

    summary = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            # Here you can implement a simple text summarization logic or return the text
            summary = text[:500]  # Example: return the first 500 characters as a summary
    except Exception as e:
        print(f"Error reading PDF file: {e}")

    return summary