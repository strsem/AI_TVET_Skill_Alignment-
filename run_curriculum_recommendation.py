from src.skills.curriculum_recommender import (
    CurriculumRecommender,
    load_json,
    save_json
)


GAP_REPORT_PATH = (
    "data/processed/"
    "curriculum_gap_report.json"
)

RECOMMENDATION_MAP_PATH = (
    "data/raw/"
    "curriculum_recommendation_map.json"
)

OUTPUT_PATH = (
    "data/processed/"
    "curriculum_recommendation_report.json"
)


def main():

    gap_report = load_json(
        GAP_REPORT_PATH
    )

    recommendation_map = load_json(
        RECOMMENDATION_MAP_PATH
    )

    recommender = CurriculumRecommender(
        recommendation_map
    )

    result = recommender.recommend(
        gap_report
    )

    save_json(
        result,
        OUTPUT_PATH
    )

    print("=" * 70)
    print("CURRICULUM RECOMMENDATION")
    print("=" * 70)

    print()

    print("RECOMMENDED CURRICULUM AREAS:")

    for area in result["curriculum_areas"]:

        print(
            f"\n[{area['priority']}] "
            f"{area['curriculum_area']}"
        )

        print(
            "Skills: "
            + ", ".join(area["skills"])
        )

        print(
            "Topics: "
            + ", ".join(
                area["recommended_topics"]
            )
        )

    print()

    print("UNMAPPED GAPS:")

    if result["unmapped_gaps"]:

        for item in result["unmapped_gaps"]:

            print(
                f"- {item['skill']} "
                f"({item['gap_level']})"
            )

    else:
        print("None")

    print()

    print("SUMMARY:")
    print(
        f"Recommended skills: "
        f"{result['summary']['recommended_skills']}"
    )

    print(
        f"Curriculum areas: "
        f"{result['summary']['curriculum_areas']}"
    )

    print(
        f"Unmapped gaps: "
        f"{result['summary']['unmapped_gaps']}"
    )

    print()

    print(
        f"Report saved to: {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()