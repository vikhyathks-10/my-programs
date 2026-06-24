# 🔹 DAY 24 - PROJECT REFACTORING PRACTICE


# ==========================================
# 🔹 COMMON HELPER CLASS
# ==========================================

class Utility:

    @staticmethod
    def display_header(title):

        print("\n" + "=" * 40)

        print(title)

        print("=" * 40)


# ==========================================
# 🔹 1. REFACTORED CALCULATOR
# ==========================================

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):

        if b == 0:
            return "Cannot Divide By Zero"

        return a / b


# ==========================================
# 🔹 2. REFACTORED STUDENT SYSTEM
# ==========================================

class Student:

    def __init__(self, name, marks):

        self.name = name

        self.marks = marks

    def grade(self):

        if self.marks >= 90:
            return "A+"

        elif self.marks >= 80:
            return "A"

        elif self.marks >= 70:
            return "B"

        elif self.marks >= 60:
            return "C"

        return "F"

    def display(self):

        print(
            f"Name: {self.name} | "
            f"Marks: {self.marks} | "
            f"Grade: {self.grade()}"
        )


# ==========================================
# 🔹 3. REFACTORED ATM PROJECT
# ==========================================

class ATM:

    def __init__(self):

        self.balance = 5000

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        if amount > self.balance:

            print("Insufficient Balance")

        else:

            self.balance -= amount

    def show_balance(self):

        print(
            f"Balance: ₹{self.balance}"
        )


# ==========================================
# 🔹 4. REFACTORED EXPENSE TRACKER
# ==========================================

class ExpenseTracker:

    def __init__(self):

        self.expenses = []

    def add_expense(self, amount):

        self.expenses.append(amount)

    def total_expense(self):

        return sum(self.expenses)

    def display(self):

        print(
            "Expenses:",
            self.expenses
        )

        print(
            "Total:",
            self.total_expense()
        )


# ==========================================
# 🔹 5. REFACTORED QUIZ APP
# ==========================================

class Quiz:

    def __init__(self):

        self.questions = {

            "Capital of India": "Delhi",

            "2 + 2": "4",

            "Python Creator":
            "Guido van Rossum"
        }

        self.score = 0

    def start(self):

        for question, answer in self.questions.items():

            user_answer = input(
                f"{question}: "
            )

            if user_answer.lower() == answer.lower():

                self.score += 1

        print(
            f"\nScore: "
            f"{self.score}/"
            f"{len(self.questions)}"
        )


# ==========================================
# 🔹 MAIN PROGRAM
# ==========================================

while True:

    Utility.display_header(
        "DAY 24 REFACTORING PRACTICE"
    )

    print("1. Refactored Calculator")

    print("2. Refactored Student System")

    print("3. Refactored ATM")

    print("4. Refactored Expense Tracker")

    print("5. Refactored Quiz App")

    print("6. Exit")

    choice = input(
        "\nEnter Choice: "
    )

    # ----------------------------------

    if choice == "1":

        Utility.display_header(
            "CALCULATOR"
        )

        calc = Calculator()

        a = float(
            input("Enter First Number: ")
        )

        b = float(
            input("Enter Second Number: ")
        )

        print(
            "Addition:",
            calc.add(a, b)
        )

        print(
            "Subtraction:",
            calc.subtract(a, b)
        )

        print(
            "Multiplication:",
            calc.multiply(a, b)
        )

        print(
            "Division:",
            calc.divide(a, b)
        )

    # ----------------------------------

    elif choice == "2":

        Utility.display_header(
            "STUDENT SYSTEM"
        )

        name = input(
            "Enter Name: "
        )

        marks = float(
            input(
                "Enter Marks: "
            )
        )

        student = Student(
            name,
            marks
        )

        student.display()

    # ----------------------------------

    elif choice == "3":

        Utility.display_header(
            "ATM"
        )

        atm = ATM()

        amount = float(
            input(
                "Deposit Amount: "
            )
        )

        atm.deposit(amount)

        atm.show_balance()

        amount = float(
            input(
                "Withdraw Amount: "
            )
        )

        atm.withdraw(amount)

        atm.show_balance()

    # ----------------------------------

    elif choice == "4":

        Utility.display_header(
            "EXPENSE TRACKER"
        )

        tracker = ExpenseTracker()

        count = int(
            input(
                "How Many Expenses: "
            )
        )

        for _ in range(count):

            amount = float(
                input(
                    "Expense Amount: "
                )
            )

            tracker.add_expense(
                amount
            )

        tracker.display()

    # ----------------------------------

    elif choice == "5":

        Utility.display_header(
            "QUIZ APP"
        )

        quiz = Quiz()

        quiz.start()

    # ----------------------------------

    elif choice == "6":

        print(
            "\nGoodbye 👋"
        )

        break

    else:

        print(
            "\nInvalid Choice"
        )