def normalize_skill(skill: str) -> str:

    skill = skill.strip().lower()

    skill_aliases = {

        # Python
        "python programming": "Python",
        "python developer": "Python",
        "python language": "Python",

        # Machine Learning
        "ml": "Machine Learning",
        "machine learning algorithms": "Machine Learning",
        "machine-learning": "Machine Learning",

        # REST API
        "restful api": "REST API",
        "rest apis": "REST API",
        "rest api development": "REST API",

        # APIs
        "api": "APIs",

        # Scikit-learn
        "sklearn": "Scikit-learn",
        "scikit learn": "Scikit-learn",

        # LLM
        "large language model": "LLM",
        "large language models": "LLM",

        # Generative AI
        "genai": "Generative AI",
        "generative artificial intelligence": "Generative AI",

        # NumPy
        "numpy": "NumPy",

        # Pandas
        "pandas": "Pandas",

        # Django
        "django framework": "Django",
    }

    return skill_aliases.get(
        skill,
        skill.title()
    )