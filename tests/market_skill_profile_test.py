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


from src.llm.schemas import (
    ExtractedSkill,
    SkillExtractionResult
)

from src.skills.market_skill_profile import (
    calculate_market_skill_profile,
    calculate_market_skill_profile_from_extractions
)


def test_market_profile_from_llm_extractions():

    job_1 = SkillExtractionResult(
        skills=[
            ExtractedSkill(
                skill="Python",
                category="Programming",
                importance="Required",
                proficiency="Advanced",
                evidence="Python"
            ),
            ExtractedSkill(
                skill="Git",
                category="Version Control",
                importance="Required",
                proficiency="Intermediate",
                evidence="Git"
            )
        ]
    )

    job_2 = SkillExtractionResult(
        skills=[
            ExtractedSkill(
                skill="Python Programming",
                category="Programming",
                importance="Required",
                proficiency="Advanced",
                evidence="Python Programming"
            ),
            ExtractedSkill(
                skill="PyTorch",
                category="Machine Learning",
                importance="Preferred",
                proficiency="Intermediate",
                evidence="PyTorch"
            )
        ]
    )

    profile = calculate_market_skill_profile_from_extractions(
        [job_1, job_2]
    )

    assert profile["Python"]["job_count"] == 2
    assert profile["Python"]["market_coverage"] == 100.0

    assert profile["Git"]["job_count"] == 1
    assert profile["PyTorch"]["job_count"] == 1