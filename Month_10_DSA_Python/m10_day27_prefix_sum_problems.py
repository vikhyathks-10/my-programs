
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


# Program 131: Maximum Subarray Sum Using Prefix Concepts
def maximum_subarray_sum(numbers: list[int]) -> tuple[int, int, int] | None:
    """
    Return (maximum_sum, start_index, end_index).
    Uses a running prefix sum and the minimum prefix seen so far.
    """
    if not numbers:
        return None

    prefix_sum = 0
    minimum_prefix = 0
    minimum_prefix_index = -1

    best_sum: int | None = None
    best_start = 0
    best_end = 0

    for index, number in enumerate(numbers):
        prefix_sum += number
        current_sum = prefix_sum - minimum_prefix

        if best_sum is None or current_sum > best_sum:
            best_sum = current_sum
            best_start = minimum_prefix_index + 1
            best_end = index

        if prefix_sum < minimum_prefix:
            minimum_prefix = prefix_sum
            minimum_prefix_index = index

    if best_sum is None:
        return None

    return best_sum, best_start, best_end


def program_131() -> None:
    print("\n--- Program 131: Maximum Subarray Sum ---")
    numbers = read_integer_list("Enter array elements: ")
    result = maximum_subarray_sum(numbers)

    if result is None:
        print("The array is empty.")
        return

    total, start, end = result
    print("Maximum subarray sum:", total)
    print(f"Subarray indices: {start} to {end}")
    print("Subarray:", numbers[start:end + 1])


# Program 132: Minimum Subarray Sum
def minimum_subarray_sum(numbers: list[int]) -> tuple[int, int, int] | None:
    """
    Return (minimum_sum, start_index, end_index).
    Uses a running prefix sum and the maximum prefix seen so far.
    """
    if not numbers:
        return None

    prefix_sum = 0
    maximum_prefix = 0
    maximum_prefix_index = -1

    best_sum: int | None = None
    best_start = 0
    best_end = 0

    for index, number in enumerate(numbers):
        prefix_sum += number
        current_sum = prefix_sum - maximum_prefix

        if best_sum is None or current_sum < best_sum:
            best_sum = current_sum
            best_start = maximum_prefix_index + 1
            best_end = index

        if prefix_sum > maximum_prefix:
            maximum_prefix = prefix_sum
            maximum_prefix_index = index

    if best_sum is None:
        return None

    return best_sum, best_start, best_end


def program_132() -> None:
    print("\n--- Program 132: Minimum Subarray Sum ---")
    numbers = read_integer_list("Enter array elements: ")
    result = minimum_subarray_sum(numbers)

    if result is None:
        print("The array is empty.")
        return

    total, start, end = result
    print("Minimum subarray sum:", total)
    print(f"Subarray indices: {start} to {end}")
    print("Subarray:", numbers[start:end + 1])


# Program 133: Find the Longest Subarray with Sum K
def longest_subarray_with_sum(
    numbers: list[int], target: int
) -> tuple[int, int, int] | None:
    """
    Return (length, start_index, end_index) for a longest subarray
    with sum target. Supports positive, zero, and negative values.
    """
    first_prefix_index: dict[int, int] = {0: -1}
    prefix_sum = 0

    best_length = 0
    best_start = 0
    best_end = -1

    for index, number in enumerate(numbers):
        prefix_sum += number
        needed = prefix_sum - target

        if needed in first_prefix_index:
            start = first_prefix_index[needed] + 1
            length = index - start + 1

            if length > best_length:
                best_length = length
                best_start = start
                best_end = index

        if prefix_sum not in first_prefix_index:
            first_prefix_index[prefix_sum] = index

    if best_length == 0:
        return None

    return best_length, best_start, best_end


def program_133() -> None:
    print("\n--- Program 133: Longest Subarray with Sum K ---")
    numbers = read_integer_list("Enter array elements: ")
    target = read_integer("Enter target sum K: ")

    result = longest_subarray_with_sum(numbers, target)

    if result is None:
        print("No subarray with the given sum was found.")
        return

    length, start, end = result
    print("Longest subarray length:", length)
    print(f"Subarray indices: {start} to {end}")
    print("Subarray:", numbers[start:end + 1])


# Program 134: Count Zero-Sum Subarrays
def count_zero_sum_subarrays(numbers: list[int]) -> int:
    """Count contiguous subarrays whose sum is zero."""
    prefix_frequency: dict[int, int] = {0: 1}
    prefix_sum = 0
    count = 0

    for number in numbers:
        prefix_sum += number
        count += prefix_frequency.get(prefix_sum, 0)
        prefix_frequency[prefix_sum] = (
            prefix_frequency.get(prefix_sum, 0) + 1
        )

    return count


def program_134() -> None:
    print("\n--- Program 134: Count Zero-Sum Subarrays ---")
    numbers = read_integer_list("Enter array elements: ")

    result = count_zero_sum_subarrays(numbers)
    print("Number of zero-sum subarrays:", result)


# Program 135: Range Update Using a Difference Array
def apply_range_updates(
    numbers: list[int],
    updates: list[tuple[int, int, int]],
) -> list[int]:
    """
    Each update is (left, right, value), using inclusive 0-based indices.
    Add value to every element from left through right.
    """
    size = len(numbers)
    difference = [0] * (size + 1)

    for left, right, value in updates:
        if left < 0 or right >= size or left > right:
            raise ValueError(
                f"Invalid update range: ({left}, {right})"
            )

        difference[left] += value

        if right + 1 < size:
            difference[right + 1] -= value

    result: list[int] = []
    running_update = 0

    for index, number in enumerate(numbers):
        running_update += difference[index]
        result.append(number + running_update)

    return result


def program_135() -> None:
    print("\n--- Program 135: Range Update Using Difference Array ---")
    numbers = read_integer_list("Enter initial array: ")

    if not numbers:
        print("The array is empty.")
        return

    update_count = read_integer("How many range updates? ")

    if update_count < 0:
        print("Number of updates cannot be negative.")
        return

    updates: list[tuple[int, int, int]] = []

    print("Enter each update as: left_index right_index value")
    print("Indices are 0-based, and both endpoints are included.")

    for update_number in range(1, update_count + 1):
        while True:
            try:
                parts = input(f"Update {update_number}: ").split()

                if len(parts) != 3:
                    print("Enter exactly three integers.")
                    continue

                left, right, value = map(int, parts)

                if left < 0 or right >= len(numbers) or left > right:
                    print(
                        f"Invalid range. Indices must be between "
                        f"0 and {len(numbers) - 1}, with left <= right."
                    )
                    continue

                updates.append((left, right, value))
                break

            except ValueError:
                print("Invalid input. Enter three integers.")

    result = apply_range_updates(numbers, updates)

    print("Original array:", numbers)
    print("Array after all updates:", result)


def run_all() -> None:
    program_131()
    program_132()
    program_133()
    program_134()
    program_135()


def main() -> None:
    while True:
        print("\n========== DAY 27: PREFIX SUM PROBLEMS ==========")
        print("131. Maximum Subarray Sum")
        print("132. Minimum Subarray Sum")
        print("133. Longest Subarray with Sum K")
        print("134. Count Zero-Sum Subarrays")
        print("135. Range Update Using Difference Array")
        print("136. Run All Programs")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "131":
            program_131()
        elif choice == "132":
            program_132()
        elif choice == "133":
            program_133()
        elif choice == "134":
            program_134()
        elif choice == "135":
            program_135()
        elif choice == "136":
            run_all()
        elif choice == "0":
            print("Exiting Day 27 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 131–136 or 0.")


if __name__ == "__main__":
    main()
