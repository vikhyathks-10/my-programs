# -------- Simulating calculator module --------
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


# -------- Simulating string module --------
def reverse(text):
    return text[::-1]

def upper(text):
    return text.upper()


# -------- Simulating interest module --------
def simple_interest(p, r, t):
    return (p * r * t) / 100


# -------- Main Program --------
while True:

    print("\n------ MODULE PRACTICE PROGRAM ------")
    print("1 Import module using alias (calculator)")
    print("2 Use from module import * (string utilities)")
    print("3 Interest calculator (package example)")
    print("4 Mini Project (Student Utility)")
    print("5 Exit")

    choice = input("Enter choice: ")

    # 1 Alias example
    if choice == "1":
        print("\nCalculator using alias concept")
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("Addition:", add(a, b))
        print("Multiplication:", multiply(a, b))

    # 2 from module import *
    elif choice == "2":
        text = input("Enter text: ")

        print("Reversed:", reverse(text))
        print("Uppercase:", upper(text))

    # 3 Interest module
    elif choice == "3":
        p = float(input("Principal: "))
        r = float(input("Rate: "))
        t = float(input("Time: "))

        print("Simple Interest:", simple_interest(p, r, t))

    # 4 Mini project
    elif choice == "4":

        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        else:
            grade = "Fail"

        print("\nStudent Report")
        print("Name:", upper(name))
        print("Marks:", marks)
        print("Grade:", grade)

    elif choice == "5":
        break

    else:
        print("Invalid choice")