from fastapi import UploadFile, HTTPException
from starlette.responses import JSONResponse

from services.openai_service.summarize_pdf import summarize_text
from services.pdf_service.extract_pdf.extract_pdf import extract_text_from_pdf


async def summarize(file: UploadFile) -> JSONResponse:
    """
    Summarize a PDF file.

    Args:
        file (UploadFile): The uploaded PDF file.

    Returns:
        JSONResponse: JSON response containing the summary of the PDF content.
    """
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Unsupported file type")

    try:
        pdf_text = extract_text_from_pdf(file)
        if not pdf_text:
            raise HTTPException(status_code=400, detail="No text found in the PDF file")

        summary = await summarize_text(pdf_text)
        return JSONResponse(content={"summary": summary}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the PDF file: {e}")