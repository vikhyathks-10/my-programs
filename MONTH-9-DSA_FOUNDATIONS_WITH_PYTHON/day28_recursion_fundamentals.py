# DAY 28 - RECURSION FUNDAMENTALS
# Programs 136 - 140


# ---------------------------------------------------------
# 136. Print Numbers From 1 to N Recursively
# ---------------------------------------------------------
def print_1_to_n(n):
    if n <= 0:
        return

    print_1_to_n(n - 1)
    print(n)


def program_136():
    n = int(input("Enter N: "))

    print("Numbers from 1 to N:")
    print_1_to_n(n)

    print("Complexity: O(N) time, O(N) recursion stack")


# ---------------------------------------------------------
# 137. Print Numbers From N to 1 Recursively
# ---------------------------------------------------------
def print_n_to_1(n):
    if n <= 0:
        return

    print(n)
    print_n_to_1(n - 1)


def program_137():
    n = int(input("Enter N: "))

    print("Numbers from N to 1:")
    print_n_to_1(n)

    print("Complexity: O(N) time, O(N) recursion stack")


# ---------------------------------------------------------
# 138. Calculate Factorial
# ---------------------------------------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def program_138():
    n = int(input("Enter a non-negative integer: "))

    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return

    result = factorial(n)

    print("Factorial:", result)
    print("Complexity: O(N) time, O(N) recursion stack")


# ---------------------------------------------------------
# 139. Calculate Power Recursively
# ---------------------------------------------------------
def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


def program_139():
    base = int(input("Enter base: "))
    exponent = int(input("Enter non-negative exponent: "))

    if exponent < 0:
        print("This program accepts only non-negative exponents.")
        return

    result = power(base, exponent)

    print("Result:", result)
    print("Complexity: O(N) time, O(N) recursion stack")


# ---------------------------------------------------------
# 140. Calculate Sum of Digits Recursively
# ---------------------------------------------------------
def sum_of_digits(n):
    n = abs(n)

    if n == 0:
        return 0

    return (n % 10) + sum_of_digits(n // 10)


def program_140():
    n = int(input("Enter an integer: "))

    result = sum_of_digits(n)

    print("Sum of digits:", result)
    print("Complexity: O(D) time, O(D) recursion stack")


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main():

    while True:

        print("\n==========================================")
        print("     DAY 28 - RECURSION FUNDAMENTALS")
        print("==========================================")
        print("136. Print numbers from 1 to N recursively")
        print("137. Print N to 1 recursively")
        print("138. Calculate factorial")
        print("139. Calculate power recursively")
        print("140. Calculate sum of digits recursively")
        print("141. Run All Programs")
        print("142. Exit")
        print("==========================================")

        choice = int(input("Enter your choice: "))

        if choice == 136:
            program_136()

        elif choice == 137:
            program_137()

        elif choice == 138:
            program_138()

        elif choice == 139:
            program_139()

        elif choice == 140:
            program_140()

        elif choice == 141:
            print("\nRunning all Day 28 programs...\n")

            program_136()
            program_137()
            program_138()
            program_139()
            program_140()

        elif choice == 142:
            print("Exiting Day 28. 🔥")
            break

        else:
            print("Invalid choice. Please try again.")


# Program starts here
if __name__ == "__main__":
    main()