"""
MONTH 11 - DAY 5
DIVIDE AND CONQUER FUNDAMENTALS

Programs:
21. Recursive Binary Search
22. Merge Sort
23. Quick Sort
24. Maximum Subarray Sum using Divide and Conquer
25. Majority Element using Divide and Conquer

Menu:
21-25: Run individual programs
26: Run all programs
0: Exit
"""

from typing import Optional


# ---------------------------------------------------------
# PROGRAM 21: RECURSIVE BINARY SEARCH
# ---------------------------------------------------------

def binary_search(
    arr: list[int],
    target: int,
    low: int,
    high: int
) -> int:
    """Return the index of target, or -1 if it is not present."""

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    if target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)

    return binary_search(arr, target, mid + 1, high)


def program_21() -> None:
    print("\nPROGRAM 21: RECURSIVE BINARY SEARCH")

    arr = [3, 7, 11, 15, 19, 23, 27, 31]
    target = 23

    print("Sorted array:", arr)
    print("Target:", target)

    result = binary_search(arr, target, 0, len(arr) - 1)

    if result != -1:
        print(f"Element found at index {result}.")
    else:
        print("Element not found.")


# ---------------------------------------------------------
# PROGRAM 22: MERGE SORT
# ---------------------------------------------------------

def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list."""

    result: list[int] = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr: list[int]) -> list[int]:
    """Sort a list using the merge sort algorithm."""

    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def program_22() -> None:
    print("\nPROGRAM 22: MERGE SORT")

    arr = [38, 12, 27, 43, 9, 31, 18, 25]

    print("Original array:", arr)

    sorted_arr = merge_sort(arr)

    print("Sorted array:", sorted_arr)


# ---------------------------------------------------------
# PROGRAM 23: QUICK SORT
# ---------------------------------------------------------

def partition(arr: list[int], low: int, high: int) -> int:
    """Partition the array using the last element as pivot."""

    pivot = arr[high]
    smaller_index = low - 1

    for current in range(low, high):
        if arr[current] <= pivot:
            smaller_index += 1
            arr[smaller_index], arr[current] = (
                arr[current],
                arr[smaller_index]
            )

    arr[smaller_index + 1], arr[high] = (
        arr[high],
        arr[smaller_index + 1]
    )

    return smaller_index + 1


def quick_sort(arr: list[int], low: int, high: int) -> None:
    """Sort the array in place using quick sort."""

    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def program_23() -> None:
    print("\nPROGRAM 23: QUICK SORT")

    arr = [29, 10, 14, 37, 13, 5, 22]

    print("Original array:", arr)

    quick_sort(arr, 0, len(arr) - 1)

    print("Sorted array:", arr)


# ---------------------------------------------------------
# PROGRAM 24: MAXIMUM SUBARRAY SUM
# USING DIVIDE AND CONQUER
# ---------------------------------------------------------

def max_crossing_sum(
    arr: list[int],
    low: int,
    mid: int,
    high: int
) -> int:
    """Find the maximum subarray sum crossing the midpoint."""

    left_sum = float("-inf")
    current_sum = 0

    for i in range(mid, low - 1, -1):
        current_sum += arr[i]
        left_sum = max(left_sum, current_sum)

    right_sum = float("-inf")
    current_sum = 0

    for i in range(mid + 1, high + 1):
        current_sum += arr[i]
        right_sum = max(right_sum, current_sum)

    return int(left_sum + right_sum)


def max_subarray_sum(arr: list[int], low: int, high: int) -> int:
    """Return the maximum contiguous subarray sum."""

    if low == high:
        return arr[low]

    mid = (low + high) // 2

    left_max = max_subarray_sum(arr, low, mid)
    right_max = max_subarray_sum(arr, mid + 1, high)
    crossing_max = max_crossing_sum(arr, low, mid, high)

    return max(left_max, right_max, crossing_max)


def program_24() -> None:
    print("\nPROGRAM 24: MAXIMUM SUBARRAY SUM")

    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    print("Array:", arr)

    result = max_subarray_sum(arr, 0, len(arr) - 1)

    print("Maximum subarray sum:", result)


# ---------------------------------------------------------
# PROGRAM 25: MAJORITY ELEMENT
# USING DIVIDE AND CONQUER
# ---------------------------------------------------------

def majority_candidate(
    arr: list[int],
    low: int,
    high: int
) -> Optional[int]:
    """Find a possible majority candidate recursively."""

    if low == high:
        return arr[low]

    mid = (low + high) // 2

    left_candidate = majority_candidate(arr, low, mid)
    right_candidate = majority_candidate(arr, mid + 1, high)

    if left_candidate == right_candidate:
        return left_candidate

    left_count = 0
    right_count = 0

    for i in range(low, high + 1):
        if arr[i] == left_candidate:
            left_count += 1

        if arr[i] == right_candidate:
            right_count += 1

    if left_count > right_count:
        return left_candidate

    if right_count > left_count:
        return right_candidate

    return None


def majority_element(arr: list[int]) -> Optional[int]:
    """Return the majority element if one exists."""

    if not arr:
        return None

    candidate = majority_candidate(arr, 0, len(arr) - 1)

    if candidate is None:
        return None

    if arr.count(candidate) > len(arr) // 2:
        return candidate

    return None


def program_25() -> None:
    print("\nPROGRAM 25: MAJORITY ELEMENT")

    arr = [2, 2, 1, 1, 2, 2, 2]

    print("Array:", arr)

    result = majority_element(arr)

    if result is not None:
        print("Majority element:", result)
    else:
        print("No majority element exists.")


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main() -> None:
    while True:
        print("\n========================================")
        print(" MONTH 11 - DAY 5: DIVIDE AND CONQUER")
        print("========================================")
        print("21. Recursive Binary Search")
        print("22. Merge Sort")
        print("23. Quick Sort")
        print("24. Maximum Subarray Sum")
        print("25. Majority Element")
        print("26. Run All Programs")
        print("0. Exit")
        print("========================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 21:
            program_21()
        elif choice == 22:
            program_22()
        elif choice == 23:
            program_23()
        elif choice == 24:
            program_24()
        elif choice == 25:
            program_25()
        elif choice == 26:
            for program in (
                program_21,
                program_22,
                program_23,
                program_24,
                program_25
            ):
                program()
        elif choice == 0:
            print("Exiting Day 5 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 0 or 21-26.")


if __name__ == "__main__":
    main()