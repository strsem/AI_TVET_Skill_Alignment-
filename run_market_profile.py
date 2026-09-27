from src.data.job_description_loader import (
    load_job_descriptions
)

from src.pipeline.market_skill_pipeline import (
    build_market_skill_profile
)


file_path = "data/raw/job_descriptions.json"


job_descriptions = load_job_descriptions(
    file_path
)


market_profile = build_market_skill_profile(
    job_descriptions,
    model="qwen3:4b"
)


print("\n")
print("FINAL MARKET SKILL PROFILE")


sorted_profile = sorted(
    market_profile.items(),
    key=lambda item: item[1]["job_count"],
    reverse=True
)


for skill, data in sorted_profile:

    print(
        f"{skill:35} "
        f"{data['job_count']}/{data['total_jobs']} "
        f"({data['market_coverage']}%)"
    )