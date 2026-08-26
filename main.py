import pandas as pd
from src.data.loader import load_job_postings

# 1. Load job postings
file_path = "data/raw/job_postings.json"

jobs = load_job_postings(file_path)

print("Number of jobs:", len(jobs))

# 2. Create DataFrame
df = pd.DataFrame([
    {
        "title": job.title,
        "company": job.company,
        "skills": job.skills,
        "experience": job.experience
    }
    for job in jobs
])
print("\nDataFrame:")
print(df)

# 3. Count skill frequency

skill_counts = {}

for skills in df["skills"]:
    for skill in skills:

        skill_counts[skill] = skill_counts.get(skill, 0) + 1

# 4. Create Skill DataFrame

skill_df = pd.DataFrame(
    list(skill_counts.items()),
    columns=["skill", "job_count"]
)


# 5. Sort by frequency

skill_df = skill_df.sort_values(
    by="job_count",
    ascending=False
).reset_index(drop=True)


print("\nSkill Demand:")
print(skill_df)