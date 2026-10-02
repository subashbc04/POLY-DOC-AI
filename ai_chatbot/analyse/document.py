import fitz


def extract_text_from_pdf(pdf_file):
    text = ""

    pdf_data = pdf_file.read()

    doc = fitz.open(stream=pdf_data, filetype="pdf")

    for page in doc:
        page_text = page.get_text()

        if page_text:
            text += page_text + "\n"

    doc.close()

    return text
            
