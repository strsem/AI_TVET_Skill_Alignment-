from src.llm.ollama_extractor import OllamaSkillExtractor

from src.skills.market_skill_profile import (
    calculate_market_skill_profile_from_extractions
)


def build_market_skill_profile(
    job_descriptions: list[dict],
    model: str = "qwen3:4b"
):

    extractor = OllamaSkillExtractor(
        model=model
    )

    return build_market_skill_profile_with_extractor(
        job_descriptions,
        extractor
    )


def build_market_skill_profile_with_extractor(
    job_descriptions: list[dict],
    extractor
):

    extraction_results = []

    for job in job_descriptions:

        print("\n" + "=" * 70)
        print("Processing:", job["title"])
        print("=" * 70)

        result = extractor.extract(
            job["description"]
        )

        extraction_results.append(
            result
        )

        print(
            "Extracted skills:",
            len(result.skills)
        )

    market_profile = (
        calculate_market_skill_profile_from_extractions(
            extraction_results
        )
    )

    return market_profile