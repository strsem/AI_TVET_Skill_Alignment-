import re

from src.skills.requirement_logic import (
    RequirementGroup,
    create_requirement
)

from src.skills.skill_ontology import get_canonical_name


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
    # حالت مخلوط: هم "and" هم "or"
    # با هم در یک رشته.
    # مثال: "Python or Git and Docker"
    # چون RequirementGroup فقط یک منطق
    # (AND یا OR) را پشتیبانی می‌کند، این حالت
    # را به‌جای حدس اشتباه، صریحاً رد می‌کنیم
    # تا caller خودش تصمیم بگیرد (مثلاً متن را
    # دستی به چند Requirement بشکند).
    # -------------------------

    if has_or and has_and:
        raise ValueError(
            "mixed AND/OR in a single requirement "
            f"is not supported: {text!r}. Split it "
            "into separate requirements first."
        )

    # OR requirement
    if has_or:
        parts = re.split(
            r"\s+or\s+",
            text,
            flags=re.IGNORECASE
        )

        skills = [
            get_canonical_name(part.strip())
            for part in parts
            if part.strip()
        ]

        return create_requirement(
            requirement_id=requirement_id,
            skills=skills,
            logic="OR",
            category=category
        )

    # AND requirement
    if has_and:
        parts = re.split(
            r"\s+and\s+",
            text,
            flags=re.IGNORECASE
        )

        skills = [
            get_canonical_name(part.strip())
            for part in parts
            if part.strip()
        ]

        return create_requirement(
            requirement_id=requirement_id,
            skills=skills,
            logic="AND",
            category=category
        )

    # Single skill
    skill = get_canonical_name(text)

    return create_requirement(
        requirement_id=requirement_id,
        skills=[skill],
        logic="AND",
        category=category
    )