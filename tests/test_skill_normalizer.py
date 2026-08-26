from src.skills.skill_normalizer import normalize_skill


def test_python_normalization():

    assert normalize_skill("python") == "Python"
    assert normalize_skill("Python Programming") == "Python"
    assert normalize_skill("python developer") == "Python"


def test_machine_learning_normalization():

    assert normalize_skill("ML") == "Machine Learning"
    assert normalize_skill("Machine Learning Algorithms") == "Machine Learning"


def test_rest_api_normalization():

    assert normalize_skill("RESTful API") == "REST API"
    assert normalize_skill("REST APIs") == "REST API"


def test_llm_normalization():

    assert normalize_skill("large language model") == "LLM"