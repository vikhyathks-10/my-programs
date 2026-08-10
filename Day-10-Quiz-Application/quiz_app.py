import tkinter as tk
from tkinter import messagebox


class QuizApplication:

    def __init__(self, root):

        self.root = root
        self.root.title("Python Quiz Application")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        # Questions
        self.questions = [
            {
                "question": "Which language is used to create this application?",
                "options": ["Java", "Python", "C++", "JavaScript"],
                "answer": "Python"
            },
            {
                "question": "Which keyword is used to create a class in Python?",
                "options": ["function", "class", "object", "define"],
                "answer": "class"
            },
            {
                "question": "Which library is used for GUI development in this project?",
                "options": ["Pandas", "NumPy", "Tkinter", "Requests"],
                "answer": "Tkinter"
            },
            {
                "question": "Which data type stores multiple values in an ordered collection?",
                "options": ["List", "Integer", "Boolean", "Float"],
                "answer": "List"
            },
            {
                "question": "Which method is used to create a constructor in Python?",
                "options": ["__start__", "__new__", "__init__", "__create__"],
                "answer": "__init__"
            },
            {
                "question": "Which database did you use in Day 9?",
                "options": ["MongoDB", "SQLite", "MySQL", "Oracle"],
                "answer": "SQLite"
            },
            {
                "question": "Which symbol is used for comments in Python?",
                "options": ["//", "/*", "#", "<!--"],
                "answer": "#"
            },
            {
                "question": "Which function is used to display output in Python?",
                "options": ["display()", "output()", "print()", "show()"],
                "answer": "print()"
            },
            {
                "question": "Which keyword is used to handle exceptions?",
                "options": ["try", "check", "error", "handle"],
                "answer": "try"
            },
            {
                "question": "Which file format is commonly used to store structured data?",
                "options": ["JSON", "EXE", "PNG", "MP3"],
                "answer": "JSON"
            }
        ]

        self.current_question = 0
        self.score = 0
        self.selected_answer = tk.StringVar()

        self.create_widgets()
        self.show_question()

    # ======================================
    # CREATE GUI
    # ======================================

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="Python Programming Quiz",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        self.progress_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12)
        )

        self.progress_label.pack(pady=5)

        self.question_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 16, "bold"),
            wraplength=500,
            justify="center"
        )

        self.question_label.pack(pady=25)

        self.option_buttons = []

        for i in range(4):

            button = tk.Radiobutton(
                self.root,
                text="",
                variable=self.selected_answer,
                value="",
                font=("Arial", 13),
                anchor="w",
                width=35
            )

            button.pack(pady=5)

            self.option_buttons.append(button)

        self.next_button = tk.Button(
            self.root,
            text="Next",
            font=("Arial", 13, "bold"),
            width=15,
            command=self.next_question
        )

        self.next_button.pack(pady=25)

    # ======================================
    # DISPLAY QUESTION
    # ======================================

    def show_question(self):

        question_data = self.questions[self.current_question]

        self.progress_label.config(
            text=f"Question {self.current_question + 1} "
                 f"of {len(self.questions)}"
        )

        self.question_label.config(
            text=question_data["question"]
        )

        self.selected_answer.set("")

        for i in range(4):

            self.option_buttons[i].config(
                text=question_data["options"][i],
                value=question_data["options"][i]
            )

        if self.current_question == len(self.questions) - 1:

            self.next_button.config(
                text="Finish"
            )

        else:

            self.next_button.config(
                text="Next"
            )

    # ======================================
    # NEXT QUESTION
    # ======================================

    def next_question(self):

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

        self.current_question += 1

        if self.current_question < len(self.questions):

            self.show_question()

        else:

            self.show_result()

    # ======================================
    # SHOW RESULT
    # ======================================

    def show_result(self):

        percentage = (
            self.score / len(self.questions)
        ) * 100

        self.progress_label.config(
            text="Quiz Completed!"
        )

        self.question_label.config(
            text=f"Your Score\n\n"
                 f"{self.score} / {len(self.questions)}\n\n"
                 f"Percentage: {percentage:.1f}%"
        )

        for button in self.option_buttons:

            button.pack_forget()

        self.next_button.config(
            text="Restart Quiz",
            command=self.restart_quiz
        )

    # ======================================
    # RESTART QUIZ
    # ======================================

    def restart_quiz(self):

        self.current_question = 0
        self.score = 0

        for button in self.option_buttons:

            button.pack(
                pady=5
            )

        self.next_button.config(
            text="Next",
            command=self.next_question
        )

        self.show_question()


# ==========================================
# MAIN
# ==========================================

root = tk.Tk()

app = QuizApplication(root)

root.mainloop()