
from __future__ import annotations


def read_integer_list(prompt: str = "Enter integers separated by spaces: ") -> list[int]:
    """Read a list of integers from the user."""
    while True:
        try:
            values = input(prompt).strip()
            if not values:
                return []
            return [int(value) for value in values.split()]
        except ValueError:
            print("Invalid input. Please enter integers only.")


# Program 106: Two Sum in a Sorted Array
def two_sum_sorted(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Return the 0-based indices of two numbers that add up to target."""
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return left, right
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return None


def program_106() -> None:
    print("\n--- Program 106: Two Sum in Sorted Array ---")
    print("Enter numbers in sorted (ascending) order.")
    numbers = read_integer_list()
    target = int(input("Enter target sum: "))

    result = two_sum_sorted(numbers, target)

    if result is None:
        print("No pair adds up to the target.")
    else:
        left, right = result
        print(f"Pair: {numbers[left]} + {numbers[right]} = {target}")
        print(f"0-based indices: {left}, {right}")


# Program 107: Remove Duplicates Using Two Pointers
def remove_duplicates(numbers: list[int]) -> list[int]:
    """Remove duplicates from a sorted list in place and return unique values."""
    if not numbers:
        return []

    write = 0

    for read in range(1, len(numbers)):
        if numbers[read] != numbers[write]:
            write += 1
            numbers[write] = numbers[read]

    return numbers[:write + 1]


def program_107() -> None:
    print("\n--- Program 107: Remove Duplicates ---")
    print("Enter numbers in sorted (ascending) order.")
    numbers = read_integer_list()

    unique_numbers = remove_duplicates(numbers)
    print("List after removing duplicates:", unique_numbers)


# Program 108: Move Zeroes Using Two Pointers
def move_zeroes(numbers: list[int]) -> list[int]:
    """Move zeroes to the end while preserving the order of non-zero values."""
    write = 0

    for read in range(len(numbers)):
        if numbers[read] != 0:
            numbers[write], numbers[read] = numbers[read], numbers[write]
            write += 1

    return numbers


def program_108() -> None:
    print("\n--- Program 108: Move Zeroes ---")
    numbers = read_integer_list()

    print("After moving zeroes to the end:", move_zeroes(numbers))


# Program 109: Reverse a String Using Two Pointers
def reverse_string(value: str) -> str:
    """Reverse a string using two pointers."""
    characters = list(value)
    left = 0
    right = len(characters) - 1

    while left < right:
        characters[left], characters[right] = (
            characters[right],
            characters[left],
        )
        left += 1
        right -= 1

    return "".join(characters)


def program_109() -> None:
    print("\n--- Program 109: Reverse String ---")
    value = input("Enter a string: ")
    print("Reversed string:", reverse_string(value))


# Program 110: Check Palindrome Using Two Pointers
def is_palindrome(value: str) -> bool:
    """Check whether a string is a palindrome, ignoring case and non-alphanumeric characters."""
    characters = [
        character.lower()
        for character in value
        if character.isalnum()
    ]

    left = 0
    right = len(characters) - 1

    while left < right:
        if characters[left] != characters[right]:
            return False
        left += 1
        right -= 1

    return True


def program_110() -> None:
    print("\n--- Program 110: Check Palindrome ---")
    value = input("Enter a string: ")

    if is_palindrome(value):
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")


def run_all() -> None:
    """Run all five programs in sequence."""
    program_106()
    program_107()
    program_108()
    program_109()
    program_110()


def main() -> None:
    while True:
        print("\n========== DAY 22: TWO POINTERS ==========")
        print("106. Two Sum in Sorted Array")
        print("107. Remove Duplicates")
        print("108. Move Zeroes")
        print("109. Reverse String")
        print("110. Check Palindrome")
        print("111. Run All Programs")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "106":
            program_106()
        elif choice == "107":
            program_107()
        elif choice == "108":
            program_108()
        elif choice == "109":
            program_109()
        elif choice == "110":
            program_110()
        elif choice == "111":
            run_all()
        elif choice == "0":
            print("Exiting Day 22 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 106–111 or 0.")


if __name__ == "__main__":
    main()
