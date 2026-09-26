from src.llm.ollama_extractor import OllamaSkillExtractor
from src.skills.normalized_skills import normalize_extracted_skills


# نمونه آگهی شغلی

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


# 1. استخراج مهارت‌ها با LLM
extractor = OllamaSkillExtractor(
    model="qwen3:4b"
)

result = extractor.extract(job_description)


# 2. نمایش خروجی خام LLM
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


# 3. نرمال‌سازی مهارت‌ها
normalized_skills = normalize_extracted_skills(result)

# 4. نمایش خروجی نرمال‌شده
print("NORMALIZED SKILLS")
for skill in normalized_skills:

    print(
        f"{skill['original_skill']:<60}"
        f" -> {skill['skill']}"
    )


# 5. خلاصه اهمیت مهارت‌ها
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
