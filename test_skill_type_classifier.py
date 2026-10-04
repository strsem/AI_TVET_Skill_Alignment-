from src.skills.skill_type_classifier import classify_skill_type


def test_skill_type_classification():
    assert classify_skill_type("RAG") == "SKILL"
    assert classify_skill_type("AI Agents") == "SKILL"
    assert classify_skill_type("Linux") == "SKILL"

    assert classify_skill_type("Git") == "TOOL"
    assert classify_skill_type("Docker") == "TOOL"
    assert classify_skill_type("PostgreSQL") == "TOOL"
    assert classify_skill_type("REST API") == "TOOL"

    assert classify_skill_type("LangChain") == "FRAMEWORK"
    assert classify_skill_type("LangGraph") == "FRAMEWORK"

    assert classify_skill_type("Qwen") == "MODEL"
    assert classify_skill_type("Mistral") == "MODEL"
    assert classify_skill_type("Whisper") == "MODEL"


def test_unknown_skill_defaults_to_skill():
    assert classify_skill_type("Kubernetes") == "SKILL"