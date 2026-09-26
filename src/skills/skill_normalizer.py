def normalize_skill(skill: str) -> str:
    """
    Convert different names of the same skill
    into a standard skill name.
    """

    skill = skill.strip().lower()

    skill_aliases = {

        # -------------------------
        # Programming
        # -------------------------

        "python programming": "Python",
        "python developer": "Python",
        "python language": "Python",

        # -------------------------
        # Version Control
        # -------------------------

        "git": "Git",
        "git version control": "Git",

        # -------------------------
        # Machine Learning
        # -------------------------

        "ml": "Machine Learning",
        "machine learning algorithms": "Machine Learning",

        "tensorflow": "TensorFlow",
        "pytorch": "PyTorch",

        # -------------------------
        # NLP
        # -------------------------

        "natural language processing": "NLP",
        "nlp algorithms": "NLP",
        "deep knowledge of nlp algorithms": "NLP",

        "transformer": "Transformer",
        "transformers": "Transformer",

        "bert": "BERT",
        "gpt": "GPT",

        # -------------------------
        # LLM
        # -------------------------

        "large language model": "LLM",
        "large language models": "LLM",

        # -------------------------
        # Hugging Face
        # -------------------------

        "hugging face transformers": "Hugging Face Transformers",

        # -------------------------
        # Databases
        # -------------------------

        "vector database": "Vector Database",
        "vector db": "Vector Database",

        "document database": "Document Database",
        "document db": "Document Database",

        "graph database": "Graph Database",
        "graph db": "Graph Database",

        # -------------------------
        # Knowledge Graph
        # -------------------------

        "knowledge graph": "Knowledge Graph",
        "knowledge graphs": "Knowledge Graph",

        # -------------------------
        # APIs / Web
        # -------------------------

        "api": "APIs",
        "apis": "APIs",

        "rest api": "REST API",
        "rest apis": "REST API",

        "web service": "Web Service",

        "web service and fastapi": "FastAPI",

        "fastapi": "FastAPI",

        # -------------------------
        # Search / RAG
        # -------------------------

        "semantic search": "Semantic Search",
        "rag": "RAG",

        # -------------------------
        # DevOps
        # -------------------------

        "docker": "Docker",
        "ci/cd": "CI/CD",
        "devops": "DevOps",

        # -------------------------
        # Architecture
        # -------------------------

        "microservices": "Microservices",
        "distributed systems": "Distributed Systems",

        # -------------------------
        # Graph
        # -------------------------

        "neo4j": "Neo4j",
        "cypher": "Cypher",

        # -------------------------
        # Soft skills
        # -------------------------

        "problem solving": "Problem Solving",
        "problem-solving and logical thinking": "Problem Solving",

        "teamwork and agile methods": "Teamwork & Agile",

        # -------------------------
        # Data
        # -------------------------

        "large text data processing": "Large-Scale Text Processing",
        "processing large volumes of text data":
            "Large-Scale Text Processing",

        # -------------------------
        # Language
        # -------------------------

        "english": "English",
    }

    return skill_aliases.get(skill, skill.title())



from src.skills.skill_ontology import get_canonical_name
def normalize_skill(skill: str) -> str:
    """
    Convert a skill name into its canonical ontology name.
    """
    if not skill:
        return ""

    return get_canonical_name(skill)