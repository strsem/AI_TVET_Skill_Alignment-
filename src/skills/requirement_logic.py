from dataclasses import dataclass
from typing import List

@dataclass
class RequirementGroup:
    requirement_id: str
    logic: str
    skills: List[str]
    category: str
    description: str

# Create OR requirement
def create_or_requirement(
    requirement_id: str,
    skills: List[str],
    category: str = "Alternative",
) -> RequirementGroup:

    description = "At least one of: " + ", ".join(skills)
    return RequirementGroup(
        requirement_id=requirement_id,
        logic="OR",
        skills=skills,
        category=category,
        description=description
    )

# Create AND requirement
def create_and_requirement(
    requirement_id: str,
    skills: List[str],
    category: str = "Combined",
) -> RequirementGroup:

    description = "All of: " + ", ".join(skills)
    return RequirementGroup(
        requirement_id=requirement_id,
        logic="AND",
        skills=skills,
        category=category,
        description=description
    )

# Example requirements
REQUIREMENT_GROUPS = [

    create_or_requirement(
        requirement_id="REQ_001",
        skills=[
            "TensorFlow",
            "PyTorch"
        ],
        category="Deep Learning Framework"
    ),

    create_and_requirement(
        requirement_id="REQ_002",
        skills=[
            "Web Service",
            "FastAPI"
        ],
        category="Backend Development"
    ),

    create_and_requirement(
        requirement_id="REQ_003",
        skills=[
            "Transformer",
            "BERT",
            "GPT"
        ],
        category="NLP"
    )
]

# Print requirements
def print_requirements():
    for requirement in REQUIREMENT_GROUPS:
        print("\nRequirement:", requirement.requirement_id)
        print("Logic:", requirement.logic)
        print("Skills:", requirement.skills)
        print("Category:", requirement.category)
        print("Description:", requirement.description)