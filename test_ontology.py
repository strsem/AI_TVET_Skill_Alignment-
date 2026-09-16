from src.skills.skill_ontology import (
    get_skill_concept,
    get_canonical_name,
    get_parent_skill
)

from src.skills.requirement_logic import (
    print_requirements
)

# Test 1
skill = get_skill_concept("python")

print("SKILL ONTOLOGY")
print("Skill ID:", skill.skill_id)
print("Canonical Name:", skill.canonical_name)
print("Category:", skill.category)
print("Aliases:", skill.aliases)


# Test 2
print("\n" + "=" * 60)
print("CANONICAL NAME")
print("=" * 60)

print(
    "GIT ->",
    get_canonical_name("GIT")
)
print(
    "python ->",
    get_canonical_name("python")
)
print(
    "vector db ->",
    get_canonical_name("vector db")
)

# Test 3
print("\n" + "=" * 60)
print("PARENT SKILL")

print(
    "Transformer parent:",
    get_parent_skill("Transformer")
)

print(
    "BERT parent:",
    get_parent_skill("BERT")
)

# Test 4
print("REQUIREMENT LOGIC")
print("=" * 60)

print_requirements()