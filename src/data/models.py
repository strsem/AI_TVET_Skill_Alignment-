from dataclasses import dataclass


@dataclass
class JobPosting:
    title: str
    company: str
    skills: list[str]
    experience: str = ""