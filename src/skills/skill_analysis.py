import pandas as pd


def analyze_skill_importance(
        df: pd.DataFrame
) -> pd.DataFrame:

    total_jobs = len(df)

    skill_data = {}

    for _, row in df.iterrows():

        required_skills = row["required_skills"]
        preferred_skills = row["preferred_skills"]

        # -------------------------
        # Required Skills
        # -------------------------

        for skill in required_skills:

            skill = skill.strip()

            if skill not in skill_data:
                skill_data[skill] = {
                    "job_count": 0,
                    "required_count": 0,
                    "preferred_count": 0
                }

            skill_data[skill]["job_count"] += 1
            skill_data[skill]["required_count"] += 1

        # -------------------------
        # Preferred Skills
        # -------------------------

        for skill in preferred_skills:

            skill = skill.strip()

            if skill not in skill_data:
                skill_data[skill] = {
                    "job_count": 0,
                    "required_count": 0,
                    "preferred_count": 0
                }

            skill_data[skill]["job_count"] += 1
            skill_data[skill]["preferred_count"] += 1

    # -------------------------
    # Create DataFrame
    # -------------------------

    skill_df = pd.DataFrame.from_dict(
        skill_data,
        orient="index"
    )

    skill_df.index.name = "skill"

    skill_df = skill_df.reset_index()

    # -------------------------
    # Frequency
    # -------------------------

    skill_df["frequency"] = (
        skill_df["job_count"] / total_jobs
    )

    # -------------------------
    # Required Rate
    # -------------------------

    skill_df["required_rate"] = (
        skill_df["required_count"] / total_jobs
    )

    # -------------------------
    # Preferred Rate
    # -------------------------

    skill_df["preferred_rate"] = (
        skill_df["preferred_count"] / total_jobs
    )

    # -------------------------
    # Importance Score
    # -------------------------

    skill_df["importance_score"] = (
        skill_df["frequency"] * 60
        +
        skill_df["required_rate"] * 40
    )

    # -------------------------
    # Sort
    # -------------------------

    skill_df = skill_df.sort_values(
        by="importance_score",
        ascending=False
    )

    skill_df = skill_df.reset_index(drop=True)

    return skill_df