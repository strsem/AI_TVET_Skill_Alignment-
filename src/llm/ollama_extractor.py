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
skills and competencies that are relevant to the job.

Rules:

1. Extract technical skills, tools, technologies,
   methodologies and relevant professional competencies.

2. Ignore salary, benefits, company introduction,
   location and unrelated information.

3. Determine whether each skill is Required or Preferred.

4. If the job posting explicitly states a proficiency level,
   preserve it.

5. If no proficiency level is explicitly stated,
   use "Not specified".

6. Do not invent proficiency levels.

7. Provide the exact or near-exact text from the job posting
   as evidence.

8. Do not create duplicate skills.

9. Return only skills that are useful for analyzing
   labor-market requirements.

10. Return the result according to the provided JSON schema.
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