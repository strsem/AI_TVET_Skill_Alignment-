import re
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class SkillConcept:
    """
    A normalized skill concept used by the TVET Skill Alignment pipeline.

    Fields are kept compatible with the existing project so other modules
    can use parent/child/related skill relationships when needed.
    """

    skill_id: str
    canonical_name: str
    aliases: List[str] = field(default_factory=list)
    category: Optional[str] = None
    parent_skill: Optional[str] = None
    child_skills: List[str] = field(default_factory=list)
    related_skills: List[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# SKILL ONTOLOGY
# ---------------------------------------------------------------------------
#
# IMPORTANT DESIGN RULES
# 1. Every dictionary key is unique.
# 2. Every skill_id is unique.
# 3. canonical_name is the name stored by the normalization layer.
# 4. aliases are alternative spellings / names.
# 5. parent_skill contains a canonical skill name.
#
# The original project had duplicate dictionary keys (especially ai_agents)
# which caused later definitions to overwrite earlier definitions. This
# version removes those collisions and keeps the original core concepts.
# ---------------------------------------------------------------------------

SKILL_ONTOLOGY = {

    # -----------------------------------------------------------------------
    # Programming / Version Control / DevOps
    # -----------------------------------------------------------------------

    "python": SkillConcept(
        skill_id="SKILL_001",
        canonical_name="Python",
        aliases=[
            "python",
            "python programming",
            "python developer",
            "python language",
        ],
        category="Programming Language",
    ),

    "git": SkillConcept(
        skill_id="SKILL_002",
        canonical_name="Git",
        aliases=[
            "git",
            "git version control",
            "git versioning",
        ],
        category="Version Control",
    ),

    "docker": SkillConcept(
        skill_id="SKILL_003",
        canonical_name="Docker",
        aliases=[
            "docker",
            "docker container",
            "docker containers",
            "containerization",
        ],
        category="DevOps",
    ),

    "tensorflow": SkillConcept(
        skill_id="SKILL_004",
        canonical_name="TensorFlow",
        aliases=[
            "tensorflow",
        ],
        category="Machine Learning",
    ),

    "pytorch": SkillConcept(
        skill_id="SKILL_005",
        canonical_name="PyTorch",
        aliases=[
            "pytorch",
            "torch",
        ],
        category="Machine Learning",
    ),

    "nlp": SkillConcept(
        skill_id="SKILL_006",
        canonical_name="Natural Language Processing",
        aliases=[
            "nlp",
            "natural language processing",
        ],
        category="Artificial Intelligence",
        child_skills=[
            "Transformer",
            "BERT",
            "GPT",
        ],
    ),

    "transformer": SkillConcept(
        skill_id="SKILL_007",
        canonical_name="Transformer",
        aliases=[
            "transformer",
            "transformers",
        ],
        category="Deep Learning",
        parent_skill="Natural Language Processing",
    ),

    "bert": SkillConcept(
        skill_id="SKILL_008",
        canonical_name="BERT",
        aliases=[
            "bert",
        ],
        category="NLP",
        parent_skill="Natural Language Processing",
    ),

    "gpt": SkillConcept(
        skill_id="SKILL_009",
        canonical_name="GPT",
        aliases=[
            "gpt",
            "generative pre-trained transformer",
            "generative pretrained transformer",
        ],
        category="NLP",
        parent_skill="Natural Language Processing",
    ),

    "hugging_face_transformers": SkillConcept(
        skill_id="SKILL_010",
        canonical_name="Hugging Face Transformers",
        aliases=[
            "hugging face transformers",
            "huggingface transformers",
            "transformers library",
        ],
        category="NLP / Deep Learning",
    ),

    "fastapi": SkillConcept(
        skill_id="SKILL_011",
        canonical_name="FastAPI",
        aliases=[
            "fastapi",
            "fast api",
        ],
        category="Web Development",
    ),

    "rag": SkillConcept(
        skill_id="SKILL_012",
        canonical_name="RAG",
        aliases=[
            "rag",
            "retrieval augmented generation",
            "retrieval-augmented generation",
        ],
        category="Generative AI",
        parent_skill="LLM",
    ),

    "vector_database": SkillConcept(
        skill_id="SKILL_013",
        canonical_name="Vector Database",
        aliases=[
            "vector database",
            "vector databases",
            "vector db",
            "vector dbs",
        ],
        category="Database",
        parent_skill="Embeddings",
    ),

    "neo4j": SkillConcept(
        skill_id="SKILL_014",
        canonical_name="Neo4j",
        aliases=[
            "neo4j",
        ],
        category="Graph Database",
    ),

    "cypher": SkillConcept(
        skill_id="SKILL_015",
        canonical_name="Cypher",
        aliases=[
            "cypher",
        ],
        category="Query Language",
    ),

    "microservices": SkillConcept(
        skill_id="SKILL_016",
        canonical_name="Microservices",
        aliases=[
            "microservices",
            "microservice architecture",
            "microservices architecture",
        ],
        category="Software Architecture",
    ),

    "ci_cd": SkillConcept(
        skill_id="SKILL_017",
        canonical_name="CI/CD",
        aliases=[
            "ci/cd",
            "ci cd",
            "continuous integration",
            "continuous delivery",
            "continuous deployment",
        ],
        category="DevOps",
    ),

    "devops": SkillConcept(
        skill_id="SKILL_018",
        canonical_name="DevOps",
        aliases=[
            "devops",
            "dev ops",
        ],
        category="DevOps",
    ),

    "machine_learning": SkillConcept(
        skill_id="SKILL_019",
        canonical_name="Machine Learning",
        aliases=[
            "machine learning",
            "ml",
            "machine learning algorithms",
        ],
        category="Machine Learning",
    ),

    "rest_api": SkillConcept(
        skill_id="SKILL_020",
        canonical_name="REST API",
        aliases=[
            "rest api",
            "rest apis",
            "restful api",
            "restful apis",
        ],
        category="Web Development",
    ),

    "llm": SkillConcept(
        skill_id="SKILL_021",
        canonical_name="LLM",
        aliases=[
            "llm",
            "llms",
            "large language model",
            "large language models",
            "llm api",
            "llm apis",
        ],
        category="Artificial Intelligence",
    ),

    # -----------------------------------------------------------------------
    # Agentic AI
    # -----------------------------------------------------------------------

    "ai_agents": SkillConcept(
        skill_id="SKILL_022",
        canonical_name="AI Agents",
        aliases=[
            "ai agent",
            "ai agents",
            "agentic ai",
            "agentic systems",
            "agentic system",
            "ai agent systems",
        ],
        category="Artificial Intelligence",
        parent_skill="LLM",
    ),

    "function_calling": SkillConcept(
        skill_id="SKILL_023",
        canonical_name="Function Calling",
        aliases=[
            "function calling",
            "function call",
            "function calling api",
        ],
        category="Generative AI",
        parent_skill="AI Agents",
    ),

    "tool_calling": SkillConcept(
        skill_id="SKILL_024",
        canonical_name="Tool Calling",
        aliases=[
            "tool calling",
            "tool call",
            "tool calls",
        ],
        category="Generative AI",
        parent_skill="AI Agents",
    ),

    "embeddings": SkillConcept(
        skill_id="SKILL_025",
        canonical_name="Embeddings",
        aliases=[
            "embedding",
            "embeddings",
            "text embeddings",
            "vector embeddings",
        ],
        category="Generative AI",
        parent_skill="LLM",
    ),

    "postgresql": SkillConcept(
        skill_id="SKILL_026",
        canonical_name="PostgreSQL",
        aliases=[
            "postgresql",
            "postgres",
            "postgres sql",
        ],
        category="Database",
    ),

    "linux": SkillConcept(
        skill_id="SKILL_027",
        canonical_name="Linux",
        aliases=[
            "linux",
            "linux operating system",
        ],
        category="Operating System",
    ),

    "langchain": SkillConcept(
        skill_id="SKILL_028",
        canonical_name="LangChain",
        aliases=[
            "langchain",
        ],
        category="AI Framework",
        parent_skill="AI Agents",
    ),

    "langgraph": SkillConcept(
        skill_id="SKILL_029",
        canonical_name="LangGraph",
        aliases=[
            "langgraph",
        ],
        category="AI Framework",
        parent_skill="AI Agents",
    ),

    "mcp": SkillConcept(
        skill_id="SKILL_030",
        canonical_name="MCP",
        aliases=[
            "mcp",
            "model context protocol",
        ],
        category="AI Infrastructure",
        parent_skill="AI Agents",
    ),

    "redis": SkillConcept(
        skill_id="SKILL_031",
        canonical_name="Redis",
        aliases=[
            "redis",
        ],
        category="Database",
    ),

    "n8n": SkillConcept(
        skill_id="SKILL_032",
        canonical_name="n8n",
        aliases=[
            "n8n",
            "n 8 n",
        ],
        category="Automation",
    ),

    "prompt_engineering": SkillConcept(
        skill_id="SKILL_033",
        canonical_name="Prompt Engineering",
        aliases=[
            "prompt engineering",
            "prompt design",
            "prompting",
        ],
        category="Generative AI",
        parent_skill="LLM",
    ),

    "context_engineering": SkillConcept(
        skill_id="SKILL_034",
        canonical_name="Context Engineering",
        aliases=[
            "context engineering",
            "context management",
            "context design",
        ],
        category="Generative AI",
        parent_skill="LLM",
    ),

    "context_generation": SkillConcept(
        skill_id="SKILL_035",
        canonical_name="Context Generation",
        aliases=[
            "context generation",
            "context generation for llm",
        ],
        category="Generative AI",
        parent_skill="LLM",
    ),

    "tool_integration": SkillConcept(
        skill_id="SKILL_036",
        canonical_name="Tool Integration",
        aliases=[
            "tool integration",
            "tools integration",
        ],
        category="Artificial Intelligence",
        parent_skill="AI Agents",
    ),

    "educational_data_analysis": SkillConcept(
        skill_id="SKILL_037",
        canonical_name="Educational Data Analysis",
        aliases=[
            "educational data analysis",
            "education data analysis",
        ],
        category="Data Analysis",
    ),

    "personalized_output_generation": SkillConcept(
        skill_id="SKILL_038",
        canonical_name="Personalized Output Generation",
        aliases=[
            "personalized output generation",
            "personalized outputs",
        ],
        category="Generative AI",
    ),

    # -----------------------------------------------------------------------
    # Agent internals
    # -----------------------------------------------------------------------

    "agent_memory": SkillConcept(
        skill_id="SKILL_039",
        canonical_name="Agent Memory",
        aliases=[
            "agent memory",
            "agent memories",
            "memory for agents",
            "agent memory management",
        ],
        category="Agentic AI",
        parent_skill="AI Agents",
    ),

    "state_management": SkillConcept(
        skill_id="SKILL_040",
        canonical_name="State Management",
        aliases=[
            "state management",
            "agent state management",
            "state management for agents",
        ],
        category="Agentic AI",
        parent_skill="AI Agents",
    ),

    "agent_orchestration": SkillConcept(
        skill_id="SKILL_041",
        canonical_name="Agent Orchestration",
        aliases=[
            "agent orchestration",
            "agent orchestration systems",
            "orchestration of agents",
            "agent workflow orchestration",
        ],
        category="Agentic AI",
        parent_skill="AI Agents",
    ),

    "openai_agents_sdk": SkillConcept(
        skill_id="SKILL_042",
        canonical_name="OpenAI Agents SDK",
        aliases=[
            "openai agents sdk",
            "openai agents",
        ],
        category="Agentic AI Framework",
        parent_skill="AI Agents",
    ),

    # -----------------------------------------------------------------------
    # AI models / ecosystem
    # -----------------------------------------------------------------------

    "llama_index": SkillConcept(
        skill_id="SKILL_043",
        canonical_name="LlamaIndex",
        aliases=[
            "llamaindex",
            "llama index",
        ],
        category="Generative AI Framework",
        parent_skill="LLM",
    ),

    "llama": SkillConcept(
        skill_id="SKILL_044",
        canonical_name="Llama",
        aliases=[
            "llama",
            "meta llama",
        ],
        category="Language Model",
        parent_skill="LLM",
    ),

    "qwen": SkillConcept(
        skill_id="SKILL_045",
        canonical_name="Qwen",
        aliases=[
            "qwen",
        ],
        category="Language Model",
        parent_skill="LLM",
    ),

    "mistral": SkillConcept(
        skill_id="SKILL_046",
        canonical_name="Mistral",
        aliases=[
            "mistral",
            "mistral ai",
        ],
        category="Language Model",
        parent_skill="LLM",
    ),

    "gpt_oss": SkillConcept(
        skill_id="SKILL_047",
        canonical_name="GPT-OSS",
        aliases=[
            "gpt-oss",
            "gpt oss",
            "gptoss",
        ],
        category="Language Model",
        parent_skill="LLM",
    ),

    "gemma": SkillConcept(
        skill_id="SKILL_048",
        canonical_name="Gemma",
        aliases=[
            "gemma",
            "google gemma",
        ],
        category="Language Model",
        parent_skill="LLM",
    ),

    "whisper": SkillConcept(
        skill_id="SKILL_049",
        canonical_name="Whisper",
        aliases=[
            "whisper",
            "openai whisper",
        ],
        category="Speech AI",
    ),

    # -----------------------------------------------------------------------
    # AI Infrastructure / Cloud
    # -----------------------------------------------------------------------

    "observability_tools": SkillConcept(
        skill_id="SKILL_050",
        canonical_name="Observability Tools",
        aliases=[
            "observability tools",
            "ai observability",
            "llm observability",
            "observability",
        ],
        category="AI Infrastructure",
    ),

    "cloud_infrastructure": SkillConcept(
        skill_id="SKILL_051",
        canonical_name="Cloud Infrastructure",
        aliases=[
            "cloud infrastructure",
            "cloud infrastructure management",
            "cloud systems",
        ],
        category="Infrastructure",
    ),

    "aws": SkillConcept(
        skill_id="SKILL_052",
        canonical_name="AWS",
        aliases=[
            "aws",
            "amazon web services",
        ],
        category="Cloud Platform",
        parent_skill="Cloud Infrastructure",
    ),

    "kubernetes": SkillConcept(
        skill_id="SKILL_053",
        canonical_name="Kubernetes",
        aliases=[
            "kubernetes",
            "k8s",
        ],
        category="Infrastructure",
    ),

    # -----------------------------------------------------------------------
    # Database / Web additions used by the current tests
    # -----------------------------------------------------------------------

    "sql": SkillConcept(
        skill_id="SKILL_054",
        canonical_name="SQL",
        aliases=[
            "sql",
        ],
        category="Database Language",
    ),

    "django": SkillConcept(
        skill_id="SKILL_055",
        canonical_name="Django",
        aliases=[
            "django",
        ],
        category="Web Framework",
    ),

    # -----------------------------------------------------------------------
    # Generic framework concept
    # -----------------------------------------------------------------------

    "ai_framework": SkillConcept(
        skill_id="SKILL_056",
        canonical_name="AI Framework",
        aliases=[
            "ai framework",
            "ai frameworks",
        ],
        category="AI Infrastructure",
    ),
}


# ---------------------------------------------------------------------------
# Normalization helper
# ---------------------------------------------------------------------------

def normalize_skill_text(text: str) -> str:
    """
    Normalize a skill phrase before exact ontology matching.

    This function is intentionally conservative. It handles:
    - empty values
    - whitespace
    - case differences
    - common proficiency / experience prefixes
    """

    if not text:
        return ""

    normalized_text = text.strip().lower()

    prefixes = [
        "high proficiency in",
        "advanced proficiency in",
        "professional proficiency in",
        "proficient in",
        "strong proficiency in",
        "experience in",
        "experience with",
        "experience working with",
        "practical experience in",
        "hands-on experience with",
        "hands-on experience in",
        "familiarity with",
        "knowledge of",
        "understanding of",
        "working knowledge of",
        "expertise in",
        "expert in",
        "skilled in",
        "proficiency in",
        "تسلط حرفه‌ای به",
        "تسلط حرفه ای به",
        "تسلط به",
    ]

    # Remove a leading natural-language prefix once.
    changed = True

    while changed:

        changed = False

        for prefix in prefixes:

            if normalized_text.startswith(prefix):

                normalized_text = (
                    normalized_text[len(prefix):]
                    .strip(" :,-")
                )

                changed = True
                break

    normalized_text = re.sub(
        r"\s+",
        " ",
        normalized_text,
    )

    return normalized_text


# ---------------------------------------------------------------------------
# Lookup helpers
# ---------------------------------------------------------------------------

def get_skill_concept(
    skill_name: str
) -> Optional[SkillConcept]:
    """
    Return the ontology concept matching a canonical name or alias.

    Matching is case-insensitive and whitespace-normalized.

    Exact canonical/alias matching is attempted first. If the input is a
    larger phrase, a longest-phrase match is attempted afterward.
    """

    normalized_name = normalize_skill_text(
        skill_name
    )

    if not normalized_name:
        return None

    # 1. Canonical-name exact match
    for concept in SKILL_ONTOLOGY.values():

        if (
            normalize_skill_text(
                concept.canonical_name
            )
            == normalized_name
        ):
            return concept

    # 2. Alias exact match
    for concept in SKILL_ONTOLOGY.values():

        for alias in concept.aliases:

            if (
                normalize_skill_text(alias)
                == normalized_name
            ):
                return concept

    # 3. Phrase matching.
    # Longest phrase first prevents a shorter phrase from winning when a
    # more specific concept exists.
    candidates = []

    for concept in SKILL_ONTOLOGY.values():

        candidates.append(
            (
                normalize_skill_text(
                    concept.canonical_name
                ),
                concept,
            )
        )

        for alias in concept.aliases:

            candidates.append(
                (
                    normalize_skill_text(alias),
                    concept,
                )
            )

    candidates.sort(
        key=lambda item: len(item[0]),
        reverse=True,
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
            normalized_name,
        ):
            return concept

    return None


def get_canonical_name(
    skill_name: str
) -> Optional[str]:
    """
    Return the canonical ontology name.

    Returns None when no ontology concept matches.
    """

    concept = get_skill_concept(
        skill_name
    )

    if concept is None:
        return None

    return concept.canonical_name


def get_parent_skill(
    skill_name: str
) -> Optional[str]:
    """
    Return the canonical parent skill, if one exists.
    """

    concept = get_skill_concept(
        skill_name
    )

    if concept is None:
        return None

    return concept.parent_skill


def get_child_skills(
    skill_name: str
) -> List[str]:
    """
    Return the child skills of a concept.
    """

    concept = get_skill_concept(
        skill_name
    )

    if concept is None:
        return []

    return list(
        concept.child_skills
    )


def get_related_skills(
    skill_name: str
) -> List[str]:
    """
    Return related skills of a concept.
    """

    concept = get_skill_concept(
        skill_name
    )

    if concept is None:
        return []

    return list(
        concept.related_skills
    )


def get_skill_category(
    skill_name: str
) -> Optional[str]:
    """
    Return the ontology category for a skill.
    """

    concept = get_skill_concept(
        skill_name
    )

    if concept is None:
        return None

    return concept.category


def get_all_canonical_skills() -> List[str]:
    """
    Return all canonical skill names in ontology order.
    """

    return [
        concept.canonical_name
        for concept in SKILL_ONTOLOGY.values()
    ]


# ---------------------------------------------------------------------------
# Standalone test
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    print("=" * 72)
    print("SKILL ONTOLOGY TEST")
    print("=" * 72)

    examples = [
        "python",
        "Python programming",
        "REST APIs",
        "Vector Databases",
        "Experience with Django",
        "agentic systems",
        "Function Calling",
        "Tool Calling",
        "Agent Memory",
        "State Management",
        "Agent Orchestration",
        "OpenAI Agents SDK",
        "LangGraph",
        "Model Context Protocol",
        "GptOss",
        "Qwen",
        "LlamaIndex",
        "Whisper",
        "AWS",
        "unknown skill",
    ]

    for example in examples:

        concept = get_skill_concept(
            example
        )

        print(f"\nInput: {example}")

        if concept is None:
            print("  Canonical: NOT FOUND")
            continue

        print(
            f"  ID: {concept.skill_id}"
        )
        print(
            f"  Canonical: {concept.canonical_name}"
        )
        print(
            f"  Category: {concept.category}"
        )
        print(
            f"  Parent: {concept.parent_skill}"
        )

    # Structural validation
    skill_ids = [
        concept.skill_id
        for concept in SKILL_ONTOLOGY.values()
    ]

    assert len(skill_ids) == len(
        set(skill_ids)
    ), "Duplicate skill_id detected."

    assert len(SKILL_ONTOLOGY) == 56

    print("\n" + "=" * 72)
    print(
        f"Total ontology concepts: "
        f"{len(SKILL_ONTOLOGY)}"
    )
    print("Unique skill IDs: OK")
    print("Ontology structure: OK")
    print("=" * 72)
