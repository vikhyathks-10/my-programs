# 🔹 DAY 17 - QUIZ APP

import random


class QuizApp:

    def __init__(self):

        self.score = 0

        self.question_bank = [

            {
                "question": "What is the capital of India?",
                "options": ["A. Mumbai",
                            "B. Delhi",
                            "C. Chennai",
                            "D. Kolkata"],
                "answer": "B"
            },

            {
                "question": "Which language is used for AI and Data Science?",
                "options": ["A. Java",
                            "B. C",
                            "C. Python",
                            "D. PHP"],
                "answer": "C"
            },

            {
                "question": "What is 10 + 20?",
                "options": ["A. 20",
                            "B. 25",
                            "C. 30",
                            "D. 40"],
                "answer": "C"
            },

            {
                "question": "Which data structure follows FIFO?",
                "options": ["A. Stack",
                            "B. Queue",
                            "C. Tree",
                            "D. Graph"],
                "answer": "B"
            },

            {
                "question": "Which keyword is used to create a class in Python?",
                "options": ["A. function",
                            "B. define",
                            "C. class",
                            "D. object"],
                "answer": "C"
            }

        ]

    # =====================================
    # 🔹 Start Quiz
    # =====================================

    def start_quiz(self):

        print("\n===== QUIZ APP =====\n")

        questions = random.sample(
            self.question_bank,
            len(self.question_bank)
        )

        for i, q in enumerate(questions, start=1):

            print(f"\nQuestion {i}")

            print(q["question"])

            for option in q["options"]:
                print(option)

            user_answer = input(
                "\nEnter Answer (A/B/C/D): "
            ).upper()

            if user_answer == q["answer"]:

                print("✅ Correct")

                self.score += 1

            else:

                print(
                    f"❌ Wrong | Correct Answer: {q['answer']}"
                )

    # =====================================
    # 🔹 Result Summary
    # =====================================

    def show_result(self):

        total = len(self.question_bank)

        percentage = (
            self.score / total
        ) * 100

        print("\n===== RESULT SUMMARY =====")

        print("Total Questions :", total)

        print("Correct Answers :", self.score)

        print("Wrong Answers   :", total - self.score)

        print(
            f"Percentage      : {percentage:.2f}%"
        )

        if percentage >= 80:

            print("Grade           : A")

        elif percentage >= 60:

            print("Grade           : B")

        elif percentage >= 40:

            print("Grade           : C")

        else:

            print("Grade           : F")


# =====================================
# 🔹 MAIN PROGRAM
# =====================================

quiz = QuizApp()

quiz.start_quiz()

quiz.show_result()