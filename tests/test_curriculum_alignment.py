from src.skills.curriculum_alignment import (
    CurriculumAligner
)


def build_aligner():

    return CurriculumAligner(
        {
            "python": "Python",
            "python programming": "Python",
            "rest api": "REST API",
            "restful api": "REST API",
            "git": "Git"
        }
    )


def test_aliases_are_canonicalized():

    aligner = build_aligner()

    assert (
        aligner.canonicalize(
            "Python Programming"
        )
        == "Python"
    )

    assert (
        aligner.canonicalize(
            "RESTful API"
        )
        == "REST API"
    )


def test_current_curriculum_covers_prerequisite_skills():

    roadmap = {
        "roadmap": [
            {
                "sequence": 1,
                "phase": 1,
                "curriculum_area":
                    "AI Backend and API Development",
                "priority": "MEDIUM",
                "skills": ["FastAPI"],
                "prerequisite_skills": [
                    "Python",
                    "REST API"
                ],
                "prerequisite_curriculum_areas": [],
                "related_areas": []
            }
        ]
    }

    curriculum = [
        "Python",
        "Git",
        "REST API"
    ]

    result = build_aligner().align(
        roadmap,
        curriculum
    )

    area = result["areas"][0]

    assert area["status"] == "GAP"

    assert area[
        "covered_prerequisite_skills"
    ] == [
        "Python",
        "REST API"
    ]

    assert area[
        "missing_core_skills"
    ] == [
        "FastAPI"
    ]


def test_partial_area_is_detected():

    roadmap = {
        "roadmap": [
            {
                "sequence": 1,
                "phase": 1,
                "curriculum_area":
                    "Example Area",
                "priority": "HIGH",
                "skills": [
                    "Python",
                    "FastAPI"
                ],
                "prerequisite_skills": [],
                "prerequisite_curriculum_areas": [],
                "related_areas": []
            }
        ]
    }

    curriculum = [
        "Python",
        "Git",
        "REST API"
    ]

    result = build_aligner().align(
        roadmap,
        curriculum
    )

    area = result["areas"][0]

    assert area["status"] == "PARTIAL"

    assert area[
        "covered_core_skills"
    ] == ["Python"]

    assert area[
        "missing_core_skills"
    ] == ["FastAPI"]


def test_unmapped_curriculum_skill_is_reported():

    roadmap = {
        "roadmap": [
            {
                "sequence": 1,
                "phase": 1,
                "curriculum_area":
                    "Example Area",
                "priority": "HIGH",
                "skills": ["Python"],
                "prerequisite_skills": [],
                "prerequisite_curriculum_areas": [],
                "related_areas": []
            }
        ]
    }

    curriculum = [
        "Python",
        "Git"
    ]

    result = build_aligner().align(
        roadmap,
        curriculum
    )

    assert (
        result[
            "unmapped_curriculum_skills"
        ]
        == ["Git"]
    )


def test_covered_area_is_detected():

    roadmap = {
        "roadmap": [
            {
                "sequence": 1,
                "phase": 1,
                "curriculum_area":
                    "Python Foundations",
                "priority": "MEDIUM",
                "skills": ["Python"],
                "prerequisite_skills": [],
                "prerequisite_curriculum_areas": [],
                "related_areas": []
            }
        ]
    }

    curriculum = ["Python"]

    result = build_aligner().align(
        roadmap,
        curriculum
    )

    assert (
        result["areas"][0]["status"]
        == "COVERED"
    )