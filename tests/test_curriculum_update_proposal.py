from src.skills.curriculum_update_proposal import (
    CurriculumUpdateProposer,
)


def test_gap_creates_add_core_skills_proposal():
    report = {
        "areas": [{
            "sequence": 1,
            "phase": 1,
            "curriculum_area": "LLM Fundamentals and Application Engineering",
            "priority": "HIGH",
            "status": "GAP",
            "missing_core_skills": ["LLM", "Context Engineering"],
            "missing_prerequisite_skills": [],
            "prerequisite_curriculum_areas": [],
        }],
        "unmapped_curriculum_skills": [],
    }

    result = CurriculumUpdateProposer().propose(report)
    assert len(result["proposals"]) == 1
    proposal = result["proposals"][0]
    assert proposal["action"] == "ADD_CORE_SKILLS"
    assert proposal["core_skills_to_add"] == ["LLM", "Context Engineering"]
    assert proposal["prerequisite_skills_to_add"] == []


def test_partial_area_creates_extend_proposal():
    report = {
        "areas": [{
            "sequence": 1,
            "phase": 1,
            "curriculum_area": "Example Area",
            "priority": "HIGH",
            "status": "PARTIAL",
            "missing_core_skills": ["FastAPI"],
            "missing_prerequisite_skills": [],
            "prerequisite_curriculum_areas": [],
        }],
        "unmapped_curriculum_skills": [],
    }

    result = CurriculumUpdateProposer().propose(report)
    proposal = result["proposals"][0]
    assert proposal["action"] == "EXTEND_CORE_SKILLS"
    assert proposal["core_skills_to_add"] == ["FastAPI"]


def test_missing_prerequisite_is_proposed():
    report = {
        "areas": [{
            "sequence": 1,
            "phase": 1,
            "curriculum_area": "Example Area",
            "priority": "MEDIUM",
            "status": "COVERED",
            "missing_core_skills": [],
            "missing_prerequisite_skills": ["REST API"],
            "prerequisite_curriculum_areas": [],
        }],
        "unmapped_curriculum_skills": [],
    }

    result = CurriculumUpdateProposer().propose(report)
    proposal = result["proposals"][0]
    assert proposal["action"] == "ADD_PREREQUISITE_SKILLS"
    assert proposal["core_skills_to_add"] == []
    assert proposal["prerequisite_skills_to_add"] == ["REST API"]


def test_fully_covered_area_creates_no_proposal():
    report = {
        "areas": [{
            "sequence": 1,
            "phase": 1,
            "curriculum_area": "Python Foundations",
            "priority": "MEDIUM",
            "status": "COVERED",
            "missing_core_skills": [],
            "missing_prerequisite_skills": [],
            "prerequisite_curriculum_areas": [],
        }],
        "unmapped_curriculum_skills": [],
    }

    result = CurriculumUpdateProposer().propose(report)
    assert result["proposals"] == []


def test_unmapped_curriculum_skill_is_reviewed():
    report = {
        "areas": [],
        "unmapped_curriculum_skills": ["Git"],
    }

    result = CurriculumUpdateProposer().propose(report)
    items = result["unmapped_curriculum_skills"]
    assert len(items) == 1
    assert items[0]["skill"] == "Git"
    assert items[0]["action"] == "REVIEW_UNMAPPED_SKILL"


def test_core_and_prerequisite_skills_are_combined():
    report = {
        "areas": [{
            "sequence": 1,
            "phase": 1,
            "curriculum_area": "Example Area",
            "priority": "HIGH",
            "status": "GAP",
            "missing_core_skills": ["FastAPI"],
            "missing_prerequisite_skills": ["REST API"],
            "prerequisite_curriculum_areas": [],
        }],
        "unmapped_curriculum_skills": [],
    }

    result = CurriculumUpdateProposer().propose(report)
    proposal = result["proposals"][0]
    assert proposal["action"] == "ADD_CORE_AND_PREREQUISITE_SKILLS"
    assert proposal["core_skills_to_add"] == ["FastAPI"]
    assert proposal["prerequisite_skills_to_add"] == ["REST API"]
