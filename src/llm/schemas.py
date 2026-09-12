from dataclasses import dataclass


@dataclass
class ExtractedSkill:
    skill: str
    importance: str
    evidence: str