from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    match_score: float
    skills: list
    insights: dict
