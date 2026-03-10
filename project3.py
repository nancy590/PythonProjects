# Project 3: Smart Quiz Engine with Performance Analytics

questions = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 12"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A. List", "B. Set", "C. Dictionary", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "What does len() function do?",
        "options": ["A. Adds values", "B. Deletes values", "C. Returns length", "D. Sorts values"],
        "answer": "C"
    }
]

def start_quiz():
    score = 0
    wrong = 0

    print("\n=== Smart Quiz Engine ===\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['question']}")
        for opt in q["options"]:
            print(opt)

        user_answer = input("Your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}\n")
            wrong += 1

    analyze_performance(score, wrong)

def analyze_performance(correct, wrong):
    total = correct + wrong
    percentage = (correct / total) * 100

    print("=== Quiz Result ===")
    print(f"Total Questions : {total}")
    print(f"Correct Answers : {correct}")
    print(f"Wrong Answers   : {wrong}")
    print(f"Score           : {percentage:.2f}%")

    if percentage >= 80:
        print("Performance     : Excellent 🌟")
    elif percentage >= 50:
        print("Performance     : Average 👍")
    else:
        print("Performance     : Needs Improvement 📘")

def main():
    start_quiz()
if __name__ == "__main__":
    main()
