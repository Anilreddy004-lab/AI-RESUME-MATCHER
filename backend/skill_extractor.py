SKILLS = [
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


def extract_skills(text):

    found_skills = []

    text = text.lower()

    for skill in SKILLS:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills