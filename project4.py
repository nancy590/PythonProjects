# Project 4: Resume Keyword Analyzer (ATS Scanner)
import re

KEYWORDS = [
    "python", "java", "sql", "django", "react",
    "api", "git", "html", "css", "javascript",
    "machine learning", "data analysis"
]

def analyze_resume(text):
    text = text.lower()
    found = []
    missing = []

    for word in KEYWORDS:
        if re.search(r"\b" + re.escape(word) + r"\b", text):
            found.append(word)
        else:
            missing.append(word)

    score = int((len(found) / len(KEYWORDS)) * 100)
    return score, found, missing


def main():
    print("=== Resume Keyword Analyzer ===")
    print("Paste your resume text below (single paragraph):\n")

    resume_text = input("> ")

    score, found, missing = analyze_resume(resume_text)

    print("\n===== ATS REPORT =====")
    print(f"ATS Score : {score}%")

    print("\n✅ Keywords Found:")
    for k in found:
        print(f"- {k}")

    print("\n❌ Missing Keywords:")
    for k in missing:
        print(f"- {k}")

    if score >= 70:
        print("\n🌟 Strong resume for ATS!")
    elif score >= 40:
        print("\n👍 Decent, but needs improvement.")
    else:
        print("\n⚠️ Weak ATS optimization.")


if __name__ == "__main__":
    main()
