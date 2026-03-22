# -------- Calculator Module --------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"


# -------- Validation Module --------
def validate_age(age):
    if age < 0 or age > 120:
        return "Invalid age"
    return "Valid age"

def validate_email(email):
    if "@" in email and "." in email:
        return "Valid email"
    return "Invalid email"


# -------- String Module --------
def reverse(text):
    return text[::-1]

def to_upper(text):
    return text.upper()

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for c in text if c in vowels)


# -------- Main Program --------
while True:

    print("\n------ MODULE PRACTICE PROGRAM ------")
    print("1 Calculator (alias concept)")
    print("2 Validation (from * concept)")
    print("3 String Utilities")
    print("4 Exit")

    choice = input("Enter choice: ")

    # 1 Alias concept (simulated)
    if choice == "1":
        print("\nCalculator (alias simulation)")
        a = float(input("Enter number 1: "))
        b = float(input("Enter number 2: "))

        print("Add:", add(a, b))
        print("Subtract:", subtract(a, b))
        print("Multiply:", multiply(a, b))
        print("Divide:", divide(a, b))

    # 2 from module import * concept
    elif choice == "2":
        age = int(input("Enter age: "))
        email = input("Enter email: ")

        print(validate_age(age))
        print(validate_email(email))

    # 3 String module
    elif choice == "3":
        text = input("Enter text: ")

        print("Reversed:", reverse(text))
        print("Uppercase:", to_upper(text))
        print("Vowel count:", count_vowels(text))

    # Exit
    elif choice == "4":
        break

    else:
        print("Invalid choice")