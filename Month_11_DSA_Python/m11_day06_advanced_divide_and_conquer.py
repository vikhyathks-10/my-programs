"""
MONTH 11 - DAY 6
ADVANCED DIVIDE AND CONQUER

Programs:
26. Kth Largest Element using Quickselect
27. Count Inversions using Merge Sort
28. Closest Pair of Points using Divide and Conquer
29. Maximum Sum Subarray Crossing the Midpoint
30. Fast Exponentiation using Divide and Conquer

Menu:
26-30: Run individual programs
31: Run all programs
0: Exit
"""

from typing import Optional


# ---------------------------------------------------------
# PROGRAM 26: KTH LARGEST ELEMENT USING QUICKSELECT
# ---------------------------------------------------------

def quickselect_kth_largest(arr: list[int], k: int) -> int:
    """
    Find the kth largest element.
    Duplicate values are counted separately.
    k is 1-based.
    """

    if not arr:
        raise ValueError("Array cannot be empty.")

    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and the array length.")

    values = arr.copy()

    # Convert kth largest into an ascending order index.
    target = len(values) - k

    low = 0
    high = len(values) - 1

    while low <= high:
        pivot = values[(low + high) // 2]

        # Three-way partition:
        # [low, smaller_end] < pivot
        # [smaller_end+1, equal_end] == pivot
        # [equal_end+1, high] > pivot

        smaller_end = low
        current = low
        larger_start = high

        while current <= larger_start:
            if values[current] < pivot:
                values[smaller_end], values[current] = (
                    values[current],
                    values[smaller_end]
                )
                smaller_end += 1
                current += 1

            elif values[current] > pivot:
                values[current], values[larger_start] = (
                    values[larger_start],
                    values[current]
                )
                larger_start -= 1

            else:
                current += 1

        if target < smaller_end:
            high = smaller_end - 1
        elif target > larger_start:
            low = larger_start + 1
        else:
            return pivot

    raise ValueError("Kth largest element not found.")


def program_26() -> None:
    print("\nPROGRAM 26: KTH LARGEST ELEMENT USING QUICKSELECT")

    arr = [7, 10, 4, 3, 20, 15]
    k = 3

    print("Array:", arr)
    print("K:", k)

    result = quickselect_kth_largest(arr, k)

    print(f"{k}rd largest element: {result}" if k == 3
          else f"{k}th largest element: {result}")


# ---------------------------------------------------------
# PROGRAM 27: COUNT INVERSIONS USING MERGE SORT
# ---------------------------------------------------------

def merge_and_count(
    arr: list[int],
    left: int,
    mid: int,
    right: int
) -> int:
    """Merge two sorted halves and count split inversions."""

    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    inversions = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1

            # Every remaining element in left_part
            # forms an inversion with right_part[j-1].
            inversions += len(left_part) - i

        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

    return inversions


def count_inversions_recursive(
    arr: list[int],
    left: int,
    right: int
) -> int:
    """Count inversions recursively using merge sort."""

    if left >= right:
        return 0

    mid = (left + right) // 2

    left_count = count_inversions_recursive(arr, left, mid)
    right_count = count_inversions_recursive(arr, mid + 1, right)

    split_count = merge_and_count(arr, left, mid, right)

    return left_count + right_count + split_count


def count_inversions(arr: list[int]) -> int:
    """Return the total number of inversions."""

    values = arr.copy()

    if len(values) < 2:
        return 0

    return count_inversions_recursive(values, 0, len(values) - 1)


def program_27() -> None:
    print("\nPROGRAM 27: COUNT INVERSIONS USING MERGE SORT")

    arr = [8, 4, 2, 1]

    print("Array:", arr)

    result = count_inversions(arr)

    print("Number of inversions:", result)


# ---------------------------------------------------------
# PROGRAM 28: CLOSEST PAIR OF POINTS
# USING DIVIDE AND CONQUER
# ---------------------------------------------------------

Point = tuple[float, float]
ClosestResult = tuple[float, Point, Point]


def distance(point1: Point, point2: Point) -> float:
    """Calculate Euclidean distance between two points."""

    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]

    return (dx * dx + dy * dy) ** 0.5


def closest_pair_recursive(
    points_x: list[Point]
) -> tuple[ClosestResult, list[Point]]:
    """
    Return the closest pair and points sorted by y-coordinate.

    points_x is sorted by x-coordinate.
    """

    n = len(points_x)

    # Brute force for small groups.
    if n <= 3:
        best: ClosestResult = (
            float("inf"),
            points_x[0],
            points_x[0]
        )

        for i in range(n):
            for j in range(i + 1, n):
                current_distance = distance(points_x[i], points_x[j])

                if current_distance < best[0]:
                    best = (
                        current_distance,
                        points_x[i],
                        points_x[j]
                    )

        points_y = sorted(points_x, key=lambda point: point[1])

        return best, points_y

    mid = n // 2
    midpoint_x = points_x[mid][0]

    left_result, left_y = closest_pair_recursive(points_x[:mid])
    right_result, right_y = closest_pair_recursive(points_x[mid:])

    # Choose the better result from the two halves.
    if left_result[0] <= right_result[0]:
        best = left_result
    else:
        best = right_result

    # Merge the two y-sorted lists.
    points_y: list[Point] = []
    i = 0
    j = 0

    while i < len(left_y) and j < len(right_y):
        if left_y[i][1] <= right_y[j][1]:
            points_y.append(left_y[i])
            i += 1
        else:
            points_y.append(right_y[j])
            j += 1

    points_y.extend(left_y[i:])
    points_y.extend(right_y[j:])

    # Keep points close enough to the dividing line.
    strip = [
        point for point in points_y
        if abs(point[0] - midpoint_x) < best[0]
    ]

    # Compare each point with at most the next 7 points.
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 8, len(strip))):
            if strip[j][1] - strip[i][1] >= best[0]:
                break

            current_distance = distance(strip[i], strip[j])

            if current_distance < best[0]:
                best = (current_distance, strip[i], strip[j])

    return best, points_y


def closest_pair(points: list[Point]) -> Optional[ClosestResult]:
    """Find the closest pair among at least two points."""

    if len(points) < 2:
        return None

    points_x = sorted(points, key=lambda point: (point[0], point[1]))

    result, _ = closest_pair_recursive(points_x)

    return result


def program_28() -> None:
    print("\nPROGRAM 28: CLOSEST PAIR OF POINTS")

    points: list[Point] = [
        (2.0, 3.0),
        (12.0, 30.0),
        (40.0, 50.0),
        (5.0, 1.0),
        (12.0, 10.0),
        (3.0, 4.0)
    ]

    print("Points:", points)

    result = closest_pair(points)

    if result is not None:
        minimum_distance, point1, point2 = result

        print("Closest points:", point1, "and", point2)
        print(f"Minimum distance: {minimum_distance:.4f}")


# ---------------------------------------------------------
# PROGRAM 29: MAXIMUM SUM SUBARRAY CROSSING MIDPOINT
# ---------------------------------------------------------

def max_crossing_subarray(
    arr: list[int],
    low: int,
    mid: int,
    high: int
) -> tuple[int, int, int]:
    """
    Find the maximum-sum contiguous subarray that
    must include elements on both sides of mid.

    Returns:
        (maximum_sum, start_index, end_index)
    """

    left_sum = float("-inf")
    current_sum = 0
    max_left = mid

    for i in range(mid, low - 1, -1):
        current_sum += arr[i]

        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i

    right_sum = float("-inf")
    current_sum = 0
    max_right = mid + 1

    for i in range(mid + 1, high + 1):
        current_sum += arr[i]

        if current_sum > right_sum:
            right_sum = current_sum
            max_right = i

    return int(left_sum + right_sum), max_left, max_right


def program_29() -> None:
    print("\nPROGRAM 29: MAXIMUM SUM SUBARRAY CROSSING MIDPOINT")

    arr = [2, -4, 5, 6, -2, 3, -1, 4]
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    print("Array:", arr)
    print("Midpoint index:", mid)

    result_sum, start, end = max_crossing_subarray(
        arr, low, mid, high
    )

    print("Crossing subarray:", arr[start:end + 1])
    print("Start index:", start)
    print("End index:", end)
    print("Maximum crossing sum:", result_sum)


# ---------------------------------------------------------
# PROGRAM 30: FAST EXPONENTIATION
# USING DIVIDE AND CONQUER
# ---------------------------------------------------------

def fast_power(base: float, exponent: int) -> float:
    """
    Calculate base raised to exponent using exponentiation
    by squaring.

    Supports negative integer exponents.
    """

    if exponent == 0:
        return 1.0

    if base == 0 and exponent < 0:
        raise ValueError("Zero cannot have a negative exponent.")

    if exponent < 0:
        return 1.0 / fast_power(base, -exponent)

    half = fast_power(base, exponent // 2)

    if exponent % 2 == 0:
        return half * half

    return base * half * half


def program_30() -> None:
    print("\nPROGRAM 30: FAST EXPONENTIATION")

    base = 2.0
    exponent = 10

    print("Base:", base)
    print("Exponent:", exponent)

    result = fast_power(base, exponent)

    print("Result:", result)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main() -> None:
    while True:
        print("\n==========================================")
        print(" MONTH 11 - DAY 6: ADVANCED DIVIDE & CONQUER")
        print("==========================================")
        print("26. Kth Largest Element using Quickselect")
        print("27. Count Inversions using Merge Sort")
        print("28. Closest Pair of Points")
        print("29. Maximum Sum Subarray Crossing Midpoint")
        print("30. Fast Exponentiation")
        print("31. Run All Programs")
        print("0. Exit")
        print("==========================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 26:
            program_26()
        elif choice == 27:
            program_27()
        elif choice == 28:
            program_28()
        elif choice == 29:
            program_29()
        elif choice == 30:
            program_30()
        elif choice == 31:
            for program in (
                program_26,
                program_27,
                program_28,
                program_29,
                program_30
            ):
                program()
        elif choice == 0:
            print("Exiting Day 6 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 0 or 26-31.")


if __name__ == "__main__":
    main()