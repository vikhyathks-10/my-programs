questions = [
    {"question": "What is the capital of India?", "answer": "Delhi"},
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "What is the color of the sky?", "answer": "Blue"}
]

score = 0

for q in questions:
    user_ans = input(q["question"] + " ")
    if user_ans.strip().lower() == q["answer"].lower():
        print(" Correct!\n")
        score += 1
    else:
        print(" Wrong!\n")

print(f"Your final score is: {score}/{len(questions)}")
