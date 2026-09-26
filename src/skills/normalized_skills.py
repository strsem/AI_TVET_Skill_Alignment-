from src.llm.schemas import SkillExtractionResult
from src.skills.skill_ontology import (
    get_canonical_name,
    get_skill_category,
    get_parent_skill
)


def normalize_extracted_skills(
    result: SkillExtractionResult
) -> list[dict]:

    normalized_skills = []

    for extracted_skill in result.skills:

        original_skill = extracted_skill.skill

        canonical_skill = get_canonical_name(original_skill)

        ontology_category = get_skill_category(canonical_skill)

        parent_skill = get_parent_skill(canonical_skill)

        normalized_skill = {
            "skill": canonical_skill,
            "original_skill": original_skill,
            "category": (
                ontology_category
                if ontology_category
                else extracted_skill.category
            ),
            "importance": extracted_skill.importance,
            "proficiency": extracted_skill.proficiency,
            "evidence": extracted_skill.evidence,
            "parent_skill": parent_skill
        }

        normalized_skills.append(normalized_skill)

    return normalized_skills