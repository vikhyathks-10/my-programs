"""
MONTH 11 - DAY 7
WEEK 1 REVISION

Programs:
31. Generate All Unique Subsets with Duplicates
32. Combination Sum II
33. N-Queens: Find and Count All Valid Arrangements
34. Median of Two Sorted Arrays using Binary Search
35. Kth Smallest Element in Two Sorted Arrays

Menu:
31-35: Run individual programs
36: Run all programs
0: Exit
"""


# ---------------------------------------------------------
# PROGRAM 31: GENERATE ALL UNIQUE SUBSETS
# ---------------------------------------------------------

def unique_subsets(arr: list[int]) -> list[list[int]]:
    """Generate all unique subsets of an array with duplicates."""

    arr.sort()
    result: list[list[int]] = []
    current: list[int] = []

    def backtrack(start: int) -> None:
        result.append(current.copy())

        for i in range(start, len(arr)):
            # Skip duplicate choices at the same recursion level.
            if i > start and arr[i] == arr[i - 1]:
                continue

            current.append(arr[i])
            backtrack(i + 1)
            current.pop()

    backtrack(0)
    return result


def program_31() -> None:
    print("\nPROGRAM 31: UNIQUE SUBSETS WITH DUPLICATES")

    arr = [1, 2, 2]

    print("Original array:", arr)

    result = unique_subsets(arr)

    print("Unique subsets:")
    for subset in result:
        print(subset)

    print("Total unique subsets:", len(result))


# ---------------------------------------------------------
# PROGRAM 32: COMBINATION SUM II
# ---------------------------------------------------------

def combination_sum_ii(
    candidates: list[int],
    target: int
) -> list[list[int]]:
    """
    Find unique combinations that add up to target.
    Each candidate can be used only once.
    Candidates must be positive integers.
    """

    candidates.sort()

    result: list[list[int]] = []
    current: list[int] = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(current.copy())
            return

        for i in range(start, len(candidates)):
            # Avoid duplicate combinations.
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            value = candidates[i]

            # Positive sorted candidates allow early stopping.
            if value > remaining:
                break

            current.append(value)
            backtrack(i + 1, remaining - value)
            current.pop()

    backtrack(0, target)
    return result


def program_32() -> None:
    print("\nPROGRAM 32: COMBINATION SUM II")

    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    print("Candidates:", candidates)
    print("Target:", target)

    result = combination_sum_ii(candidates, target)

    print("Unique combinations:")
    for combination in result:
        print(combination)


# ---------------------------------------------------------
# PROGRAM 33: N-QUEENS - FIND AND COUNT ARRANGEMENTS
# ---------------------------------------------------------

def solve_n_queens(n: int) -> list[list[str]]:
    """Generate every valid N-Queens board arrangement."""

    if n < 1:
        raise ValueError("N must be at least 1.")

    result: list[list[str]] = []

    board = [["." for _ in range(n)] for _ in range(n)]

    columns: set[int] = set()
    diagonal_down: set[int] = set()
    diagonal_up: set[int] = set()

    def backtrack(row: int) -> None:
        if row == n:
            result.append(["".join(board_row) for board_row in board])
            return

        for col in range(n):
            down = row - col
            up = row + col

            if (
                col in columns
                or down in diagonal_down
                or up in diagonal_up
            ):
                continue

            # Place queen.
            board[row][col] = "Q"
            columns.add(col)
            diagonal_down.add(down)
            diagonal_up.add(up)

            backtrack(row + 1)

            # Backtrack.
            board[row][col] = "."
            columns.remove(col)
            diagonal_down.remove(down)
            diagonal_up.remove(up)

    backtrack(0)
    return result


def program_33() -> None:
    print("\nPROGRAM 33: N-QUEENS")

    n = 4

    print("Board size:", n, "x", n)

    solutions = solve_n_queens(n)

    for index, solution in enumerate(solutions, start=1):
        print(f"\nArrangement {index}:")
        for row in solution:
            print(row)

    print("\nTotal valid arrangements:", len(solutions))


# ---------------------------------------------------------
# PROGRAM 34: MEDIAN OF TWO SORTED ARRAYS
# USING BINARY SEARCH
# ---------------------------------------------------------

def median_two_sorted_arrays(
    nums1: list[int],
    nums2: list[int]
) -> float:
    """
    Find the median of two sorted arrays in
    O(log(min(m, n))) time.
    """

    if not nums1 and not nums2:
        raise ValueError("Both arrays cannot be empty.")

    # Binary search on the smaller array.
    if len(nums1) > len(nums2):
        return median_two_sorted_arrays(nums2, nums1)

    m = len(nums1)
    n = len(nums2)

    low = 0
    high = m
    half = (m + n + 1) // 2

    while low <= high:
        i = (low + high) // 2
        j = half - i

        left_a = nums1[i - 1] if i > 0 else None
        right_a = nums1[i] if i < m else None

        left_b = nums2[j - 1] if j > 0 else None
        right_b = nums2[j] if j < n else None

        # Check whether the partition is valid.
        if (
            left_a is not None
            and right_b is not None
            and left_a > right_b
        ):
            high = i - 1

        elif (
            left_b is not None
            and right_a is not None
            and left_b > right_a
        ):
            low = i + 1

        else:
            left_values = [
                value for value in (left_a, left_b)
                if value is not None
            ]

            right_values = [
                value for value in (right_a, right_b)
                if value is not None
            ]

            max_left = max(left_values)

            if (m + n) % 2 == 1:
                return float(max_left)

            min_right = min(right_values)

            return (max_left + min_right) / 2.0

    raise ValueError("Input arrays must be sorted.")


def program_34() -> None:
    print("\nPROGRAM 34: MEDIAN OF TWO SORTED ARRAYS")

    nums1 = [1, 3]
    nums2 = [2, 4]

    print("First sorted array:", nums1)
    print("Second sorted array:", nums2)

    result = median_two_sorted_arrays(nums1, nums2)

    print("Median:", result)


# ---------------------------------------------------------
# PROGRAM 35: KTH SMALLEST IN TWO SORTED ARRAYS
# ---------------------------------------------------------

def kth_smallest_two_sorted_arrays(
    nums1: list[int],
    nums2: list[int],
    k: int
) -> int:
    """
    Find the kth smallest element in two sorted arrays.
    k is 1-based.
    """

    total = len(nums1) + len(nums2)

    if k < 1 or k > total:
        raise ValueError("k is outside the valid range.")

    # Binary search on the smaller array.
    if len(nums1) > len(nums2):
        return kth_smallest_two_sorted_arrays(nums2, nums1, k)

    m = len(nums1)
    n = len(nums2)

    # i + j must equal k.
    low = max(0, k - n)
    high = min(k, m)

    while low <= high:
        i = (low + high) // 2
        j = k - i

        left_a = nums1[i - 1] if i > 0 else None
        right_a = nums1[i] if i < m else None

        left_b = nums2[j - 1] if j > 0 else None
        right_b = nums2[j] if j < n else None

        if (
            left_a is not None
            and right_b is not None
            and left_a > right_b
        ):
            high = i - 1

        elif (
            left_b is not None
            and right_a is not None
            and left_b > right_a
        ):
            low = i + 1

        else:
            left_values = [
                value for value in (left_a, left_b)
                if value is not None
            ]

            return max(left_values)

    raise ValueError("Input arrays must be sorted.")


def program_35() -> None:
    print("\nPROGRAM 35: KTH SMALLEST IN TWO SORTED ARRAYS")

    nums1 = [2, 3, 6, 7, 9]
    nums2 = [1, 4, 8, 10]
    k = 5

    print("First sorted array:", nums1)
    print("Second sorted array:", nums2)
    print("K:", k)

    result = kth_smallest_two_sorted_arrays(nums1, nums2, k)

    print(f"{k}th smallest element:", result)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main() -> None:
    while True:
        print("\n========================================")
        print(" MONTH 11 - DAY 7: WEEK 1 REVISION")
        print("========================================")
        print("31. Generate Unique Subsets")
        print("32. Combination Sum II")
        print("33. N-Queens: Find and Count Solutions")
        print("34. Median of Two Sorted Arrays")
        print("35. Kth Smallest in Two Sorted Arrays")
        print("36. Run All Programs")
        print("0. Exit")
        print("========================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 31:
            program_31()
        elif choice == 32:
            program_32()
        elif choice == 33:
            program_33()
        elif choice == 34:
            program_34()
        elif choice == 35:
            program_35()
        elif choice == 36:
            for program in (
                program_31,
                program_32,
                program_33,
                program_34,
                program_35
            ):
                program()
        elif choice == 0:
            print("Week 1 revision completed. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 0 or 31-36.")


if __name__ == "__main__":
    main()