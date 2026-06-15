def get_resume_review(match_score, matched_skills, missing_skills):

    strengths = []
    weaknesses = []
    suggestions = []
    projects = []

    if match_score >= 80:
        ats = "Excellent ATS Score"
    elif match_score >= 60:
        ats = "Good ATS Score"
    else:
        ats = "Needs Improvement"

    if len(matched_skills) > 0:
        strengths.append(
            "Good technical skills: " + ", ".join(matched_skills)
        )

    if len(missing_skills) > 0:
        weaknesses.append(
            "Missing important skills: " + ", ".join(missing_skills)
        )

        suggestions.append(
            "Learn these skills: " + ", ".join(missing_skills)
        )

    suggestions.extend([
        "Improve GitHub profile.",
        "Add more real-world projects.",
        "Keep resume to one page.",
        "Add measurable achievements."
    ])

    projects.extend([
        "AI Resume Matcher",
        "Job Portal",
        "Employee Management System",
        "Sales Dashboard",
        "E-commerce Analytics"
    ])

    return {
        "ATS_Result": ats,
        "Match_Score": match_score,
        "Matched_Skills": matched_skills,
        "Missing_Skills": missing_skills,
        "Strengths": strengths,
        "Weaknesses": weaknesses,
        "Suggestions": suggestions,
        "Project_Ideas": projects,
        "Final_Recommendation":
        "Good for entry-level roles. Continue improving missing skills and build projects."
    }