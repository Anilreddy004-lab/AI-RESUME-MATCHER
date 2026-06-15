import google.generativeai as genai

API_KEY = ""

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


def improve_resume(resume_text, job_description):

    prompt = f"""
    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Analyse the resume.

    Give:
    1. ATS Score out of 100.
    2. Missing Skills.
    3. Resume Strengths.
    4. Weaknesses.
    5. Suggestions to improve.
    6. Better project ideas.
    7. Final recommendation.

    Format the answer clearly.
    """

    response = model.generate_content(prompt)

    return response.text