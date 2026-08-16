import tkinter as tk
from tkinter import messagebox
import json


class QuizApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Application")
        self.root.geometry("650x550")
        self.root.resizable(False, False)

        # Load questions
        self.load_questions()

        self.current_question = 0
        self.score = 0
        self.selected_answer = tk.StringVar()

        # Title
        self.title_label = tk.Label(
            root,
            text="🧠 Python Quiz",
            font=("Arial", 26, "bold")
        )
        self.title_label.pack(pady=20)

        # Question number
        self.question_number = tk.Label(
            root,
            text="",
            font=("Arial", 13)
        )
        self.question_number.pack(pady=5)

        # Question
        self.question_label = tk.Label(
            root,
            text="",
            font=("Arial", 17, "bold"),
            wraplength=550,
            justify="center"
        )
        self.question_label.pack(pady=20)

        # Options
        self.option_buttons = []

        for i in range(4):
            button = tk.Radiobutton(
                root,
                text="",
                variable=self.selected_answer,
                value="",
                font=("Arial", 14),
                anchor="w",
                width=35
            )

            button.pack(pady=5)

            self.option_buttons.append(button)

        # Submit button
        self.submit_button = tk.Button(
            root,
            text="✅ Submit Answer",
            font=("Arial", 13, "bold"),
            command=self.check_answer
        )
        self.submit_button.pack(pady=20)

        # Score
        self.score_label = tk.Label(
            root,
            text="Score: 0",
            font=("Arial", 13, "bold")
        )
        self.score_label.pack()

        # Load first question
        self.show_question()

    def load_questions(self):
        try:
            with open("questions.json", "r") as file:
                self.questions = json.load(file)

        except FileNotFoundError:
            messagebox.showerror(
                "Error",
                "questions.json file not found."
            )
            self.root.destroy()

        except json.JSONDecodeError:
            messagebox.showerror(
                "Error",
                "Invalid JSON file."
            )
            self.root.destroy()

    def show_question(self):

        if self.current_question >= len(self.questions):
            self.show_result()
            return

        question = self.questions[self.current_question]

        self.question_number.config(
            text=f"Question {self.current_question + 1} "
                 f"of {len(self.questions)}"
        )

        self.question_label.config(
            text=question["question"]
        )

        self.selected_answer.set("")

        for i, option in enumerate(question["options"]):

            self.option_buttons[i].config(
                text=option,
                value=option
            )

    def check_answer(self):

        selected = self.selected_answer.get()

        if not selected:
            messagebox.showwarning(
                "No Answer",
                "Please select an answer."
            )
            return

        correct_answer = self.questions[
            self.current_question
        ]["answer"]

        if selected == correct_answer:
            self.score += 1

            messagebox.showinfo(
                "Correct!",
                "🎉 Correct Answer!"
            )

        else:
            messagebox.showerror(
                "Wrong Answer",
                f"❌ Wrong Answer!\n\n"
                f"Correct Answer: {correct_answer}"
            )

        self.score_label.config(
            text=f"Score: {self.score}"
        )

        self.current_question += 1

        if self.current_question < len(self.questions):

            self.submit_button.config(
                text="➡️ Next Question"
            )

            self.submit_button.config(
                command=self.next_question
            )

        else:

            self.submit_button.config(
                text="🏆 View Result"
            )

            self.submit_button.config(
                command=self.show_result
            )

    def next_question(self):

        self.submit_button.config(
            text="✅ Submit Answer",
            command=self.check_answer
        )

        self.show_question()

    def show_result(self):

        total = len(self.questions)

        percentage = (self.score / total) * 100

        messagebox.showinfo(
            "Quiz Completed",
            f"🎉 Quiz Completed!\n\n"
            f"Your Score: {self.score}/{total}\n"
            f"Percentage: {percentage:.1f}%"
        )

        self.submit_button.config(
            text="🔄 Restart Quiz",
            command=self.restart_quiz
        )

    def restart_quiz(self):

        self.current_question = 0
        self.score = 0

        self.score_label.config(
            text="Score: 0"
        )

        self.submit_button.config(
            text="✅ Submit Answer",
            command=self.check_answer
        )

        self.show_question()


# Create application
root = tk.Tk()

app = QuizApp(root)

root.mainloop()