from src.llm.schemas import SkillExtractionResult
from src.skills.skill_normalizer import normalize_skill


def normalize_extracted_skills(
    result: SkillExtractionResult
) -> list[dict]:

    normalized_skills = []

    for extracted_skill in result.skills:

        normalized_skill = normalize_skill(
            extracted_skill.skill
        )

        normalized_skills.append(
            {
                "skill": normalized_skill,
                "original_skill": extracted_skill.skill,
                "category": extracted_skill.category,
                "importance": extracted_skill.importance,
                "proficiency": extracted_skill.proficiency,
                "evidence": extracted_skill.evidence
            }
        )

    return normalized_skills