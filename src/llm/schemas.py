from typing import Literal, Optional

from pydantic import BaseModel


class ExtractedSkill(BaseModel):

    skill: str

    category: str

    importance: Literal[
        "Required",
        "Preferred"
    ]

    proficiency: Literal[
        "Advanced",
        "Intermediate",
        "Beginner",
        "Not specified"
    ]

    evidence: str


class ExtractedRequirement(BaseModel):

    requirement: str

    type: Literal[
        "Experience",
        "Education",
        "Language",
        "Other"
    ]

    value: Optional[str] = None

    evidence: str


class SkillExtractionResult(BaseModel):

    skills: list[ExtractedSkill]

    requirements: list[ExtractedRequirement] = []