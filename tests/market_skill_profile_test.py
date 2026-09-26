from src.skills.market_skill_profile import (
    calculate_market_skill_profile
)

def test_market_skill_profile():
    jobs = [
        ["Python", "Git", "Docker"],
        ["Python", "PyTorch"],
        ["Python", "FastAPI"]
    ]

    profile = calculate_market_skill_profile(
        jobs
    )

    assert profile["Python"]["job_count"] == 3
    assert profile["Python"]["market_coverage"] == 100.0
    assert profile["Git"]["job_count"] == 1
    assert profile["PyTorch"]["job_count"] == 1