from src.skills.requirement_logic import (
    RequirementGroup,
    create_and_requirement,
    create_or_requirement,
    create_requirement,
    requirement_to_text
)


def test_or_requirement():

    requirement = create_or_requirement(
        requirement_id="REQ_001",
        skills=["TensorFlow", "PyTorch"],
        category="Deep Learning Framework"
    )

    assert isinstance(requirement, RequirementGroup)

    assert requirement.requirement_id == "REQ_001"

    assert requirement.logic == "OR"

    assert requirement.skills == [
        "TensorFlow",
        "PyTorch"
    ]

    assert requirement.category == "Deep Learning Framework"

    assert requirement.description == (
        "At least one of: TensorFlow, PyTorch"
    )


def test_and_requirement():

    requirement = create_and_requirement(
        requirement_id="REQ_002",
        skills=["Web Service", "FastAPI"],
        category="Backend Development"
    )

    assert isinstance(requirement, RequirementGroup)

    assert requirement.logic == "AND"

    assert requirement.skills == [
        "Web Service",
        "FastAPI"
    ]

    assert requirement.description == (
        "All of: Web Service, FastAPI"
    )


def test_requirement_to_text():

    requirement = create_or_requirement(
        requirement_id="REQ_003",
        skills=["TensorFlow", "PyTorch"]
    )

    text = requirement_to_text(requirement)

    assert text == "TensorFlow OR PyTorch"


def test_create_requirement_and():

    requirement = create_requirement(
        requirement_id="REQ_004",
        skills=["Python", "Git"],
        logic="AND"
    )

    assert requirement.logic == "AND"

    assert requirement.skills == [
        "Python",
        "Git"
    ]


def test_create_requirement_or():

    requirement = create_requirement(
        requirement_id="REQ_005",
        skills=["TensorFlow", "PyTorch"],
        logic="OR"
    )

    assert requirement.logic == "OR"


def test_invalid_logic():

    try:
        create_requirement(
            requirement_id="REQ_006",
            skills=["Python"],
            logic="XOR"
        )

        assert False

    except ValueError:
        assert True


def test_empty_skills():

    try:
        create_and_requirement(
            requirement_id="REQ_007",
            skills=[]
        )

        assert False

    except ValueError:
        assert True