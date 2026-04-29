from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Intelligent Resume Screening System",
    description="AI-powered system for resume analysis and candidate-job matching",
    version="1.0.0"
)

app.include_router(router)
