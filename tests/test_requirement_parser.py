import pytest

from src.skills.requirement_parser import (
    parse_requirement,
    parse_requirement_text
)


def test_parse_or_requirement():

    requirement = parse_requirement_text(
        requirement_id="REQ_001",
        text="TensorFlow or PyTorch",
        category="Deep Learning Framework"
    )

    assert requirement.logic == "OR"

    assert requirement.skills == [
        "TensorFlow",
        "PyTorch"
    ]


def test_parse_and_requirement():

    requirement = parse_requirement_text(
        requirement_id="REQ_002",
        text="Web Service and FastAPI",
        category="Backend Development"
    )

    assert requirement.logic == "AND"

    assert requirement.skills == [
        "Web Service",
        "FastAPI"
    ]


def test_parse_single_skill():

    requirement = parse_requirement_text(
        requirement_id="REQ_003",
        text="Python"
    )

    assert requirement.logic == "AND"

    assert requirement.skills == [
        "Python"
    ]


def test_parse_case_insensitive_or():

    requirement = parse_requirement_text(
        requirement_id="REQ_004",
        text="TensorFlow OR PyTorch"
    )

    assert requirement.logic == "OR"

    assert requirement.skills == [
        "TensorFlow",
        "PyTorch"
    ]


def test_parse_mixed_and_or_raises():

    with pytest.raises(ValueError):
        parse_requirement_text(
            requirement_id="REQ_005",
            text="Python or Git and Docker"
        )


def test_parse_requirement_from_list_unchanged():

    requirement = parse_requirement(
        requirement_id="REQ_006",
        skills=["Python", "Git"],
        logic="AND"
    )

    assert requirement.logic == "AND"

    assert requirement.skills == [
        "Python",
        "Git"
    ]