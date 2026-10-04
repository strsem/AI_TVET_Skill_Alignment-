from typing import Dict


# Skills that are commonly considered direct educational competencies.
SKILL_TYPES: Dict[str, str] = {
    # Core / technical skills
    "Python": "SKILL",
    "Prompt Engineering": "SKILL",
    "LLM": "SKILL",
    "RAG": "SKILL",
    "Vector Database": "SKILL",
    "AI Agents": "SKILL",
    "State Management": "SKILL",
    "Linux": "SKILL",
    "Embeddings": "SKILL",
    "Agent Memory": "SKILL",
    "Agent Orchestration": "SKILL",
    "Tool Calling": "SKILL",
    "Function Calling": "SKILL",
    "Context Engineering": "SKILL",

    # Tools / technologies
    "Git": "TOOL",
    "Docker": "TOOL",
    "PostgreSQL": "TOOL",
    "REST API": "TOOL",

    # Frameworks
    "LangChain": "FRAMEWORK",
    "LangGraph": "FRAMEWORK",
    "LlamaIndex": "FRAMEWORK",

    # Models
    "GPT-OSS": "MODEL",
    "Mistral": "MODEL",
    "Qwen": "MODEL",
    "Gemma": "MODEL",
    "Llama": "MODEL",
    "Whisper": "MODEL",
}


def classify_skill_type(skill: str) -> str:
    """
    Return the type of a skill.

    Known skills are classified using SKILL_TYPES.
    Unknown skills default to SKILL for now.
    """
    return SKILL_TYPES.get(skill, "SKILL")