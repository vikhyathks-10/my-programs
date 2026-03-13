# m3day13.py

# -------- Calculator Module --------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


# -------- Grade Evaluation Module --------
def evaluate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"


# -------- Interest Calculator Module --------
def simple_interest(p, r, t):
    return (p * r * t) / 100

def compound_interest(p, r, t):
    amount = p * (1 + r/100) ** t
    return amount - p


# -------- String Utility Module --------
def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

def to_upper(text):
    return text.upper()


# -------- Main Program --------
while True:

    print("\n------ MODULE PROGRAM ------")
    print("1 Calculator")
    print("2 Grade Evaluation")
    print("3 Interest Calculator")
    print("4 String Utilities")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        a = float(input("Enter number 1: "))
        b = float(input("Enter number 2: "))

        print("Add:", add(a, b))
        print("Subtract:", subtract(a, b))
        print("Multiply:", multiply(a, b))
        print("Divide:", divide(a, b))

    elif choice == "2":
        marks = int(input("Enter marks: "))
        print("Grade:", evaluate_grade(marks))

    elif choice == "3":
        p = float(input("Enter principal: "))
        r = float(input("Enter rate: "))
        t = float(input("Enter time: "))

        print("Simple Interest:", simple_interest(p, r, t))
        print("Compound Interest:", compound_interest(p, r, t))

    elif choice == "4":
        text = input("Enter a string: ")

        print("Reversed:", reverse_string(text))
        print("Vowel Count:", count_vowels(text))
        print("Uppercase:", to_upper(text))

    elif choice == "5":
        break

    else:
        print("Invalid choice")