def extract_job_skills(text):

    skills = [
        "Python",
        "SQL",
        "React",
        "FastAPI",
        "MySQL",
        "Pandas",
        "NumPy",
        "Power BI",
        "Tableau",
        "Excel",
        "JavaScript",
        "HTML",
        "CSS",
        "Git",
        "Django"
    ]

    found = []

    text = text.lower()

    for skill in skills:
        if skill.lower() in text:
            found.append(skill)

    return found