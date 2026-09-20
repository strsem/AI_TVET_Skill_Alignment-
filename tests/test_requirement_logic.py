from src.skills.requirement_parser import (
    create_requirement,
    requirement_to_text
)


def test_or_requirement():

    requirement = create_requirement(
        skills=[
            "TensorFlow",
            "PyTorch"
        ],
        logic="OR",
        importance="Required"
    )

    assert requirement.logic == "OR"
    assert requirement.skills == [
        "TensorFlow",
        "PyTorch"
    ]


def test_and_requirement():

    requirement = create_requirement(
        skills=[
            "Python",
            "FastAPI"
        ],
        logic="AND",
        importance="Required"
    )

    assert requirement.logic == "AND"


def test_requirement_text():

    requirement = create_requirement(
        skills=[
            "TensorFlow",
            "PyTorch"
        ],
        logic="OR",
        importance="Required"
    )

    text = requirement_to_text(requirement)

    assert text == (
        "TensorFlow OR PyTorch (Required)"
    )