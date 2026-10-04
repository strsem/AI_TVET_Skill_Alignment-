from typing import Dict, List

from src.skills.skill_ontology import get_canonical_name
from src.skills.skill_type_classifier import classify_skill_type


HIGH_GAP_THRESHOLD = 50.0

NOT_DIRECT_GAP_TYPES = {
    "MODEL",
    "FRAMEWORK",
}


def normalize_curriculum_skills(
    curriculum_skills: List[str],
) -> tuple[set[str], List[str]]:
    """
    Convert curriculum skill names to canonical ontology names.

    Returns:
        canonical_skills:
            Known curriculum skills in canonical form.
        unknown_skills:
            Curriculum skills that are not found in the ontology.
    """

    canonical_skills = set()
    unknown_skills = []

    for skill in curriculum_skills:
        canonical_skill = get_canonical_name(skill)

        if canonical_skill is None:
            unknown_skills.append(skill)
            continue

        canonical_skills.add(canonical_skill)

    return canonical_skills, unknown_skills


def analyze_curriculum_gap(
    market_profile: Dict[str, Dict],
    curriculum_skills: List[str],
    high_gap_threshold: float = HIGH_GAP_THRESHOLD,
) -> Dict:
    """
    Compare market-demanded skills with TVET curriculum skills.

    Classification logic:

        SKILL      -> can be a curriculum gap
        TOOL       -> can be a curriculum gap
        FRAMEWORK  -> NOT DIRECT GAP
        MODEL      -> NOT DIRECT GAP
    """

    canonical_curriculum_skills, unknown_curriculum_skills = (
        normalize_curriculum_skills(curriculum_skills)
    )

    report = {
        "summary": {
            "total_market_skills": len(market_profile),
            "total_curriculum_skills": len(canonical_curriculum_skills),
        },
        "high_gap": [],
        "medium_gap": [],
        "covered": [],
        "not_direct_gap": [],
        "unknown_curriculum_skills": unknown_curriculum_skills,
    }

    for skill, market_data in market_profile.items():

        skill_type = classify_skill_type(skill)

        market_demand = market_data["market_coverage"]

        record = {
            "skill": skill,
            "skill_type": skill_type,
            "job_count": market_data["job_count"],
            "total_jobs": market_data["total_jobs"],
            "market_demand": market_demand,
            "curriculum_covered": skill in canonical_curriculum_skills,
        }

        # ---------------------------------------------------------
        # 1. Models and frameworks are not direct curriculum gaps.
        # ---------------------------------------------------------
        if skill_type in NOT_DIRECT_GAP_TYPES:
            record["gap_level"] = "NOT DIRECT GAP"
            report["not_direct_gap"].append(record)
            continue

        # ---------------------------------------------------------
        # 2. Skills that already exist in curriculum are covered.
        # ---------------------------------------------------------
        if skill in canonical_curriculum_skills:
            record["gap_level"] = "COVERED"
            report["covered"].append(record)
            continue

        # ---------------------------------------------------------
        # 3. Remaining skills/tools can be curriculum gaps.
        # ---------------------------------------------------------
        if market_demand >= high_gap_threshold:
            record["gap_level"] = "HIGH GAP"
            report["high_gap"].append(record)
        else:
            record["gap_level"] = "MEDIUM GAP"
            report["medium_gap"].append(record)

    # Sort by market demand
    for key in [
        "high_gap",
        "medium_gap",
        "covered",
        "not_direct_gap",
    ]:
        report[key].sort(
            key=lambda item: item["market_demand"],
            reverse=True,
        )

    # Add useful counts to summary
    report["summary"]["high_gap_count"] = len(report["high_gap"])
    report["summary"]["medium_gap_count"] = len(report["medium_gap"])
    report["summary"]["covered_count"] = len(report["covered"])
    report["summary"]["not_direct_gap_count"] = len(
        report["not_direct_gap"]
    )

    return report


def print_curriculum_gap_report(report: Dict) -> None:
    """
    Print the curriculum gap report in a readable format.
    """

    print("=" * 70)
    print("TVET CURRICULUM GAP ANALYSIS")
    print("=" * 70)

    print("\nHIGH GAP")
    print("-" * 70)

    for item in report["high_gap"]:
        print(
            f"{item['skill']:<30}"
            f"{item['market_demand']:.2f}% "
            f"({item['job_count']}/{item['total_jobs']})"
            f"  [{item['skill_type']}]"
        )

    print("\nMEDIUM GAP")
    print("-" * 70)

    for item in report["medium_gap"]:
        print(
            f"{item['skill']:<30}"
            f"{item['market_demand']:.2f}% "
            f"({item['job_count']}/{item['total_jobs']})"
            f"  [{item['skill_type']}]"
        )

    print("\nCOVERED")
    print("-" * 70)

    for item in report["covered"]:
        print(
            f"{item['skill']:<30}"
            f"{item['market_demand']:.2f}% "
            f"({item['job_count']}/{item['total_jobs']})"
            f"  [{item['skill_type']}]"
        )

    print("\nNOT DIRECT GAP")
    print("-" * 70)

    for item in report["not_direct_gap"]:
        print(
            f"{item['skill']:<30}"
            f"{item['market_demand']:.2f}% "
            f"({item['job_count']}/{item['total_jobs']})"
            f"  [{item['skill_type']}]"
        )

    print("\nUNKNOWN CURRICULUM SKILLS")
    print("-" * 70)

    if report["unknown_curriculum_skills"]:
        for skill in report["unknown_curriculum_skills"]:
            print(skill)
    else:
        print("None")

    print("\nSUMMARY")
    print("-" * 70)
    print(
        f"Market skills:      "
        f"{report['summary']['total_market_skills']}"
    )
    print(
        f"Curriculum skills:  "
        f"{report['summary']['total_curriculum_skills']}"
    )
    print(
        f"High gaps:          "
        f"{report['summary']['high_gap_count']}"
    )
    print(
        f"Medium gaps:        "
        f"{report['summary']['medium_gap_count']}"
    )
    print(
        f"Covered:            "
        f"{report['summary']['covered_count']}"
    )
    print(
        f"Not direct gaps:    "
        f"{report['summary']['not_direct_gap_count']}"
    )
