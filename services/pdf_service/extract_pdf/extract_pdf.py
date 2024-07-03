import fitz
from fastapi import UploadFile, HTTPException
from typing import Optional


def extract_text_from_pdf(file: UploadFile) -> Optional[str]:
    """
    Extract text from a PDF file.

    Args:
        file (UploadFile): The uploaded PDF file.

    Returns:
        Optional[str]: The extracted text from the PDF file, or None if no text is found.
    """
    try:
        pdf_document = fitz.open(stream=file.file.read(), filetype="pdf")
        text = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
        return text if text.strip() else None
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while extracting text from the PDF file: {e}")
