from src.llm.schemas import SkillExtractionResult

from src.skills.skill_ontology import (
    get_skill_category,
    get_parent_skill
)

from src.skills.skill_segmenter import (
    segment_skill
)


_IMPORTANCE_RANK = {
    "Required": 2,
    "Preferred": 1
}


def normalize_extracted_skills(
    result: SkillExtractionResult
) -> list[dict]:

    normalized_by_canonical = {}

    for extracted_skill in result.skills:

        original_skill = extracted_skill.skill

        canonical_skills = segment_skill(
            original_skill
        )

        for canonical_skill in canonical_skills:

            ontology_category = get_skill_category(
                canonical_skill
            )

            parent_skill = get_parent_skill(
                canonical_skill
            )

            candidate = {
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

            existing = normalized_by_canonical.get(
                canonical_skill
            )

            if existing is None:

                normalized_by_canonical[
                    canonical_skill
                ] = candidate

                continue

            existing["original_skill"] = (
                f"{existing['original_skill']}, "
                f"{candidate['original_skill']}"
            )

            existing["evidence"] = (
                f"{existing['evidence']} | "
                f"{candidate['evidence']}"
            )

            if (
                _IMPORTANCE_RANK.get(
                    candidate["importance"],
                    0
                )
                >
                _IMPORTANCE_RANK.get(
                    existing["importance"],
                    0
                )
            ):
                existing["importance"] = (
                    candidate["importance"]
                )

    return list(
        normalized_by_canonical.values()
    )