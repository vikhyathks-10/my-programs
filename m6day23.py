# 🔹 DAY 23 - CODE REFACTORING PRACTICE


# ==========================================
# 🔹 1. Convert Loops To Comprehensions
# ==========================================

def square_numbers():

    numbers = [1, 2, 3, 4, 5]

    squares = [number ** 2 for number in numbers]

    print("\nSquares:")
    print(squares)


# ==========================================
# 🔹 2. Reduce Nested Loops
# ==========================================

def common_elements():

    first_list = [1, 2, 3, 4, 5]

    second_list = [4, 5, 6, 7, 8]

    common = list(
        set(first_list)
        &
        set(second_list)
    )

    print("\nCommon Elements:")
    print(common)


# ==========================================
# 🔹 3. Improve Function Reuse
# ==========================================

def calculate_area(shape, value1, value2=0):

    if shape == "square":

        return value1 * value1

    elif shape == "rectangle":

        return value1 * value2

    return 0


def area_demo():

    print("\nSquare Area:")
    print(calculate_area("square", 5))

    print("\nRectangle Area:")
    print(calculate_area("rectangle", 5, 10))


# ==========================================
# 🔹 4. Remove Duplicate Code
# ==========================================

def display_message(message):

    print(message)


def duplicate_code_demo():

    display_message(
        "\nWelcome To Python"
    )

    display_message(
        "Learning Refactoring"
    )


# ==========================================
# 🔹 5. Improve Variable Naming
# ==========================================

def variable_naming_demo():

    student_name = "Vikyath"

    student_marks = 95

    student_grade = "A+"

    print("\nStudent Details")

    print(
        student_name,
        student_marks,
        student_grade
    )


# ==========================================
# 🔹 MAIN PROGRAM
# ==========================================

while True:

    print(
        "\n===== DAY 23 REFACTORING PRACTICE ====="
    )

    print(
        "1. Convert Loops To Comprehensions"
    )

    print(
        "2. Reduce Nested Loops"
    )

    print(
        "3. Improve Function Reuse"
    )

    print(
        "4. Remove Duplicate Code"
    )

    print(
        "5. Improve Variable Naming"
    )

    print("6. Exit")

    choice = input(
        "\nEnter Choice: "
    )

    if choice == "1":

        square_numbers()

    elif choice == "2":

        common_elements()

    elif choice == "3":

        area_demo()

    elif choice == "4":

        duplicate_code_demo()

    elif choice == "5":

        variable_naming_demo()

    elif choice == "6":

        print(
            "\nGoodbye 👋"
        )

        break

    else:

        print(
            "\n❌ Invalid Choice"
        )