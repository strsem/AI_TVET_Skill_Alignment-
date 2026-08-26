import pandas as pd
from src.skills.job_skill_matrix import create_job_skill_matrix

from src.data.loader import load_job_postings
from src.skills.skill_analysis import analyze_skill_importance


# -------------------------
# 1. Load Job Postings
# -------------------------

file_path = "data/raw/job_postings.json"

jobs = load_job_postings(file_path)

print("Number of jobs:", len(jobs))


# -------------------------
# 2. Create DataFrame
# -------------------------

df = pd.DataFrame([
    {
        "title": job.title,
        "company": job.company,
        "required_skills": job.required_skills,
        "preferred_skills": job.preferred_skills,
        "experience": job.experience
    }
    for job in jobs
])


print("\nJob DataFrame:")
print(df.to_string(index=False))


# -------------------------
# 3. Skill Importance
# -------------------------

skill_df = analyze_skill_importance(df)


print("\nSkill Importance:")
print(
    skill_df.to_string(index=False)
)

# -------------------------
# 4. Job × Skill Matrix
# -------------------------

job_skill_df = create_job_skill_matrix(df)

print("\nJob × Skill:")
print(
    job_skill_df.to_string(index=False)
)