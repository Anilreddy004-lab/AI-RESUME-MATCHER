from resume_advisor import get_resume_review
from gemini_helper import improve_resume
from ai_matcher import calculate_match
from job_parser import extract_job_skills
from skill_extractor import extract_skills
from resume_parser import extract_text
from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/match")

def match_resume():

    resume_skills = [
        "Python",
        "SQL",
        "Power BI",
        "Excel"
    ]

    job_skills = [
        "Python",
        "SQL",
        "React",
        "FastAPI",
        "Power BI",
        "Excel"
    ]

    result = calculate_match(
        resume_skills,
        job_skills
    )

    return result

@app.post("/ai-review")
async def ai_review(
    description: str,
    file: UploadFile = File(...)
):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    resume_text = extract_text(file_path)

    resume_skills = extract_skills(resume_text)

    job_skills = extract_job_skills(description)

    match_score, matched_skills, missing_skills = calculate_match(
        resume_skills,
        job_skills
    )

    review = get_resume_review(
        match_score,
        matched_skills,
        missing_skills
    )

    return review