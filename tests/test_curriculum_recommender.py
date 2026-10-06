from src.skills.curriculum_recommender import (
    CurriculumRecommender
)


def build_recommendation_map():
    return {
        "AI Agents": {
            "curriculum_area": "Agentic AI Development",
            "recommended_topics": [
                "AI Agents",
                "Agent Orchestration"
            ],
            "reason": "High market gap."
        },
        "RAG": {
            "curriculum_area": "Retrieval-Augmented Generation",
            "recommended_topics": [
                "RAG",
                "Embeddings"
            ],
            "reason": "High market gap."
        },
        "Embeddings": {
            "curriculum_area": "RAG and Vector Search",
            "recommended_topics": [
                "Embeddings",
                "Vector Search"
            ],
            "reason": "Medium market gap."
        }
    }


def test_high_gap_creates_curriculum_recommendation():

    gap_report = {
        "high_gap": [
            {
                "skill": "AI Agents",
                "coverage": 66.67,
                "job_count": 2,
                "total_jobs": 3,
                "skill_type": "SKILL"
            }
        ],
        "medium_gap": []
    }

    recommender = CurriculumRecommender(
        build_recommendation_map()
    )

    result = recommender.recommend(
        gap_report
    )

    assert len(
        result["recommendations"]
    ) == 1

    recommendation = result["recommendations"][0]

    assert recommendation["skill"] == "AI Agents"

    assert (
        recommendation["gap_level"]
        == "HIGH"
    )

    assert (
        recommendation["curriculum_area"]
        == "Agentic AI Development"
    )


def test_medium_gap_is_supported():

    gap_report = {
        "high_gap": [],
        "medium_gap": [
            {
                "skill": "Embeddings",
                "coverage": 33.33,
                "job_count": 1,
                "total_jobs": 3,
                "skill_type": "SKILL"
            }
        ]
    }

    recommender = CurriculumRecommender(
        build_recommendation_map()
    )

    result = recommender.recommend(
        gap_report
    )

    assert len(
        result["recommendations"]
    ) == 1

    assert (
        result["recommendations"][0][
            "gap_level"
        ]
        == "MEDIUM"
    )


def test_framework_is_not_recommended_as_gap():

    gap_report = {
        "high_gap": [
            {
                "skill": "LangGraph",
                "coverage": 66.67,
                "job_count": 2,
                "total_jobs": 3,
                "skill_type": "FRAMEWORK"
            }
        ],
        "medium_gap": []
    }

    recommender = CurriculumRecommender(
        build_recommendation_map()
    )

    result = recommender.recommend(
        gap_report
    )

    assert result["recommendations"] == []


def test_unmapped_gap_is_reported():

    gap_report = {
        "high_gap": [
            {
                "skill": "Some New Skill",
                "coverage": 66.67,
                "job_count": 2,
                "total_jobs": 3,
                "skill_type": "SKILL"
            }
        ],
        "medium_gap": []
    }

    recommender = CurriculumRecommender(
        build_recommendation_map()
    )

    result = recommender.recommend(
        gap_report
    )

    assert result["recommendations"] == []

    assert len(
        result["unmapped_gaps"]
    ) == 1

    assert (
        result["unmapped_gaps"][0]["skill"]
        == "Some New Skill"
    )
