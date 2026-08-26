import pandas as pd

from src.skills.skill_normalizer import normalize_skill


def create_job_skill_matrix(
        df: pd.DataFrame
) -> pd.DataFrame:

    rows = []

    for _, row in df.iterrows():

        job_title = row["title"]

        # -------------------------
        # Required Skills
        # -------------------------

        for skill in row["required_skills"]:

            normalized_skill = normalize_skill(skill)

            rows.append({
                "job_title": job_title,
                "skill": normalized_skill,
                "importance": "Required"
            })

        # -------------------------
        # Preferred Skills
        # -------------------------

        for skill in row["preferred_skills"]:

            normalized_skill = normalize_skill(skill)

            rows.append({
                "job_title": job_title,
                "skill": normalized_skill,
                "importance": "Preferred"
            })

    return pd.DataFrame(rows)