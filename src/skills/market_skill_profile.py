from collections import defaultdict
from typing import Dict, List
from src.skills.skill_ontology import get_canonical_name

def calculate_market_skill_profile(
    jobs: List[List[str]]
) -> Dict[str, Dict]:
    """
    Calculate market demand for skills across job postings.
    Each job is represented as a list of skills.
    """

    total_jobs = len(jobs)

    if total_jobs == 0:
        return {}

    skill_job_count = defaultdict(int)

    for job in jobs:

        # جلوگیری از شمارش تکراری یک مهارت
        # در یک آگهی شغلی
        canonical_skills = set()

        for skill in job:

            canonical_skill = get_canonical_name(skill)

            canonical_skills.add(canonical_skill)

        for skill in canonical_skills:
            skill_job_count[skill] += 1

    market_profile = {}

    for skill, job_count in skill_job_count.items():

        market_coverage = (
            job_count / total_jobs
        ) * 100

        market_profile[skill] = {
            "job_count": job_count,
            "total_jobs": total_jobs,
            "market_coverage": round(
                market_coverage,
                2
            )
        }

    return market_profile


def sort_market_profile(
    market_profile: Dict[str, Dict]
) -> List:

    return sorted(
        market_profile.items(),
        key=lambda item: item[1]["job_count"],
        reverse=True
    )


def print_market_skill_profile(
    market_profile: Dict[str, Dict]
):

    print("\n")
    print("=" * 70)
    print("MARKET SKILL PROFILE")
    print("=" * 70)

    sorted_skills = sort_market_profile(
        market_profile
    )

    for skill, data in sorted_skills:

        print("\nSkill:", skill)

        print(
            "Job Count       :",
            data["job_count"]
        )

        print(
            "Total Jobs      :",
            data["total_jobs"]
        )

        print(
            "Market Coverage :",
            f"{data['market_coverage']}%"
        )