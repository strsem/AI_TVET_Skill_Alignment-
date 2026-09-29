import re

from src.skills.skill_ontology import (
    SKILL_ONTOLOGY,
    get_canonical_name,
)


def normalize_text(
    text: str
) -> str:
    """
    Normalize text before skill matching.

    Operations:
    - remove leading/trailing spaces
    - convert text to lowercase
    - replace repeated whitespace with one space
    """

    if not text:
        return ""

    text = text.strip().lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text


def _build_match_pattern(
    candidate: str
) -> str:
    """
    Build a regex pattern for exact skill-phrase matching.

    The '-' character is treated as part of a token.
    This prevents:

        GPT

    from incorrectly matching:

        GPT-OSS
    """

    normalized_candidate = normalize_text(
        candidate
    )

    return (
        r"(?<![\w-])"
        + re.escape(normalized_candidate)
        + r"(?![\w-])"
    )


def find_skills_in_text(
    text: str
) -> list[str]:
    """
    Find ontology skills inside a piece of text.

    Each detected alias is converted to its canonical skill name.

    Example:

        "REST API, PostgreSQL, Git and Docker"

    becomes:

        [
            "PostgreSQL",
            "REST API",
            "Git",
            "Docker"
        ]
    """

    normalized_text = normalize_text(
        text
    )

    if not normalized_text:
        return []

    candidates = []

    # ---------------------------------------------------------
    # Collect canonical names and aliases from ontology
    # ---------------------------------------------------------

    for concept in SKILL_ONTOLOGY.values():

        candidates.append(
            (
                concept.canonical_name,
                concept.canonical_name
            )
        )

        for alias in concept.aliases:

            candidates.append(
                (
                    alias,
                    concept.canonical_name
                )
            )

    # ---------------------------------------------------------
    # Remove duplicate phrases
    # ---------------------------------------------------------

    unique_candidates = {}

    for candidate, canonical_name in candidates:

        normalized_candidate = normalize_text(
            candidate
        )

        if not normalized_candidate:
            continue

        unique_candidates[
            normalized_candidate
        ] = canonical_name

    # ---------------------------------------------------------
    # Longer phrases first
    #
    # Example:
    #
    # OpenAI Agents SDK
    #
    # should be checked before:
    #
    # OpenAI Agents
    # ---------------------------------------------------------

    ordered_candidates = sorted(
        unique_candidates.items(),
        key=lambda item: len(item[0]),
        reverse=True
    )

    matches = []

    # ---------------------------------------------------------
    # Search every ontology phrase in the text
    # ---------------------------------------------------------

    for candidate, canonical_name in ordered_candidates:

        pattern = _build_match_pattern(
            candidate
        )

        if re.search(
            pattern,
            normalized_text
        ):
            matches.append(
                canonical_name
            )

    # ---------------------------------------------------------
    # Remove duplicate canonical skills
    # ---------------------------------------------------------

    return list(
        dict.fromkeys(matches)
    )


def segment_skill(
    skill_text: str
) -> list[str]:
    """
    Convert an extracted skill phrase into canonical skills.

    Examples:

        "Python"
        ->
        ["Python"]

        "REST API, PostgreSQL, Git and Docker"
        ->
        ["PostgreSQL", "REST API", "Git", "Docker"]

        "Agent Memory, State Management, Agent Orchestration"
        ->
        [
            "Agent Memory",
            "State Management",
            "Agent Orchestration"
        ]
    """

    if not skill_text:
        return []

    # First try to find multiple skills inside the text.
    detected_skills = find_skills_in_text(
        skill_text
    )

    if detected_skills:
        return detected_skills

    # ---------------------------------------------------------
    # If nothing was found, try exact ontology lookup.
    # ---------------------------------------------------------

    canonical_skill = get_canonical_name(
        skill_text
    )

    if not canonical_skill:
        return []

    return [
        canonical_skill
    ]


# ============================================================
# Standalone test
# ============================================================

if __name__ == "__main__":

    examples = [

        "Familiarity with REST API, PostgreSQL, Git, Docker, and Linux",

        "Experience working with RAG, Embeddings, and Vector Databases",

        "Experience in designing and developing AI Agents and Agentic Systems",

        "Experience with Agent Memory, State Management, and Agent Orchestration",

        "Experience with OpenAI Agents SDK, LangGraph, MCP, and LlamaIndex",

        "Familiarity with Qwen, Mistral, GPT-OSS, Gemma, and Whisper",

        "High proficiency in Python",

        "Experience with Django and SQL",

        "Cloud Infrastructure and AWS",

        "This text contains an unknown technology"
    ]

    print("=" * 72)
    print("SKILL SEGMENTER TEST")
    print("=" * 72)

    for example in examples:

        print("\nInput:")
        print(example)

        skills = segment_skill(
            example
        )

        print("\nDetected skills:")

        if not skills:

            print(
                "  - No ontology skill detected"
            )

            continue

        for skill in skills:

            print(
                f"  - {skill}"
            )

    # ========================================================
    # Expected checks
    # ========================================================

    print("\n" + "=" * 72)
    print("EXPECTED CHECKS")
    print("=" * 72)

    checks = {

        "Agent Memory":
            "Experience with Agent Memory, State Management, "
            "and Agent Orchestration",

        "State Management":
            "Experience with Agent Memory, State Management, "
            "and Agent Orchestration",

        "Agent Orchestration":
            "Experience with Agent Memory, State Management, "
            "and Agent Orchestration",

        "GPT-OSS":
            "Qwen, Mistral, GPT-OSS, Gemma, and Whisper",

        "Python":
            "High proficiency in Python",

        "Vector Database":
            "Experience working with RAG, Embeddings, and Vector Databases",

        "AI Agents":
            "Experience in designing and developing AI Agents "
            "and Agentic Systems",

    }

    all_passed = True

    for expected_skill, text in checks.items():

        result = segment_skill(
            text
        )

        passed = (
            expected_skill in result
        )

        if passed:

            print(
                f"PASS: {expected_skill}"
            )

        else:

            print(
                f"FAIL: {expected_skill}"
            )

            print(
                f"      Result: {result}"
            )

            all_passed = False

    # ========================================================
    # Final result
    # ========================================================
    print("\n" + "=" * 72)

    if all_passed:
        print("All standalone checks passed.")

    else:
        print("Some standalone checks failed.")

    print("=" * 72)
