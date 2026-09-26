from dataclasses import dataclass


@dataclass
class JobPosting:

    title: str
    company: str
    required_skills: list[str]
    preferred_skills: list[str]
    experience: str = ""