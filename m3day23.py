# -------- Simulating Package: utils --------

# ---- Module 1: calculator ----
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


# ---- Module 2: string_utils ----
def reverse(text):
    return text[::-1]

def to_upper(text):
    return text.upper()


# -------- Nested Module Call (Simulation) --------
def process_text_and_calculate(text, a, b):
    # using functions from both "modules"
    rev = reverse(text)
    result = add(a, b)
    return rev, result


# -------- Main Program --------
while True:

    print("\n------ PACKAGE PRACTICE PROGRAM ------")
    print("1 Use calculator module")
    print("2 Use string module")
    print("3 Nested module call")
    print("4 Mini package demo")
    print("5 Exit")

    choice = input("Enter choice: ")

    # 1 Use calculator module
    if choice == "1":
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))

        print("Addition:", add(a, b))
        print("Multiplication:", multiply(a, b))

    # 2 Use string module
    elif choice == "2":
        text = input("Enter text: ")

        print("Reversed:", reverse(text))
        print("Uppercase:", to_upper(text))

    # 3 Nested module call
    elif choice == "3":
        text = input("Enter text: ")
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))

        rev, result = process_text_and_calculate(text, a, b)
        print("Reversed Text:", rev)
        print("Addition Result:", result)

    # 4 Mini package demo program
    elif choice == "4":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        grade = "A" if marks >= 90 else "B" if marks >= 75 else "C" if marks >= 60 else "Fail"

        print("\n--- Student Report ---")
        print("Name:", to_upper(name))   # using string module
        print("Marks:", marks)
        print("Grade:", grade)

    # Exit
    elif choice == "5":
        break

    else:
        print("Invalid choice")