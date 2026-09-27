from ollama import Client

from src.llm.base import SkillExtractor
from src.llm.schemas import SkillExtractionResult


class OllamaSkillExtractor(SkillExtractor):

    def __init__(
        self,
        model: str = "qwen3:4b",
        host: str = "http://localhost:11434"
    ):
        self.model = model
        self.client = Client(host=host)

    def extract(
        self,
        job_description: str
    ) -> SkillExtractionResult:

        system_prompt = """
You are a professional job-market skill extraction system.

Your task is to analyze a real job posting and extract
technical skills and professional competencies.

Rules:

1. Extract technical skills, tools, technologies,
   frameworks, methodologies and relevant competencies.

2. Each skill should be as atomic as possible.

3. Do NOT combine multiple independent technologies
   into one skill.

For example:

"REST API, PostgreSQL, Git and Docker"

must become:

REST API
PostgreSQL
Git
Docker

4. Determine whether each skill is Required or Preferred.

5. If a proficiency level is explicitly stated,
   preserve it.

6. If no proficiency level is explicitly stated,
   use "Not specified".

7. Do not invent proficiency levels.

8. Provide evidence from the job description.

9. Do not extract salary, location, benefits,
   company information or unrelated information.

10. Do not extract years of experience as a skill.

11. Return only useful skills for labor-market analysis.

12. Return the result according to the provided JSON schema.
"""

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": job_description
                }
            ],
            format=SkillExtractionResult.model_json_schema(),
            options={
                "temperature": 0
            },
            stream=False
        )

        return SkillExtractionResult.model_validate_json(
            response.message.content
        )