
from typing import Optional


# ============================================================
# PROGRAM 56: INTEGER SQUARE ROOT
# ============================================================

def integer_square_root(n: int) -> int:
    """
    Find the floor of the square root of n using binary search.

    Example:
    Input:  n = 26
    Output: 5
    """

    if n < 0:
        raise ValueError("Number must be non-negative.")

    left = 0
    right = n
    answer = 0

    while left <= right:
        mid = left + (right - left) // 2

        if mid * mid <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


def run_program_56() -> None:
    print("\n--- PROGRAM 56: INTEGER SQUARE ROOT ---")

    n = int(input("Enter a non-negative integer: "))

    result = integer_square_root(n)

    print("Floor square root:", result)


# ============================================================
# PROGRAM 57: SMALLEST DIVISOR GIVEN A THRESHOLD
# ============================================================

def smallest_divisor(nums: list[int], threshold: int) -> int:
    """
    Find the smallest positive divisor such that the sum of
    ceil(nums[i] / divisor) is <= threshold.

    Example:
    Input:
        nums = [1, 2, 5, 9]
        threshold = 6

    Output: 5
    """

    if not nums:
        raise ValueError("Array cannot be empty.")

    if any(num <= 0 for num in nums):
        raise ValueError("All array elements must be positive.")

    if threshold < len(nums):
        return -1

    left = 1
    right = max(nums)
    answer = right

    while left <= right:
        divisor = left + (right - left) // 2

        total = 0

        for num in nums:
            total += (num + divisor - 1) // divisor

        if total <= threshold:
            answer = divisor
            right = divisor - 1
        else:
            left = divisor + 1

    return answer


def run_program_57() -> None:
    print("\n--- PROGRAM 57: SMALLEST DIVISOR ---")

    nums = list(map(int, input("Enter array elements: ").split()))
    threshold = int(input("Enter threshold: "))

    result = smallest_divisor(nums, threshold)

    print("Smallest valid divisor:", result)


# ============================================================
# PROGRAM 58: CAPACITY TO SHIP PACKAGES WITHIN D DAYS
# ============================================================

def can_ship(weights: list[int], days: int, capacity: int) -> bool:
    """
    Check whether all packages can be shipped within the
    given number of days using the specified capacity.
    Package order must be preserved.
    """

    required_days = 1
    current_load = 0

    for weight in weights:
        if current_load + weight <= capacity:
            current_load += weight
        else:
            required_days += 1
            current_load = weight

    return required_days <= days


def ship_within_days(weights: list[int], days: int) -> int:
    """
    Find the minimum ship capacity required to ship all
    packages within the given number of days.

    Example:
    Input:
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        days = 5

    Output: 15
    """

    if not weights:
        raise ValueError("Weights cannot be empty.")

    if any(weight <= 0 for weight in weights):
        raise ValueError("All package weights must be positive.")

    if days <= 0:
        raise ValueError("Days must be positive.")

    left = max(weights)
    right = sum(weights)
    answer = right

    while left <= right:
        capacity = left + (right - left) // 2

        if can_ship(weights, days, capacity):
            answer = capacity
            right = capacity - 1
        else:
            left = capacity + 1

    return answer


def run_program_58() -> None:
    print("\n--- PROGRAM 58: SHIP PACKAGES WITHIN D DAYS ---")

    weights = list(map(int, input("Enter package weights: ").split()))
    days = int(input("Enter number of days: "))

    result = ship_within_days(weights, days)

    print("Minimum ship capacity:", result)


# ============================================================
# PROGRAM 59: BOOK ALLOCATION PROBLEM
# ============================================================

def can_allocate_books(
    pages: list[int],
    students: int,
    max_pages: int
) -> bool:
    """
    Check whether books can be allocated to students such
    that no student receives more than max_pages.

    Books must be allocated contiguously.
    """

    required_students = 1
    current_pages = 0

    for page_count in pages:
        if current_pages + page_count <= max_pages:
            current_pages += page_count
        else:
            required_students += 1
            current_pages = page_count

    return required_students <= students


def allocate_books(
    pages: list[int],
    students: int
) -> Optional[int]:
    """
    Allocate books among students while minimizing the
    maximum number of pages assigned to one student.

    Every student must receive at least one book.

    Returns None if allocation is impossible.

    Example:
    Input:
        pages = [12, 34, 67, 90]
        students = 2

    Output: 113
    """

    if not pages:
        raise ValueError("Book list cannot be empty.")

    if any(page < 0 for page in pages):
        raise ValueError("Page counts cannot be negative.")

    if students <= 0:
        raise ValueError("Number of students must be positive.")

    if students > len(pages):
        return None

    left = max(pages)
    right = sum(pages)
    answer = right

    while left <= right:
        max_pages = left + (right - left) // 2

        if can_allocate_books(pages, students, max_pages):
            answer = max_pages
            right = max_pages - 1
        else:
            left = max_pages + 1

    return answer


def run_program_59() -> None:
    print("\n--- PROGRAM 59: BOOK ALLOCATION ---")

    pages = list(map(int, input("Enter pages in each book: ").split()))
    students = int(input("Enter number of students: "))

    result = allocate_books(pages, students)

    if result is None:
        print("Allocation is not possible.")
    else:
        print("Minimum possible maximum pages:", result)


# ============================================================
# PROGRAM 60: SPLIT ARRAY LARGEST SUM
# ============================================================

def can_split_array(
    nums: list[int],
    k: int,
    max_sum: int
) -> bool:
    """
    Check whether the array can be split into at most k
    non-empty contiguous subarrays, each having sum <= max_sum.
    """

    required_parts = 1
    current_sum = 0

    for num in nums:
        if current_sum + num <= max_sum:
            current_sum += num
        else:
            required_parts += 1
            current_sum = num

    return required_parts <= k


def split_array_largest_sum(nums: list[int], k: int) -> int:
    """
    Split the array into exactly k non-empty contiguous
    subarrays while minimizing the largest subarray sum.

    Array elements must be non-negative.

    Example:
    Input:
        nums = [7, 2, 5, 10, 8]
        k = 2

    Output: 18
    """

    if not nums:
        raise ValueError("Array cannot be empty.")

    if any(num < 0 for num in nums):
        raise ValueError("Array elements must be non-negative.")

    if k <= 0 or k > len(nums):
        raise ValueError("k must be between 1 and array length.")

    left = max(nums)
    right = sum(nums)
    answer = right

    while left <= right:
        max_sum = left + (right - left) // 2

        if can_split_array(nums, k, max_sum):
            answer = max_sum
            right = max_sum - 1
        else:
            left = max_sum + 1

    return answer


def run_program_60() -> None:
    print("\n--- PROGRAM 60: SPLIT ARRAY LARGEST SUM ---")

    nums = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter number of subarrays: "))

    result = split_array_largest_sum(nums, k)

    print("Minimum possible largest subarray sum:", result)


# ============================================================
# RUN ALL PROGRAMS
# ============================================================

def run_all_programs() -> None:
    print("\n========== RUNNING ALL DAY 12 PROGRAMS ==========")

    run_program_56()
    run_program_57()
    run_program_58()
    run_program_59()
    run_program_60()


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:
    while True:
        print("\n==============================================")
        print("       MONTH 11 - DAY 12 DSA MENU")
        print("       BINARY SEARCH ON ANSWER")
        print("==============================================")

        print("56. Integer Square Root")
        print("57. Smallest Divisor Given a Threshold")
        print("58. Capacity to Ship Packages Within D Days")
        print("59. Book Allocation Problem")
        print("60. Split Array Largest Sum")
        print("61. Run All Programs")
        print("0. Exit")

        print("==============================================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 56:
                run_program_56()

            elif choice == 57:
                run_program_57()

            elif choice == 58:
                run_program_58()

            elif choice == 59:
                run_program_59()

            elif choice == 60:
                run_program_60()

            elif choice == 61:
                run_all_programs()

            elif choice == 0:
                print("Exiting Day 12 DSA Programs. Keep practicing!")
                break

            else:
                print("Invalid choice. Please select 0-61.")

        except ValueError as error:
            print("Input error:", error)

        except Exception as error:
            print("An unexpected error occurred:", error)


if __name__ == "__main__":
    main()
