import json
from ..data.models import JobPosting

def load_job_postings(file_path: str) -> list[JobPosting]:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    jobs = []

    for item in data:
        job = JobPosting(
            title=item["title"],
            company=item["company"],
            skills=item["skills"],
            experience=item.get("experience", "")
        )

        jobs.append(job)

    return jobs