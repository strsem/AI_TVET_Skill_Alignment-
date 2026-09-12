from src.llm.openai_extractor import OpenAISkillExtractor


job_description = """
We are looking for a Python developer with experience
in Django, REST API, Git and SQL.

Experience with FastAPI is a plus.

Knowledge of Docker and AWS is preferred.
"""


extractor = OpenAISkillExtractor()

print("LLM is ready.")

result = extractor.extract(
    job_description
)

print("\nLLM Result:")
print(result)