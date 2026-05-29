# 🔹 DAY 29 - COMBINED PRACTICE DAY

import re
import time
from collections import Counter


# ==================================================
# 🔹 1. REGEX + FILE HANDLING
# Email Extractor from File
# ==================================================

def email_extractor():

    print("\n--- Regex + File Handling ---")

    with open("contacts.txt", "w") as file:

        file.write("""
        vikyat@gmail.com
        test@yahoo.com
        hello123@company.org
        """)

    with open("contacts.txt", "r") as file:

        data = file.read()

    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        data
    )

    print("Emails Found:")

    for email in emails:
        print(email)


# ==================================================
# 🔹 2. AUTOMATION + DSA
# Task Manager using Queue
# ==================================================

class TaskQueue:

    def __init__(self):

        self.tasks = []

    def add_task(self, task):

        self.tasks.append(task)

    def process_task(self):

        if self.tasks:

            return self.tasks.pop(0)

        return "No Tasks"

    def show_tasks(self):

        print("Pending Tasks:", self.tasks)


# ==================================================
# 🔹 3. OOP + PROJECT LOGIC
# Employee Management
# ==================================================

class Employee:

    def __init__(self, emp_id, name, salary):

        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):

        print(
            self.emp_id,
            self.name,
            self.salary
        )


class EmployeeManager:

    def __init__(self):

        self.employees = []

    def add_employee(self, emp):

        self.employees.append(emp)

    def display_all(self):

        print("\nEmployees:")

        for emp in self.employees:
            emp.display()


# ==================================================
# 🔹 4. OPTIMIZATION CHALLENGE
# Optimized Frequency Counter
# ==================================================

def frequency_counter(text):

    print("\n--- Optimization Challenge ---")

    freq = Counter(text)

    print(freq)


# ==================================================
# 🔹 5. DEBUGGING OLD PROJECT
# Fixed Calculator
# ==================================================

def calculator(a, b, op):

    if op == "+":
        return a + b

    elif op == "-":
        return a - b

    elif op == "*":
        return a * b

    elif op == "/":

        if b == 0:
            return "Cannot Divide by Zero"

        return a / b

    return "Invalid Operator"


# ==================================================
# 🔹 MAIN PROGRAM
# ==================================================

email_extractor()


print("\n--- Automation + DSA ---")

queue = TaskQueue()

queue.add_task("Study Python")
queue.add_task("Solve DSA")

queue.show_tasks()

print("Processed:",
      queue.process_task())

queue.show_tasks()


print("\n--- OOP + Project Logic ---")

manager = EmployeeManager()

manager.add_employee(
    Employee(101, "Vikyat", 50000)
)

manager.add_employee(
    Employee(102, "Rahul", 45000)
)

manager.display_all()


frequency_counter("pythonprogramming")


print("\n--- Debugging Old Project ---")

print(calculator(10, 2, "+"))

print(calculator(10, 0, "/"))