from src.skills.curriculum_gap import (
    analyze_curriculum_gap
)


market_profile = {

    "AI Agents": {
        "job_count": 2,
        "total_jobs": 3,
        "market_coverage": 66.67
    },

    "RAG": {
        "job_count": 2,
        "total_jobs": 3,
        "market_coverage": 66.67
    },

    "LangGraph": {
        "job_count": 2,
        "total_jobs": 3,
        "market_coverage": 66.67
    },

    "MCP": {
        "job_count": 1,
        "total_jobs": 3,
        "market_coverage": 33.33
    },

    "Python": {
        "job_count": 2,
        "total_jobs": 3,
        "market_coverage": 66.67
    },

    "Git": {
        "job_count": 1,
        "total_jobs": 3,
        "market_coverage": 33.33
    },

    "REST API": {
        "job_count": 1,
        "total_jobs": 3,
        "market_coverage": 33.33
    }
}


curriculum = [
    "Python",
    "Git",
    "REST API"
]


def test_curriculum_gap_analysis():

    report = analyze_curriculum_gap(
        market_profile,
        curriculum
    )

    # -----------------------------------------
    # HIGH GAP
    # -----------------------------------------

    high_gap_skills = {
        item["skill"]
        for item in report["high_gap"]
    }

    assert high_gap_skills == {
        "AI Agents",
        "RAG",
        "LangGraph"
    }

    # -----------------------------------------
    # MEDIUM GAP
    # -----------------------------------------

    medium_gap_skills = {
        item["skill"]
        for item in report["medium_gap"]
    }

    assert medium_gap_skills == {
        "MCP"
    }

    # -----------------------------------------
    # COVERED
    # -----------------------------------------

    covered_skills = {
        item["skill"]
        for item in report["covered"]
    }

    assert covered_skills == {
        "Python",
        "Git",
        "REST API"
    }