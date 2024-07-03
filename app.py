from fastapi import FastAPI
from services.pdf_service.summarize_pdf.routes import router as SummarizePDFServiceRouter

app = FastAPI()

app.include_router(SummarizePDFServiceRouter, tags=["PDF Analysis"])
