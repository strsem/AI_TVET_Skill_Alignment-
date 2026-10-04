import re

from src.skills.requirement_logic import (
    RequirementGroup,
    create_requirement
)

from src.skills.skill_ontology import get_canonical_name


def _canonical_or_original(skill: str) -> str:
    """
    Return the canonical skill name when it exists.
    Otherwise, keep the original skill name.
    """

    skill = skill.strip()

    if not skill:
        raise ValueError("skill cannot be empty")

    canonical_name = get_canonical_name(skill)

    return canonical_name if canonical_name else skill


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


def parse_requirement_text(
    requirement_id: str,
    text: str,
    category: str = "General"
) -> RequirementGroup:

    text = text.strip()

    if not text:
        raise ValueError(
            "requirement text cannot be empty"
        )

    has_or = bool(
        re.search(r"\s+or\s+", text, re.IGNORECASE)
    )

    has_and = bool(
        re.search(r"\s+and\s+", text, re.IGNORECASE)
    )

    # -------------------------
    # Mixed AND / OR
    # -------------------------

    if has_or and has_and:
        raise ValueError(
            "mixed AND/OR in a single requirement "
            f"is not supported: {text!r}. Split it "
            "into separate requirements first."
        )

    # -------------------------
    # OR requirement
    # -------------------------

    if has_or:
        parts = re.split(
            r"\s+or\s+",
            text,
            flags=re.IGNORECASE
        )

        skills = [
            _canonical_or_original(part)
            for part in parts
            if part.strip()
        ]

        return create_requirement(
            requirement_id=requirement_id,
            skills=skills,
            logic="OR",
            category=category
        )

    # -------------------------
    # AND requirement
    # -------------------------

    if has_and:
        parts = re.split(
            r"\s+and\s+",
            text,
            flags=re.IGNORECASE
        )

        skills = [
            _canonical_or_original(part)
            for part in parts
            if part.strip()
        ]

        return create_requirement(
            requirement_id=requirement_id,
            skills=skills,
            logic="AND",
            category=category
        )

    # -------------------------
    # Single skill
    # -------------------------

    skill = _canonical_or_original(text)

    return create_requirement(
        requirement_id=requirement_id,
        skills=[skill],
        logic="AND",
        category=category
    )