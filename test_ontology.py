from src.skills.skill_ontology import (
    get_skill_concept,
    get_canonical_name,
    get_parent_skill,
    get_child_skills,
    get_skill_category
)


def test_python_canonical_name():

    assert get_canonical_name("python") == "Python"


def test_python_alias():

    assert get_canonical_name("python programming") == "Python"


def test_git_alias():

    assert get_canonical_name("git version control") == "Git"


def test_tensorflow():

    assert get_canonical_name("tensorflow") == "TensorFlow"


def test_pytorch():

    assert get_canonical_name("pytorch") == "PyTorch"


def test_nlp_canonical_name():

    assert get_canonical_name("nlp") == "Natural Language Processing"


def test_transformer_parent():

    assert get_parent_skill("Transformer") == (
        "Natural Language Processing"
    )


def test_nlp_children():

    children = get_child_skills("NLP")

    assert "Transformer" in children
    assert "BERT" in children
    assert "GPT" in children


def test_skill_category():

    assert get_skill_category("Python") == (
        "Programming Language"
    )


def test_unknown_skill():

    assert get_canonical_name("SQL") == "SQL"