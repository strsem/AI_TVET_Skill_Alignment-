from src.skills.skill_ontology import get_canonical_name


def normalize_skill(skill: str) -> str:
    """
    Convert a skill name into its canonical ontology name.

    Single source of truth is skill_ontology.py — this
    function only delegates to it, it does not keep its
    own alias table.
    """

    if not skill:
        return ""

    return get_canonical_name(skill)