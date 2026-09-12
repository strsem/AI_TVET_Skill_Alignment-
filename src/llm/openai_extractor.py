import os

from dotenv import load_dotenv
from openai import OpenAI

from src.llm.base import SkillExtractor


class OpenAISkillExtractor(SkillExtractor):

    def init(self):

        # Load environment variables
        load_dotenv()

        # Get API key
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is not set."
            )

        # Create OpenAI client
        self.client = OpenAI(
            api_key=api_key
        )

    def extract(
            self,
            job_description: str
    ):

        response = self.client.responses.create(

            model="gpt-5.6",

            input=f"""
You are an expert job market skill analyst.

Analyze the following job description.

Extract the technical skills required for this job.

For each skill:

1. Give the canonical skill name.
2. Classify it as Required or Preferred.
3. Provide evidence from the job description.

Use only information supported by the job description.

Job Description:

{job_description}
"""
        )

        return response.output_text