from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class SkillConcept:
    skill_id: str
    canonical_name: str

    aliases: List[str] = field(default_factory=list)
    category: Optional[str] = None
    parent_skill: Optional[str] = None
    child_skills: List[str] = field(default_factory=list)
    related_skills: List[str] = field(default_factory=list)

# Skill Ontology
SKILL_ONTOLOGY = {
    "python": SkillConcept(
        skill_id="SKILL_001",
        canonical_name="Python",
        aliases=[
            "python",
            "python programming"
        ],
        category="Programming Language"
    ),

    "git": SkillConcept(
        skill_id="SKILL_002",
        canonical_name="Git",
        aliases=[
            "git",
            "git version control",
            "git versioning"
        ],
        category="Version Control"
    ),

    "docker": SkillConcept(
        skill_id="SKILL_003",
        canonical_name="Docker",
        aliases=[
            "docker",
            "docker container"
        ],
        category="DevOps"
    ),

    "tensorflow": SkillConcept(
        skill_id="SKILL_004",
        canonical_name="TensorFlow",
        aliases=[
            "tensorflow"
        ],
        category="Machine Learning"
    ),

    "pytorch": SkillConcept(
        skill_id="SKILL_005",
        canonical_name="PyTorch",
        aliases=[
            "pytorch"
        ],
        category="Machine Learning"
    ),

    "nlp": SkillConcept(
        skill_id="SKILL_006",
        canonical_name="Natural Language Processing",
        aliases=[
            "nlp",
            "natural language processing"
        ],
        category="Artificial Intelligence",
        child_skills=[
            "Transformer",
            "BERT",
            "GPT"
        ]
    ),

    "transformer": SkillConcept(
        skill_id="SKILL_007",
        canonical_name="Transformer",
        aliases=[
            "transformer",
            "transformers"
        ],
        category="Deep Learning",
        parent_skill="Natural Language Processing"
    ),

    "bert": SkillConcept(
        skill_id="SKILL_008",
        canonical_name="BERT",
        aliases=[
            "bert"
        ],
        category="NLP",
        parent_skill="Natural Language Processing"
    ),

    "gpt": SkillConcept(
        skill_id="SKILL_009",
        canonical_name="GPT",
        aliases=[
            "gpt",
            "generative pre-trained transformer"
        ],
        category="NLP",
        parent_skill="Natural Language Processing"
    ),

    "hugging_face_transformers": SkillConcept(
        skill_id="SKILL_010",
        canonical_name="Hugging Face Transformers",
        aliases=[
            "hugging face transformers",
            "huggingface transformers"
        ],
        category="NLP / Deep Learning"
    ),

    "fastapi": SkillConcept(
        skill_id="SKILL_011",
        canonical_name="FastAPI",
        aliases=[
            "fastapi"
        ],
        category="Web Development"
    ),

    "rag": SkillConcept(
        skill_id="SKILL_012",
        canonical_name="RAG",
        aliases=[
            "rag",
            "retrieval augmented generation",
            "retrieval-augmented generation"
        ],
        category="Generative AI"
    ),

    "vector_database": SkillConcept(
        skill_id="SKILL_013",
        canonical_name="Vector Database",
        aliases=[
            "vector database",
            "vector db",
            "vector databases"
        ],
        category="Database"
    ),

    "neo4j": SkillConcept(
        skill_id="SKILL_014",
        canonical_name="Neo4j",
        aliases=[
            "neo4j"
        ],
        category="Graph Database"
    ),

    "cypher": SkillConcept(
        skill_id="SKILL_015",
        canonical_name="Cypher",
        aliases=[
            "cypher"
        ],
        category="Query Language"
    ),
"microservices": SkillConcept(
        skill_id="SKILL_016",
        canonical_name="Microservices",
        aliases=[
            "microservices",
            "microservice architecture"
        ],
        category="Software Architecture"
    ),
    "ci_cd": SkillConcept(
        skill_id="SKILL_017",
        canonical_name="CI/CD",
        aliases=[
            "ci/cd",
            "continuous integration",
            "continuous delivery",
            "continuous deployment"
        ],
        category="DevOps"
    ),
    "devops": SkillConcept(
        skill_id="SKILL_018",
        canonical_name="DevOps",
        aliases=[
            "devops"
        ],
        category="DevOps"
    )
}

# Lookup
def get_skill_concept(skill_name: str) -> Optional[SkillConcept]:
    normalized_name = skill_name.strip().lower()
    for concept in SKILL_ONTOLOGY.values():
        if normalized_name == concept.canonical_name.lower():
            return concept

        for alias in concept.aliases:
            if normalized_name == alias.lower():
                return concept
    return None


# Get canonical skill name
def get_canonical_name(skill_name: str) -> str:
    concept = get_skill_concept(skill_name)
    if concept is None:
        return skill_name
    return concept.canonical_name

# Get parent skill
def get_parent_skill(skill_name: str) -> Optional[str]:
    concept = get_skill_concept(skill_name)
    if concept is None:
        return None
    return concept.parent_skill

from dataclasses import dataclass, field


@dataclass
class Skill:
    name: str
    category: str
    parent: str | None = None
    aliases: list[str] = field(default_factory=list)


@dataclass
class Requirement:
    skills: list[str]
    logic: str = "AND"
    importance: str = "Required"