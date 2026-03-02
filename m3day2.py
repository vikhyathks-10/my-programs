# =====================================
# 1️⃣ Number Guessing Game (Functions)
# =====================================
import random

def number_guessing_game():
    secret = random.randint(1, 10)
    print("\nNumber Guessing Game (1–10)")

    while True:
        guess = int(input("Enter your guess: "))
        if guess == secret:
            print("Correct! You guessed it.")
            break
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

number_guessing_game()


# =====================================
# 2️⃣ Library Management (Basic)
# =====================================
def library_system():
    books = []

    while True:
        print("\nLibrary Menu")
        print("1.Add Book  2.Remove Book  3.View Books  4.Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            book = input("Enter book name: ")
            books.append(book)

        elif choice == 2:
            book = input("Enter book to remove: ")
            if book in books:
                books.remove(book)
            else:
                print("Book not found")

        elif choice == 3:
            print("Books:", books)

        elif choice == 4:
            break

        else:
            print("Invalid choice")

library_system()


# =====================================
# 3️⃣ Student Database
# =====================================
def student_database():
    students = {}

    n = int(input("\nEnter number of students: "))
    for i in range(n):
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    print("Student Database:", students)

student_database()


# =====================================
# 4️⃣ Expense Tracker
# =====================================
def expense_tracker():
    expenses = []
    total = 0

    n = int(input("\nEnter number of expenses: "))
    for i in range(n):
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)
        total += amount

    print("Total Expense:", total)
    print("Average Expense:", total / n)

expense_tracker()


# =====================================
# 5️⃣ Mini Project – To-Do List Manager
# =====================================
def todo_list():
    tasks = []

    while True:
        print("\nTo-Do Menu")
        print("1.Add Task  2.Remove Task  3.View Tasks  4.Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            task = input("Enter task: ")
            tasks.append(task)

        elif choice == 2:
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Task not found")

        elif choice == 3:
            print("Tasks:", tasks)

        elif choice == 4:
            break

        else:
            print("Invalid choice")

todo_list()