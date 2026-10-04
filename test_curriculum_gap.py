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
        "RAG"
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

    # -----------------------------------------
    # NOT DIRECT GAP
    # -----------------------------------------

    not_direct_gap_skills = {
        item["skill"]
        for item in report["not_direct_gap"]
    }

    assert not_direct_gap_skills == {
        "LangGraph"
    }


def test_framework_is_not_direct_gap():

    report = analyze_curriculum_gap(
        market_profile,
        curriculum
    )

    langgraph = next(
        item
        for item in report["not_direct_gap"]
        if item["skill"] == "LangGraph"
    )

    assert langgraph["skill_type"] == "FRAMEWORK"
    assert langgraph["gap_level"] == "NOT DIRECT GAP"
    assert langgraph["curriculum_covered"] is False


def test_summary_counts():

    report = analyze_curriculum_gap(
        market_profile,
        curriculum
    )

    assert report["summary"]["total_market_skills"] == 7
    assert report["summary"]["total_curriculum_skills"] == 3

    assert report["summary"]["high_gap_count"] == 2
    assert report["summary"]["medium_gap_count"] == 1
    assert report["summary"]["covered_count"] == 3
    assert report["summary"]["not_direct_gap_count"] == 1

    assert report["unknown_curriculum_skills"] == []