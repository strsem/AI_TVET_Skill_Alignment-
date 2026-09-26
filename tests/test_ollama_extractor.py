import pytest

from src.llm.ollama_extractor import OllamaSkillExtractor
from src.llm.schemas import SkillExtractionResult


@pytest.mark.integration
def test_ollama_skill_extraction():

    job_description = """
    We are looking for a Python developer.

    Required:
    Python
    Git
    Docker

    Preferred:
    FastAPI
    RAG
    """

    extractor = OllamaSkillExtractor(
        model="qwen3:4b"
    )

    result = extractor.extract(
        job_description
    )

    assert isinstance(
        result,
        SkillExtractionResult
    )

    assert len(result.skills) > 0