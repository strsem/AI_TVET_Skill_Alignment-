from src.skills.skill_ontology import Requirement


def create_requirement(
    skills: list[str],
    logic: str = "AND",
    importance: str = "Required"
) -> Requirement:

    if logic not in {"AND", "OR"}:
        raise ValueError("logic must be AND or OR")

    return Requirement(
        skills=skills,
        logic=logic,
        importance=importance
    )


def requirement_to_text(requirement: Requirement) -> str:

    operator = f" {requirement.logic} "

    skills_text = operator.join(
        requirement.skills
    )

    return (
        f"{skills_text} "
        f"({requirement.importance})"
    )