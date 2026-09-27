import re

from src.skills.skill_ontology import (
    SKILL_ONTOLOGY,
    get_canonical_name
)


def normalize_text(text: str) -> str:
    """
    Normalize text before skill matching.

    This function:
    - removes leading/trailing spaces
    - converts English text to lowercase
    - normalizes repeated whitespace
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


def find_skills_in_text(
    text: str
) -> list[str]:
    """
    Find known ontology skills inside a larger text.

    Example:
        "REST API, PostgreSQL, Git and Docker"

    returns:
        [
            "REST API",
            "PostgreSQL",
            "Git",
            "Docker"
        ]
    """

    normalized_text = normalize_text(text)

    if not normalized_text:
        return []

    matches = []

    for concept in SKILL_ONTOLOGY.values():

        candidates = [
            concept.canonical_name,
            *concept.aliases
        ]

        for candidate in candidates:

            normalized_candidate = normalize_text(
                candidate
            )

            if not normalized_candidate:
                continue

            pattern = (
                r"(?<!\w)"
                + re.escape(normalized_candidate)
                + r"(?!\w)"
            )

            if re.search(
                pattern,
                normalized_text
            ):
                matches.append(
                    concept.canonical_name
                )

                # This concept was already found.
                # Do not add it again through another alias.
                break

    # Remove duplicates while preserving order.
    return list(
        dict.fromkeys(matches)
    )


def segment_skill(
    skill_text: str
) -> list[str]:
    """
    Convert one LLM-extracted skill phrase into
    one or more canonical skills.

    Example:

        Input:
        "Familiarity with REST API, PostgreSQL, Git,
        Docker, and Linux"

        Output:
        [
            "REST API",
            "PostgreSQL",
            "Git",
            "Docker",
            "Linux"
        ]

    If no known ontology skill is found, the original
    skill is passed to get_canonical_name().
    """

    if not skill_text:
        return []

    detected_skills = find_skills_in_text(
        skill_text
    )

    if detected_skills:
        return detected_skills

    canonical_skill = get_canonical_name(
        skill_text
    )

    if not canonical_skill:
        return []

    return [canonical_skill]


if __name__ == "__main__":

    examples = [
        "Familiarity with REST API, PostgreSQL, Git, Docker, and Linux",
        "Experience working with RAG, Embeddings, and Vector Databases",
        "Experience in designing and developing AI Agents and Agentic Systems",
        "High proficiency in Python"
    ]

    print("=" * 70)
    print("SKILL SEGMENTER TEST")
    print("=" * 70)

    for example in examples:

        print("\nInput:")
        print(example)

        print("\nDetected skills:")

        skills = segment_skill(
            example
        )

        for skill in skills:

            print(
                f"  - {skill}"
            )