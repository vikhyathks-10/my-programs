# 🔹 DAY 19 - DATA AUTOMATION

import csv


# 🔹 1. CSV Writer

def csv_writer():

    print("\n--- CSV Writer ---")

    data = [
        ["Name", "Marks"],
        ["Vikyat", 85],
        ["Rahul", 78],
        ["Anil", 92]
    ]

    with open("students.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(data)

    print("CSV File Created")


# 🔹 2. CSV Reader

def csv_reader():

    print("\n--- CSV Reader ---")

    with open("students.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:
            print(row)


# 🔹 3. Student Marks Analyzer

def marks_analyzer():

    print("\n--- Student Marks Analyzer ---")

    marks = []

    with open("students.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)  # skip header

        for row in reader:
            marks.append(int(row[1]))

    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))
    print("Average Marks:",
          round(sum(marks) / len(marks), 2))


# 🔹 4. Expense Tracker

def expense_tracker():

    print("\n--- Expense Tracker ---")

    expenses = [
        ["Food", 250],
        ["Travel", 100],
        ["Shopping", 500]
    ]

    with open("expenses.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Category", "Amount"])

        writer.writerows(expenses)

    total = sum(expense[1] for expense in expenses)

    print("Total Expense:", total)


# 🔹 5. Attendance System

def attendance_system():

    print("\n--- Attendance System ---")

    attendance = [
        ["Vikyat", "Present"],
        ["Rahul", "Absent"],
        ["Anil", "Present"]
    ]

    with open("attendance.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Name", "Status"])

        writer.writerows(attendance)

    print("Attendance Saved")


# 🔹 MAIN PROGRAM

csv_writer()

csv_reader()

marks_analyzer()

expense_tracker()

attendance_system()