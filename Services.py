from app.utils import extract_text_from_pdf, extract_skills, compute_match_score
from app.database import save_analysis

async def process_resume(file, job_description):
    resume_text = await extract_text_from_pdf(file)

    skills = extract_skills(resume_text)
    score = compute_match_score(resume_text, job_description)

    insights = {
        "detected_skills": skills,
        "recommendation": "Improve alignment with job-specific keywords and include measurable achievements."
    }

    save_analysis(file.filename, job_description, score)

    return {
        "match_score": score,
        "skills": skills,
        "insights": insights
    }
