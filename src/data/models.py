from dataclasses import dataclass


@dataclass
class JobPosting:
    title: str
    company: str
    description: str
    experience: str = ""