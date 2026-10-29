
from __future__ import annotations


def read_integer(prompt: str) -> int:
    """Read an integer safely."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


# Program 141: Reverse a String Recursively
def reverse_string_recursive(value: str) -> str:
    """Reverse a string by recursively reversing the remaining substring."""
    if len(value) <= 1:
        return value

    return reverse_string_recursive(value[1:]) + value[0]


def program_141() -> None:
    print("\n--- Program 141: Reverse a String Recursively ---")
    value = input("Enter a string: ")

    print("Reversed string:", reverse_string_recursive(value))


# Program 142: Check Palindrome Recursively
def is_palindrome_recursive(value: str) -> bool:
    """Check whether a string is a palindrome, ignoring case and punctuation."""
    characters = "".join(
        character.lower()
        for character in value
        if character.isalnum()
    )

    def check(left: int, right: int) -> bool:
        if left >= right:
            return True

        if characters[left] != characters[right]:
            return False

        return check(left + 1, right - 1)

    return check(0, len(characters) - 1)


def program_142() -> None:
    print("\n--- Program 142: Check Palindrome Recursively ---")
    value = input("Enter a string: ")

    if is_palindrome_recursive(value):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


# Program 143: Find a Fibonacci Number
def fibonacci_recursive(n: int) -> int:
    """Return the nth Fibonacci number using basic recursion."""
    if n < 0:
        raise ValueError("n must be non-negative.")

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def program_143() -> None:
    print("\n--- Program 143: Find Fibonacci Number ---")

    while True:
        n = read_integer("Enter n (0 or greater): ")

        if n >= 0:
            break

        print("Please enter a non-negative integer.")

    print(f"Fibonacci number F({n}) =", fibonacci_recursive(n))


# Program 144: Find GCD Recursively
def gcd_recursive(first: int, second: int) -> int:
    """Find the greatest common divisor using Euclid's algorithm."""
    first = abs(first)
    second = abs(second)

    if second == 0:
        return first

    return gcd_recursive(second, first % second)


def program_144() -> None:
    print("\n--- Program 144: Find GCD Recursively ---")
    first = read_integer("Enter the first integer: ")
    second = read_integer("Enter the second integer: ")

    print("GCD:", gcd_recursive(first, second))


# Program 145: Count Digits Recursively
def count_digits_recursive(number: int) -> int:
    """Count decimal digits recursively; zero has one digit."""
    number = abs(number)

    if number < 10:
        return 1

    return 1 + count_digits_recursive(number // 10)


def program_145() -> None:
    print("\n--- Program 145: Count Digits Recursively ---")
    number = read_integer("Enter an integer: ")

    print("Number of digits:", count_digits_recursive(number))


def run_all() -> None:
    program_141()
    program_142()
    program_143()
    program_144()
    program_145()


def main() -> None:
    while True:
        print("\n========== DAY 29: RECURSION PROBLEMS ==========")
        print("141. Reverse a String Recursively")
        print("142. Check Palindrome Recursively")
        print("143. Find Fibonacci Number")
        print("144. Find GCD Recursively")
        print("145. Count Digits Recursively")
        print("146. Run All Programs")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "141":
            program_141()
        elif choice == "142":
            program_142()
        elif choice == "143":
            program_143()
        elif choice == "144":
            program_144()
        elif choice == "145":
            program_145()
        elif choice == "146":
            run_all()
        elif choice == "0":
            print("Exiting Day 29 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 141–146 or 0.")


if __name__ == "__main__":
    main()
