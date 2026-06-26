# 🔹 DAY 26 - CODE QUALITY CHALLENGE


# ==========================================
# 🔹 UTILITY CLASS
# ==========================================

class Utility:

    @staticmethod
    def header(title):

        print("\n" + "=" * 50)

        print(title)

        print("=" * 50)


# ==========================================
# 🔹 1. CODE CLEANUP CHALLENGE
# ==========================================

def even_numbers(numbers):
    """
    Returns all even numbers from the list.
    """

    return [number for number in numbers if number % 2 == 0]


def cleanup_demo():

    Utility.header("CODE CLEANUP")

    numbers = [10, 15, 22, 31, 48, 57, 60]

    print("Original List:")

    print(numbers)

    print("\nEven Numbers:")

    print(even_numbers(numbers))


# ==========================================
# 🔹 2. READABILITY CHALLENGE
# ==========================================

def readability_demo():

    Utility.header("READABILITY")

    student_name = "Vikyath"

    student_marks = 95

    student_grade = "A+"

    print("Student Name :", student_name)

    print("Marks        :", student_marks)

    print("Grade        :", student_grade)


# ==========================================
# 🔹 3. FUNCTION OPTIMIZATION
# ==========================================

def calculate_area(shape, length, width=0):
    """
    Calculates area of square or rectangle.
    """

    if shape.lower() == "square":

        return length * length

    elif shape.lower() == "rectangle":

        return length * width

    return 0


def function_demo():

    Utility.header("FUNCTION OPTIMIZATION")

    print(
        "Square Area :",
        calculate_area("square", 5)
    )

    print(
        "Rectangle Area :",
        calculate_area(
            "rectangle",
            5,
            10
        )
    )


# ==========================================
# 🔹 4. MODULARIZATION CHALLENGE
# ==========================================

def addition(a, b):

    return a + b


def subtraction(a, b):

    return a - b


def multiplication(a, b):

    return a * b


def division(a, b):

    if b == 0:

        return "Division By Zero"

    return a / b


def calculator():

    Utility.header("MODULAR CALCULATOR")

    first = float(input("First Number : "))

    second = float(input("Second Number : "))

    print("Addition :", addition(first, second))

    print("Subtraction :", subtraction(first, second))

    print("Multiplication :", multiplication(first, second))

    print("Division :", division(first, second))


# ==========================================
# 🔹 5. DOCUMENTATION CHALLENGE
# ==========================================

def factorial(number):
    """
    Returns factorial of a number.

    Parameter:
        number (int)

    Returns:
        int
    """

    result = 1

    for value in range(1, number + 1):

        result *= value

    return result


def documentation_demo():

    Utility.header("DOCUMENTATION")

    number = int(input("Enter Number : "))

    print("Factorial :", factorial(number))


# ==========================================
# 🔹 MAIN PROGRAM
# ==========================================

while True:

    Utility.header("DAY 26 CODE QUALITY")

    print("1. Code Cleanup Challenge")

    print("2. Readability Challenge")

    print("3. Function Optimization")

    print("4. Modularization Challenge")

    print("5. Documentation Challenge")

    print("6. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":

        cleanup_demo()

    elif choice == "2":

        readability_demo()

    elif choice == "3":

        function_demo()

    elif choice == "4":

        calculator()

    elif choice == "5":

        documentation_demo()

    elif choice == "6":

        print("\nGoodbye 👋")

        break

    else:

        print("\n❌ Invalid Choice")