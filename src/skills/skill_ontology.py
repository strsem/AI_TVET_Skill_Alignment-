import re
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


SKILL_ONTOLOGY = {

    "python": SkillConcept(
        skill_id="SKILL_001",
        canonical_name="Python",
        aliases=[
            "python",
            "python programming",
            "python developer",
            "python language"
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
        aliases=["tensorflow"],
        category="Machine Learning"
    ),

    "pytorch": SkillConcept(
        skill_id="SKILL_005",
        canonical_name="PyTorch",
        aliases=["pytorch"],
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
        aliases=["bert"],
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
            "fastapi",
            "fast api"
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
        aliases=["neo4j"],
        category="Graph Database"
    ),

    "cypher": SkillConcept(
        skill_id="SKILL_015",
        canonical_name="Cypher",
        aliases=["cypher"],
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
        aliases=["devops"],
        category="DevOps"
    ),

    "machine_learning": SkillConcept(
        skill_id="SKILL_019",
        canonical_name="Machine Learning",
        aliases=[
            "machine learning",
            "ml",
            "machine learning algorithms"
        ],
        category="Machine Learning"
    ),

    "rest_api": SkillConcept(
        skill_id="SKILL_020",
        canonical_name="REST API",
        aliases=[
            "rest api",
            "rest apis",
            "restful api",
            "restful apis"
        ],
        category="Web Development"
    ),

    "llm": SkillConcept(
        skill_id="SKILL_021",
        canonical_name="LLM",
        aliases=[
            "llm",
            "large language model",
            "large language models"
        ],
        category="Artificial Intelligence"
    ),
"ai_agents": SkillConcept(
        skill_id="SKILL_022",
        canonical_name="AI Agents",
        aliases=[
            "ai agent",
            "ai agents",
            "agentic ai",
            "agentic systems",
            "agentic system"
        ],
        category="Artificial Intelligence"
    ),

    "function_calling": SkillConcept(
        skill_id="SKILL_023",
        canonical_name="Function Calling",
        aliases=[
            "function calling"
        ],
        category="Generative AI"
    ),

    "tool_calling": SkillConcept(
        skill_id="SKILL_024",
        canonical_name="Tool Calling",
        aliases=[
            "tool calling"
        ],
        category="Generative AI"
    ),

    "embeddings": SkillConcept(
        skill_id="SKILL_025",
        canonical_name="Embeddings",
        aliases=[
            "embedding",
            "embeddings"
        ],
        category="Generative AI"
    ),

    "postgresql": SkillConcept(
        skill_id="SKILL_026",
        canonical_name="PostgreSQL",
        aliases=[
            "postgresql",
            "postgres"
        ],
        category="Database"
    ),

    "linux": SkillConcept(
        skill_id="SKILL_027",
        canonical_name="Linux",
        aliases=[
            "linux"
        ],
        category="Operating System"
    ),

    "langchain": SkillConcept(
        skill_id="SKILL_028",
        canonical_name="LangChain",
        aliases=[
            "langchain"
        ],
        category="AI Framework"
    ),

    "langgraph": SkillConcept(
        skill_id="SKILL_029",
        canonical_name="LangGraph",
        aliases=[
            "langgraph"
        ],
        category="AI Framework"
    ),

    "mcp": SkillConcept(
        skill_id="SKILL_030",
        canonical_name="MCP",
        aliases=[
            "mcp",
            "model context protocol"
        ],
        category="AI Infrastructure"
    ),

    "redis": SkillConcept(
        skill_id="SKILL_031",
        canonical_name="Redis",
        aliases=[
            "redis"
        ],
        category="Database"
    ),

    "n8n": SkillConcept(
        skill_id="SKILL_032",
        canonical_name="n8n",
        aliases=[
            "n8n"
        ],
        category="Automation"
    ),

    "prompt_engineering": SkillConcept(
        skill_id="SKILL_033",
        canonical_name="Prompt Engineering",
        aliases=[
            "prompt engineering"
        ],
        category="Generative AI"
    ),

    "context_engineering": SkillConcept(
        skill_id="SKILL_034",
        canonical_name="Context Engineering",
        aliases=[
            "context engineering",
            "context management"
        ],
        category="Generative AI"
    ),




"ai_agents": SkillConcept(
        skill_id="SKILL_022",
        canonical_name="AI Agents",
        aliases=[
            "ai agent",
            "ai agents",
            "agentic ai",
            "agentic systems",
            "agentic system",
            "ai agent systems"
        ],
        category="Artificial Intelligence"
    ),

    "context_generation": SkillConcept(
        skill_id="SKILL_023",
        canonical_name="Context Generation",
        aliases=[
            "context generation",
            "context generation for llm"
        ],
        category="Generative AI"
    ),

    "tool_integration": SkillConcept(
        skill_id="SKILL_024",
        canonical_name="Tool Integration",
        aliases=[
            "tool integration",
            "tools integration"
        ],
        category="Artificial Intelligence"
    ),

    "educational_data_analysis": SkillConcept(
        skill_id="SKILL_025",
        canonical_name="Educational Data Analysis",
        aliases=[
            "educational data analysis",
            "education data analysis"
        ],
        category="Data Analysis"
    ),

    "personalized_output_generation": SkillConcept(
        skill_id="SKILL_026",
        canonical_name="Personalized Output Generation",
        aliases=[
            "personalized output generation",
            "personalized outputs"
        ],
        category="Generative AI"
    ),

}







def get_skill_concept(skill_name: str) -> Optional[SkillConcept]:
    def get_skill_concept(
            skill_name: str
    ) -> Optional[SkillConcept]:

        normalized_name = normalize_skill_text(
            skill_name
        )

        # 1. Exact matching
        # ---------------------------------
        for concept in SKILL_ONTOLOGY.values():
            canonical_name = normalize_skill_text(
                concept.canonical_name
            )
            if normalized_name == canonical_name:
                return concept
            for alias in concept.aliases:
                normalized_alias = normalize_skill_text(
                    alias
                )

                if normalized_name == normalized_alias:
                    return concept

                # 2. Phrase matching

            candidates = []
            for concept in SKILL_ONTOLOGY.values():
                candidates.append(
                    (
                        normalize_skill_text(
                            concept.canonical_name
                        ),
                        concept
                    )
                )

                for alias in concept.aliases:
                    candidates.append(
                        (
                            normalize_skill_text(alias),
                            concept
                        )
                    )
                    candidates.sort(
                        key=lambda item: len(item[0]),
                        reverse=True
                    )

                    for phrase, concept in candidates:

                        if not phrase:
                            continue

                        pattern = (
                                r"(?<!\w)"
                                + re.escape(phrase)
                                + r"(?!\w)"
                        )

                        if re.search(
                                pattern,
                                normalized_name
                        ):
                            return concept

                    return None








def get_canonical_name(skill_name: str) -> str:
    concept = get_skill_concept(skill_name)

    if concept is None:
        return skill_name.strip()

    return concept.canonical_name


def get_parent_skill(skill_name: str) -> Optional[str]:
    concept = get_skill_concept(skill_name)

    if concept is None:
        return None

    return concept.parent_skill


def get_child_skills(skill_name: str) -> List[str]:
    concept = get_skill_concept(skill_name)

    if concept is None:
        return []

    return concept.child_skills


def get_skill_category(skill_name: str) -> Optional[str]:
    concept = get_skill_concept(skill_name)

    if concept is None:
        return None

    return concept.category






def normalize_skill_text(text: str) -> str:
    """
    Normalize text before ontology matching.
    """

    if not text:
        return ""

    text = text.strip().lower()

    prefixes = [
        "high proficiency in",
        "advanced proficiency in",
        "professional proficiency in",
        "proficient in",
        "experience in",
        "practical experience in",
        "hands-on experience with",
        "hands-on experience in",
        "experience with",

        "تسلط حرفه‌ای به",
        "تسلط حرفه ای به",
        "تسلط به",
    ]

    for prefix in prefixes:

        if text.startswith(prefix):
            text = text[len(prefix):].strip()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text