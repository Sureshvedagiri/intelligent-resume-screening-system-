import PyPDF2
import io
import re

async def extract_text_from_pdf(file):
    content = await file.read()
    reader = PyPDF2.PdfReader(io.BytesIO(content))
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    return text.lower()


def extract_skills(text):
    skill_keywords = [
        "python", "machine learning", "deep learning",
        "sql", "fastapi", "flask", "docker", "nlp"
    ]

    found_skills = [skill for skill in skill_keywords if skill in text]
    return found_skills


def compute_match_score(resume_text, job_description):
    job_keywords = re.findall(r'\w+', job_description.lower())
    match_count = sum(1 for word in job_keywords if word in resume_text)

    score = (match_count / len(job_keywords)) * 100 if job_keywords else 0
    return round(score, 2)
