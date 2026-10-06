from src.skills.curriculum_alignment import (
    CurriculumAligner,
    load_json,
    save_json
)


ROADMAP_PATH = (
    "data/processed/"
    "curriculum_roadmap.json"
)

CURRICULUM_PATH = (
    "data/raw/"
    "tvet_curriculum.json"
)

ALIAS_PATH = (
    "data/raw/"
    "curriculum_alignment_aliases.json"
)

OUTPUT_PATH = (
    "data/processed/"
    "curriculum_alignment_report.json"
)


def main():

    roadmap = load_json(
        ROADMAP_PATH
    )

    curriculum = load_json(
        CURRICULUM_PATH
    )

    aliases = load_json(
        ALIAS_PATH
    )

    aligner = CurriculumAligner(
        aliases
    )

    result = aligner.align(
        roadmap,
        curriculum
    )

    save_json(
        result,
        OUTPUT_PATH
    )

    print("=" * 70)
    print("CURRICULUM ALIGNMENT")
    print("=" * 70)

    print()

    for area in result["areas"]:

        print(
            f"[{area['status']}] "
            f"{area['curriculum_area']}"
        )

        print(
            "  Core skills covered: "
            + (
                ", ".join(
                    area[
                        "covered_core_skills"
                    ]
                )
                if area[
                    "covered_core_skills"
                ]
                else "None"
            )
        )

        print(
            "  Core skills missing: "
            + (
                ", ".join(
                    area[
                        "missing_core_skills"
                    ]
                )
                if area[
                    "missing_core_skills"
                ]
                else "None"
            )
        )

        print(
            "  Prerequisite skills covered: "
            + (
                ", ".join(
                    area[
                        "covered_prerequisite_skills"
                    ]
                )
                if area[
                    "covered_prerequisite_skills"
                ]
                else "None"
            )
        )

        print(
            "  Prerequisite skills missing: "
            + (
                ", ".join(
                    area[
                        "missing_prerequisite_skills"
                    ]
                )
                if area[
                    "missing_prerequisite_skills"
                ]
                else "None"
            )
        )

        print()

    print("=" * 70)
    print("UNMAPPED CURRICULUM SKILLS")
    print("=" * 70)

    if result[
        "unmapped_curriculum_skills"
    ]:

        for skill in result[
            "unmapped_curriculum_skills"
        ]:
            print(f"- {skill}")

    else:
        print("None")

    print()

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)

    for key, value in result[
        "summary"
    ].items():

        print(
            f"{key}: {value}"
        )

    print()

    print(
        f"Report saved to: {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()