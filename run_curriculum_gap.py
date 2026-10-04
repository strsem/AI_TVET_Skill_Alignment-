import json
from pathlib import Path

from src.data.job_description_loader import (
    load_job_descriptions
)

from src.pipeline.market_skill_pipeline import (
    build_market_skill_profile
)

from src.skills.curriculum_gap import (
    analyze_curriculum_gap,
    print_curriculum_gap_report
)




BASE_DIR = Path(__file__).resolve().parent

JOB_FILE = (
    BASE_DIR
    / "data"
    / "raw"
    / "job_descriptions.json"
)

CURRICULUM_FILE = (
    BASE_DIR
    / "data"
    / "raw"
    / "tvet_curriculum.json"
)

OUTPUT_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "curriculum_gap_report.json"
)





# ---------------------------------------------------------
# Load job descriptions
# ---------------------------------------------------------

job_descriptions = load_job_descriptions(
    JOB_FILE
)


# ---------------------------------------------------------
# Build market profile
# ---------------------------------------------------------

market_profile = build_market_skill_profile(
    job_descriptions,
    model="qwen3:4b"
)


# ---------------------------------------------------------
# Load TVET curriculum
# ---------------------------------------------------------

with open(
    CURRICULUM_FILE,
    "r",
    encoding="utf-8"
) as file:

    curriculum_skills = json.load(
        file
    )


# ---------------------------------------------------------
# Analyze curriculum gap
# ---------------------------------------------------------
gap_report = analyze_curriculum_gap(
    market_profile,
    curriculum_skills
)


# ---------------------------------------------------------
# Print report
# ---------------------------------------------------------

print_curriculum_gap_report(
    gap_report
)


# ---------------------------------------------------------
# Save report
# ---------------------------------------------------------

output_path = Path(
    OUTPUT_FILE
)

output_path.parent.mkdir(
    parents=True,
    exist_ok=True
)

with open(
    output_path,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        gap_report,
        file,
        ensure_ascii=False,
        indent=2
    )


print(
    f"\nReport saved to: {OUTPUT_FILE}"
)