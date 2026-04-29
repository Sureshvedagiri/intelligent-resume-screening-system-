from fastapi import APIRouter, UploadFile, File, Form
from app.services import process_resume

router = APIRouter()

@router.get("/")
def health_check():
    return {"status": "API is running"}

@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    result = await process_resume(resume, job_description)
    return result
