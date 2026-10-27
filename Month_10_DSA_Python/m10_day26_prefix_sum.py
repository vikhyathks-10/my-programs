
from __future__ import annotations


def read_integer_list(prompt: str) -> list[int]:
    """Read a space-separated list of integers."""
    while True:
        try:
            text = input(prompt).strip()
            if not text:
                return []
            return [int(item) for item in text.split()]
        except ValueError:
            print("Invalid input. Please enter integers only.")


def read_integer(prompt: str) -> int:
    """Read one integer safely."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def read_index(prompt: str, minimum: int, maximum: int) -> int:
    """Read an integer within the specified range."""
    while True:
        value = read_integer(prompt)
        if minimum <= value <= maximum:
            return value
        print(f"Please enter a value from {minimum} to {maximum}.")


# Program 126: Build a Prefix-Sum Array
def build_prefix_sum(numbers: list[int]) -> list[int]:
    """Return cumulative sums for every position."""
    prefix: list[int] = []
    running_sum = 0

    for number in numbers:
        running_sum += number
        prefix.append(running_sum)

    return prefix


def program_126() -> None:
    print("\n--- Program 126: Build Prefix-Sum Array ---")
    numbers = read_integer_list("Enter array elements: ")

    prefix = build_prefix_sum(numbers)

    print("Original array:", numbers)
    print("Prefix-sum array:", prefix)


# Program 127: Range-Sum Queries
def build_prefix_with_zero(numbers: list[int]) -> list[int]:
    """Build prefix sums with a leading zero for easier range queries."""
    prefix = [0]

    for number in numbers:
        prefix.append(prefix[-1] + number)

    return prefix


def range_sum(prefix: list[int], left: int, right: int) -> int:
    """Return the inclusive sum from left to right using 0-based indices."""
    return prefix[right + 1] - prefix[left]


def program_127() -> None:
    print("\n--- Program 127: Range-Sum Queries ---")
    numbers = read_integer_list("Enter array elements: ")

    if not numbers:
        print("The array is empty.")
        return

    prefix = build_prefix_with_zero(numbers)
    print("Array:", numbers)
    print("Enter inclusive 0-based index ranges.")

    query_count = read_index("How many queries? ", 1, 100000)

    for query_number in range(1, query_count + 1):
        print(f"Query {query_number}:")
        left = read_index("  Left index: ", 0, len(numbers) - 1)
        right = read_index("  Right index: ", 0, len(numbers) - 1)

        if left > right:
            print("  Left index must not exceed right index.")
            continue

        print("  Range sum:", range_sum(prefix, left, right))


# Program 128: Find a Subarray with a Given Sum
def find_subarray_with_sum(
    numbers: list[int], target: int
) -> tuple[int, int] | None:
    """
    Return inclusive 0-based start and end indices of a matching
    non-empty subarray, or None if no such subarray exists.
    Supports positive, zero, and negative values.
    """
    first_index: dict[int, int] = {0: -1}
    running_sum = 0

    for index, number in enumerate(numbers):
        running_sum += number
        needed = running_sum - target

        if needed in first_index:
            return first_index[needed] + 1, index

        if running_sum not in first_index:
            first_index[running_sum] = index

    return None


def program_128() -> None:
    print("\n--- Program 128: Find Subarray with Given Sum ---")
    numbers = read_integer_list("Enter array elements: ")
    target = read_integer("Enter target sum: ")

    result = find_subarray_with_sum(numbers, target)

    if result is None:
        print("No subarray with the target sum was found.")
    else:
        start, end = result
        print(f"Subarray found at indices {start} to {end}.")
        print("Subarray:", numbers[start:end + 1])
        print("Subarray sum:", sum(numbers[start:end + 1]))


# Program 129: Count Subarrays with Sum K
def count_subarrays_with_sum(numbers: list[int], target: int) -> int:
    """Count all non-empty subarrays whose sum equals target."""
    prefix_frequency: dict[int, int] = {0: 1}
    running_sum = 0
    count = 0

    for number in numbers:
        running_sum += number
        needed = running_sum - target

        count += prefix_frequency.get(needed, 0)
        prefix_frequency[running_sum] = (
            prefix_frequency.get(running_sum, 0) + 1
        )

    return count


def program_129() -> None:
    print("\n--- Program 129: Count Subarrays with Sum K ---")
    numbers = read_integer_list("Enter array elements: ")
    target = read_integer("Enter target sum K: ")

    result = count_subarrays_with_sum(numbers, target)

    print(f"Number of subarrays with sum {target}:", result)


# Program 130: Find Equilibrium Index Using Prefix Sums
def equilibrium_indices(numbers: list[int]) -> list[int]:
    """
    Return all 0-based indices where the sum to the left equals
    the sum to the right. The current element is excluded.
    """
    total_sum = sum(numbers)
    left_sum = 0
    result: list[int] = []

    for index, number in enumerate(numbers):
        right_sum = total_sum - left_sum - number

        if left_sum == right_sum:
            result.append(index)

        left_sum += number

    return result


def program_130() -> None:
    print("\n--- Program 130: Equilibrium Index ---")
    numbers = read_integer_list("Enter array elements: ")

    result = equilibrium_indices(numbers)

    if result:
        print("Equilibrium index/indices (0-based):", result)
    else:
        print("No equilibrium index exists.")


def run_all() -> None:
    program_126()
    program_127()
    program_128()
    program_129()
    program_130()


def main() -> None:
    while True:
        print("\n========== DAY 26: PREFIX SUM ==========")
        print("126. Build Prefix-Sum Array")
        print("127. Range-Sum Queries")
        print("128. Find Subarray with Given Sum")
        print("129. Count Subarrays with Sum K")
        print("130. Find Equilibrium Index")
        print("131. Run All Programs")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "126":
            program_126()
        elif choice == "127":
            program_127()
        elif choice == "128":
            program_128()
        elif choice == "129":
            program_129()
        elif choice == "130":
            program_130()
        elif choice == "131":
            run_all()
        elif choice == "0":
            print("Exiting Day 26 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 126–131 or 0.")


if __name__ == "__main__":
    main()
