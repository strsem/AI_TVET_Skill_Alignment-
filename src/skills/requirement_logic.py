from dataclasses import dataclass
from typing import List


@dataclass
class RequirementGroup:
    requirement_id: str
    logic: str
    skills: List[str]
    category: str
    description: str


def create_or_requirement(
    requirement_id: str,
    skills: List[str],
    category: str = "Alternative"
) -> RequirementGroup:

    if not skills:
        raise ValueError("skills cannot be empty")

    description = "At least one of: " + ", ".join(skills)

    return RequirementGroup(
        requirement_id=requirement_id,
        logic="OR",
        skills=skills,
        category=category,
        description=description
    )


def create_and_requirement(
    requirement_id: str,
    skills: List[str],
    category: str = "Combined"
) -> RequirementGroup:

    if not skills:
        raise ValueError("skills cannot be empty")

    description = "All of: " + ", ".join(skills)

    return RequirementGroup(
        requirement_id=requirement_id,
        logic="AND",
        skills=skills,
        category=category,
        description=description
    )


def requirement_to_text(requirement: RequirementGroup) -> str:

    operator = f" {requirement.logic} "

    return operator.join(requirement.skills)


def create_requirement(
    requirement_id: str,
    skills: List[str],
    logic: str = "AND",
    category: str = "General"
) -> RequirementGroup:

    if logic == "AND":
        return create_and_requirement(
            requirement_id=requirement_id,
            skills=skills,
            category=category
        )

    if logic == "OR":
        return create_or_requirement(
            requirement_id=requirement_id,
            skills=skills,
            category=category
        )

    raise ValueError("logic must be AND or OR")