from src.llm.ollama_extractor import OllamaSkillExtractor
from src.skills.skill_segmenter import segment_skill
from src.skills.normalized_skills import normalize_extracted_skills


job_description = """
We are looking for a Python developer with experience
in Django, REST API, Git and SQL.

Experience with FastAPI is a plus.

Knowledge of Docker and AWS is preferred.
"""


def main():

    print("=" * 70)
    print("LOCAL OLLAMA SKILL EXTRACTION")
    print("=" * 70)

    extractor = OllamaSkillExtractor(model="qwen3:4b")

    print("\nOllama is ready.")

    result = extractor.extract(
        job_description
    )

    print("\nRAW LLM RESULT")
    print("=" * 70)

    for skill in result.skills:

        print(
            f"\nSkill: {skill.skill}"
        )

        print(
            f"Category: {skill.category}"
        )

        print(
            f"Importance: {skill.importance}"
        )

        print(
            f"Proficiency: {skill.proficiency}"
        )

        print(
            f"Evidence: {skill.evidence}"
        )

    print("\n")
    print("=" * 70)
    print("SEGMENTED SKILLS")
    print("=" * 70)

    segmented_skills = []

    for extracted_skill in result.skills:

        skills = segment_skill(
            extracted_skill.skill
        )

        segmented_skills.extend(
            skills
        )

    segmented_skills = list(
        dict.fromkeys(segmented_skills)
    )

    for skill in segmented_skills:

        print(
            f"  - {skill}"
        )

    print("\n")
    print("=" * 70)
    print("NORMALIZED SKILLS")
    print("=" * 70)

    normalized_result = normalize_extracted_skills(
        result
    )

    for skill in normalized_result:

        print(
            f"\n{skill}"
        )


if __name__ == "__main__":
    main()