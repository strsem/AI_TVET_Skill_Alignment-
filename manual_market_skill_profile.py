from src.skills.market_skill_profile import (
    calculate_market_skill_profile,
    print_market_skill_profile
)

# Sample Job Postings
jobs = [

    [
        "Python",
        "Git",
        "Docker",
        "RAG"
    ],

    [
        "Python",
        "PyTorch",
        "RAG",
        "Vector Database"
    ],

    [
        "Python",
        "FastAPI",
        "Docker"
    ]

]


# Calculate Market Skill Profile
market_profile = calculate_market_skill_profile(
    jobs
)

# Print Result
print_market_skill_profile(
    market_profile
)