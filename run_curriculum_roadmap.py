from src.skills.curriculum_roadmap import (
    CurriculumRoadmapBuilder,
    load_json,
    save_json
)


INPUT_PATH = (
    "data/processed/"
    "curriculum_recommendation_report.json"
)

OUTPUT_PATH = (
    "data/processed/"
    "curriculum_roadmap.json"
)


def main():

    recommendation_report = load_json(
        INPUT_PATH
    )

    builder = CurriculumRoadmapBuilder()

    result = builder.build(
        recommendation_report
    )

    save_json(
        result,
        OUTPUT_PATH
    )

    print("=" * 70)
    print("CURRICULUM ROADMAP")
    print("=" * 70)

    print()

    for area in result["roadmap"]:

        print(
            f"{area['sequence']}. "
            f"[{area['priority']}] "
            f"{area['curriculum_area']}"
        )

        print(
            f"   Phase: {area['phase']}"
        )

        print(
            "   Skills: "
            + ", ".join(
                area["skills"]
            )
        )

        print(
            "   Prerequisite curriculum areas: "
            + (
                ", ".join(
                    area[
                        "prerequisite_curriculum_areas"
                    ]
                )
                if area[
                    "prerequisite_curriculum_areas"
                ]
                else "None"
            )
        )

        print(
            "   Prerequisite skills: "
            + (
                ", ".join(
                    area[
                        "prerequisite_skills"
                    ]
                )
                if area[
                    "prerequisite_skills"
                ]
                else "None"
            )
        )

        print(
            "   Related areas: "
            + (
                ", ".join(
                    area["related_areas"]
                )
                if area["related_areas"]
                else "None"
            )
        )

        print(
            "   Topics: "
            + ", ".join(
                area["recommended_topics"]
            )
        )

        print()

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)

    print(
        "Original areas: "
        f"{result['summary']['original_areas']}"
    )

    print(
        "Consolidated areas: "
        f"{result['summary']['consolidated_areas']}"
    )

    print(
        "High priority: "
        f"{result['summary']['high_priority_areas']}"
    )

    print(
        "Medium priority: "
        f"{result['summary']['medium_priority_areas']}"
    )

    print()

    print(
        f"Report saved to: {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()
