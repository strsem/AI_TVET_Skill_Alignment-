from src.llm.ollama_extractor import OllamaSkillExtractor
from src.skills.skill_segmenter import segment_skill
from src.skills.normalized_skills import normalize_extracted_skills


job_description = """
We are looking for an AI Engineer who can design and develop
AI-powered products and Agentic AI systems.

Requirements:

- High proficiency in Python.
- Experience working with LLM APIs.
- Experience developing applications based on LLMs.
- Experience with RAG, Embeddings, and Vector Databases.
- Familiarity with Function Calling and Tool Calling.
- Understanding of Agent Memory, State Management,
  and Agent Orchestration.
- Experience designing and developing AI Agents
  and Agentic Systems.
- Deep knowledge of Prompt Engineering
  and Context Engineering.
- Familiarity with REST API, PostgreSQL, Git, Docker,
  and Linux.
- Familiarity with LangGraph, LangChain, MCP,
  FastAPI, Redis, and n8n.
"""


def main():

    print("=" * 70)
    print("REALISTIC OLLAMA SKILL EXTRACTION TEST")
    print("=" * 70)

    extractor = OllamaSkillExtractor(
        model="qwen3:4b"
    )

    print("\nOllama is ready.")

    # --------------------------------------------------
    # 1. LLM EXTRACTION
    # --------------------------------------------------

    result = extractor.extract(
        job_description
    )

    print("\n")
    print("=" * 70)
    print("1. RAW LLM RESULT")
    print("=" * 70)

    for skill in result.skills:

        print(
            f"\nSkill: {skill.skill}"
        )

        print(
            f"Category: {skill.category}"
        )

        print(
            f"Importance: {skill.importance}"
        )

        print(
            f"Proficiency: {skill.proficiency}"
        )

        print(
            f"Evidence: {skill.evidence}"
        )

    # --------------------------------------------------
    # 2. SEGMENTATION
    # --------------------------------------------------

    print("\n")
    print("=" * 70)
    print("2. SEGMENTED SKILLS")
    print("=" * 70)

    segmented_skills = []

    for extracted_skill in result.skills:

        skills = segment_skill(
            extracted_skill.skill
        )

        segmented_skills.extend(
            skills
        )

    segmented_skills = list(
        dict.fromkeys(segmented_skills)
    )

    for skill in segmented_skills:

        print(
            f"  - {skill}"
        )

    # --------------------------------------------------
    # 3. NORMALIZATION
    # --------------------------------------------------

    print("\n")
    print("=" * 70)
    print("3. NORMALIZED SKILLS")
    print("=" * 70)

    normalized_result = normalize_extracted_skills(
        result
    )

    for skill in normalized_result:

        print(
            skill
        )

    # --------------------------------------------------
    # 4. SUMMARY
    # --------------------------------------------------

    print("\n")
    print("=" * 70)
    print("4. SUMMARY")
    print("=" * 70)

    print(
        f"LLM extracted: "
        f"{len(result.skills)} skills"
    )

    print(
        f"Segmented: "
        f"{len(segmented_skills)} skills"
    )

    print(
        f"Normalized: "
        f"{len(normalized_result)} skills"
    )


if __name__ == "__main__":
    main()