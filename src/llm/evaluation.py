from src.llm.schemas import SkillExtractionResult


def evaluate_extraction(result: SkillExtractionResult) -> None:
    """
    Print a simple report about the extracted skills.
    """

    print("\n")
    print("=" * 90)
    print("LLM EXTRACTION EVALUATION")
    print("=" * 90)

    print(f"Total extracted skills: {len(result.skills)}")

    print("\nSkills by importance:")

    required_count = 0
    preferred_count = 0

    for skill in result.skills:

        if skill.importance == "Required":
            required_count += 1

        elif skill.importance == "Preferred":
            preferred_count += 1

    print(f"Required : {required_count}")
    print(f"Preferred: {preferred_count}")

    print("\nSkills by proficiency:")

    proficiency_counts = {}

    for skill in result.skills:

        level = skill.proficiency

        if level not in proficiency_counts:
            proficiency_counts[level] = 0

        proficiency_counts[level] += 1

    for level, count in proficiency_counts.items():
        print(f"{level:<15} : {count}")

    print("\nExtracted skill list:")

    for skill in result.skills:

        print(
            f"- {skill.skill:<35} | "
            f"{skill.importance:<10} | "
            f"{skill.proficiency}"
        )