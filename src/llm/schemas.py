from typing import Literal
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

class SkillExtractionResult(BaseModel):

    skills: list[ExtractedSkill]