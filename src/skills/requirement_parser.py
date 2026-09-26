from src.skills.requirement_logic import (
    RequirementGroup,
    create_requirement
)


def parse_requirement(
    requirement_id: str,
    skills: list[str],
    logic: str = "AND",
    category: str = "General"
) -> RequirementGroup:

    return create_requirement(
        requirement_id=requirement_id,
        skills=skills,
        logic=logic,
        category=category
    )