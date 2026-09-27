from src.skills.skill_segmenter import (
    segment_skill
)


def test_multiple_skills():

    result = segment_skill(
        "Familiarity with REST API, PostgreSQL, Git, Docker, and Linux"
    )

    assert "REST API" in result
    assert "PostgreSQL" in result
    assert "Git" in result
    assert "Docker" in result
    assert "Linux" in result


def test_rag_skills():

    result = segment_skill(
        "Experience working with RAG, Embeddings, and Vector Databases"
    )

    assert "RAG" in result
    assert "Embeddings" in result
    assert "Vector Database" in result


def test_agent_skill():

    result = segment_skill(
        "Experience in designing and developing AI Agents and Agentic Systems"
    )

    assert "AI Agents" in result