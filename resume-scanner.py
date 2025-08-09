import PyPDF2

def get_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text.lower()

resume_path = input("Enter resume file path (PDF only): ")
required_skills = input("Enter required skills (comma-separated): ").lower().split(',')
resume_text = get_text_from_pdf(resume_path)
print("\n🔍 Keyword Scan Results:")

for skill in required_skills:
    skill = skill.strip()
    if skill in resume_text:
        print(f"✅ Found: {skill}")
    else:
        print(f"❌ Missing: {skill}")
print("\nScan complete! Please review the results above.")