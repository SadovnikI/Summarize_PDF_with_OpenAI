from fastapi import APIRouter
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse
from services.pdf_service.summarize_pdf.controllers import summarize

router = APIRouter()


@router.post("/summarize")
async def summarize_handler(file: UploadFile = File(...)) -> JSONResponse:
    """
    Endpoint to summarize a PDF file.

    Args:
        file (UploadFile): The uploaded PDF file.

    Returns:
        JSONResponse: JSON response containing the summary of the PDF content.
    """
    return await summarize(file)
