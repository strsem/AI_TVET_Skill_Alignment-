import pytest

from src.skills.curriculum_roadmap import (
    CurriculumRoadmapBuilder
)


def test_overlapping_areas_are_consolidated():

    recommendation_report = {
        "curriculum_areas": [
            {
                "curriculum_area":
                    "Retrieval-Augmented Generation",
                "priority": "HIGH",
                "skills": ["RAG"],
                "recommended_topics": ["RAG"],
                "reasons": ["High market gap."]
            },
            {
                "curriculum_area":
                    "RAG and Vector Search",
                "priority": "MEDIUM",
                "skills": ["Embeddings"],
                "recommended_topics": [
                    "Embeddings"
                ],
                "reasons": [
                    "Medium market gap."
                ]
            }
        ]
    }

    builder = CurriculumRoadmapBuilder()

    result = builder.build(
        recommendation_report
    )

    assert (
        result["summary"]["original_areas"]
        == 2
    )

    assert (
        result["summary"]["consolidated_areas"]
        == 1
    )

    area = result["roadmap"][0]

    assert (
        area["curriculum_area"]
        == "RAG and Vector Search"
    )

    assert area["priority"] == "HIGH"

    assert "RAG" in area["skills"]
    assert "Embeddings" in area["skills"]


def test_agentic_ai_does_not_require_rag():

    recommendation_report = {
        "curriculum_areas": [
            {
                "curriculum_area":
                    "LLM Fundamentals and Application Engineering",
                "priority": "HIGH",
                "skills": ["LLM"],
                "recommended_topics": ["LLM"],
                "reasons": []
            },
            {
                "curriculum_area":
                    "RAG and Vector Search",
                "priority": "HIGH",
                "skills": ["RAG"],
                "recommended_topics": ["RAG"],
                "reasons": []
            },
            {
                "curriculum_area":
                    "Agentic AI Development",
                "priority": "HIGH",
                "skills": ["AI Agents"],
                "recommended_topics": [
                    "AI Agents"
                ],
                "reasons": []
            }
        ]
    }

    builder = CurriculumRoadmapBuilder()

    result = builder.build(
        recommendation_report
    )

    agentic = next(
        area
        for area in result["roadmap"]
        if area["curriculum_area"]
        == "Agentic AI Development"
    )

    assert (
        agentic[
            "prerequisite_curriculum_areas"
        ]
        == [
            "LLM Fundamentals and Application Engineering"
        ]
    )

    assert (
        "RAG and Vector Search"
        not in agentic[
            "prerequisite_curriculum_areas"
        ]
    )

    assert (
        "RAG and Vector Search"
        in agentic["related_areas"]
    )


def test_skill_cannot_be_own_prerequisite():

    recommendation_report = {
        "curriculum_areas": [
            {
                "curriculum_area":
                    "Test Area",
                "priority": "HIGH",
                "skills": ["Python"],
                "recommended_topics": [],
                "reasons": []
            }
        ]
    }

    builder = CurriculumRoadmapBuilder(
        area_prerequisite_skills={
            "Test Area": ["Python"]
        }
    )

    with pytest.raises(ValueError):
        builder.build(
            recommendation_report
        )


def test_linux_and_docker_are_not_self_prerequisites():

    recommendation_report = {
        "curriculum_areas": [
            {
                "curriculum_area":
                    "AI Infrastructure, Deployment and Cloud",
                "priority": "MEDIUM",
                "skills": [
                    "Cloud Infrastructure",
                    "Docker",
                    "Linux"
                ],
                "recommended_topic  s": [],
                "reasons": []
            }
        ]
    }

    builder = CurriculumRoadmapBuilder()

    result = builder.build(
        recommendation_report
    )

    area = result["roadmap"][0]

    assert (
        area["prerequisite_skills"]
        == ["Git"]
    )


def test_topological_order_is_respected():

    recommendation_report = {
        "curriculum_areas": [
            {
                "curriculum_area":
                    "Agentic AI Development",
                "priority": "HIGH",
                "skills": ["AI Agents"],
                "recommended_topics": [],
                "reasons": []
            },
            {
                "curriculum_area":
                    "LLM Fundamentals and Application Engineering",
                "priority": "HIGH",
                "skills": ["LLM"],
                "recommended_topics": [],
                "reasons": []
            }
        ]
    }

    builder = CurriculumRoadmapBuilder()

    result = builder.build(
        recommendation_report
    )

    names = [
        area["curriculum_area"]
        for area in result["roadmap"]
    ]

    assert names.index(
        "LLM Fundamentals and Application Engineering"
    ) < names.index(
        "Agentic AI Development"
    )


def test_dependency_cycle_is_rejected():

    recommendation_report = {
        "curriculum_areas": [
            {
                "curriculum_area": "Area A",
                "priority": "HIGH",
                "skills": ["Skill A"],
                "recommended_topics": [],
                "reasons": []
            },
            {
                "curriculum_area": "Area B",
                "priority": "HIGH",
                "skills": ["Skill B"],
                "recommended_topics": [],
                "reasons": []
            }
        ]
    }

    builder = CurriculumRoadmapBuilder(
        area_prerequisite_areas={
            "Area A": ["Area B"],
            "Area B": ["Area A"]
        }
    )

    with pytest.raises(ValueError):
        builder.build(
            recommendation_report
        )
