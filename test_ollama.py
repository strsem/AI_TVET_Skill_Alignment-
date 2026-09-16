from src.llm.ollama_extractor import OllamaSkillExtractor
from src.skills.normalized_skills import normalize_extracted_skills

from src.skills.market_skill_profile import (
    calculate_market_skill_profile,
    print_market_skill_profile
)

from src.skills.skill_ontology import (
    get_skill_concept,
    get_canonical_name
)


# JOB DESCRIPTION
job_description = """
شرکت دانش‌پژوهان آروشا جهت توسعه محصولات هوشمند خود در حوزه‌های پردازش
زبان طبیعی و هوش مصنوعی نیروی متخصص جذب می‌کند.

شرایط احراز:

کارشناسی ارشد کامپیوتر یا فناوری اطلاعات

Python پیشرفته
GIT متوسط
Docker مقدماتی
زبان انگلیسی متوسط

شرح وظایف:

- توسعه مدل‌های پیشرفته NLP
- طبقه‌بندی متن
- استخراج موجودیت‌ها
- تولید متن خلاقانه
- توسعه و استفاده از Knowledge Graph
- استنتاج روی گراف دانش
- تولید متن با استفاده از LLM
- جمع‌آوری، پاک‌سازی و آماده‌سازی داده‌های متنی در مقیاس بزرگ
- کار با Vector Database
- Document Database
- Text Database
- Graph Database
- استفاده از APIهای هوش مصنوعی
- تحقیق و توسعه در حوزه NLP و Knowledge Graph
- مستندسازی فنی
- یکپارچه‌سازی مدل‌های هوش مصنوعی با محصولات

مهارت‌های مورد نیاز:

- تسلط به Python
- TensorFlow یا PyTorch
- Hugging Face Transformers
- آشنایی عمیق با الگوریتم‌های NLP مانند Transformer، BERT و GPT
- توانایی حل مسئله و تفکر منطقی
- توانایی کار تیمی و روش‌های Agile
- پردازش حجم زیادی از داده‌های متنی
- توانایی درک مسائل پیچیده کسب‌وکار و ارائه راهکارهای داده‌محور
- Docker
- Web Service و FastAPI

مهارت‌های ترجیحی:

- Semantic Search
- RAG
- Vector Database
- Document Database
- Neo4j
- Cypher
- Distributed Systems
- Microservices
- Messaging
- Git
- CI/CD
- DevOps
"""


# 1. LLM EXTRACTION
extractor = OllamaSkillExtractor(
    model="qwen3:4b"
)

result = extractor.extract(
    job_description
)

print("\n")
print("LLM EXTRACTION")
print(f"\nTotal extracted skills: {len(result.skills)}")

for skill in result.skills:
    print(
        f"\nSkill        : {skill.skill}"
        f"\nCategory     : {skill.category}"
        f"\nImportance   : {skill.importance}"
        f"\nProficiency  : {skill.proficiency}"
        f"\nEvidence     : {skill.evidence}"
    )

# 2. NORMALIZATION
normalized_skills = normalize_extracted_skills(
    result
)


print("\n")
print("NORMALIZED SKILLS")

for skill in normalized_skills:

    print(
        f"{skill['original_skill']:<60}"
        f" -> {skill['skill']}"
    )


# 3. SUMMARY
required_count = sum(
    1
    for skill in normalized_skills
    if skill["importance"] == "Required"
)


preferred_count = sum(
    1
    for skill in normalized_skills
    if skill["importance"] == "Preferred"
)


print("\n")
print("SUMMARY")
print(f"Required skills : {required_count}")
print(f"Preferred skills: {preferred_count}")
print(f"Total skills    : {len(normalized_skills)}")

# 4. ONTOLOGY CHECK
known_skills = []
unknown_skills = []


for skill in normalized_skills:
    skill_name = skill["skill"]
    concept = get_skill_concept(
        skill_name
    )

    if concept is not None:
        known_skills.append(
            skill_name
        )

    else:
        unknown_skills.append(
            skill_name
        )

# حذف موارد تکراری
known_skills = list(
    dict.fromkeys(known_skills)
)

unknown_skills = list(
    dict.fromkeys(unknown_skills)
)


print("\n")
print("ONTOLOGY CHECK")
print(f"\nKnown skills   : {len(known_skills)}")

for skill in known_skills:
    print(f"  ✓ {skill}")

print(f"\nUnknown skills : {len(unknown_skills)}")

for skill in unknown_skills:
    print(f"  ? {skill}")



# 5. CANONICAL SKILLS
canonical_skills = []
for skill in normalized_skills:
    skill_name = skill["skill"]
    canonical_name = get_canonical_name(
        skill_name
    )
    canonical_skills.append(
        canonical_name
    )

# حذف تکراری‌ها
canonical_skills = list(
    dict.fromkeys(canonical_skills)
)

print("\n")
print("CANONICAL SKILLS")
for skill in canonical_skills:
    print(f"  {skill}")

# 6. MARKET SKILL PROFILE
# فعلاً این Job را به عنوان یک Job واقعی وارد می‌کنیم.
# بعداً همین قسمت را به چندین Job Posting وصل می‌کنیم.

jobs = [canonical_skills]
market_profile = calculate_market_skill_profile(
    jobs
)

print_market_skill_profile(market_profile)