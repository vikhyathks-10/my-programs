# ============================================================
# DAY 31 - PROGRAM 158
# OPTIMIZATION CHALLENGE
# ============================================================

import time


# ============================================================
# BRUTE FORCE SOLUTION
# Time Complexity: O(n²)
# ============================================================

def two_sum_brute_force(numbers, target):

    for i in range(len(numbers)):

        for j in range(i + 1, len(numbers)):

            if numbers[i] + numbers[j] == target:

                return (
                    numbers[i],
                    numbers[j]
                )

    return None


# ============================================================
# OPTIMIZED SOLUTION
# Time Complexity: O(n)
# Space Complexity: O(n)
# ============================================================

def two_sum_optimized(numbers, target):

    seen = set()

    for number in numbers:

        required = target - number

        if required in seen:

            return (
                required,
                number
            )

        seen.add(number)

    return None


# ============================================================
# PERFORMANCE COMPARISON
# ============================================================

def compare_performance(numbers, target):

    start = time.perf_counter()

    brute_result = two_sum_brute_force(
        numbers,
        target
    )

    brute_time = (
        time.perf_counter() - start
    )

    start = time.perf_counter()

    optimized_result = two_sum_optimized(
        numbers,
        target
    )

    optimized_time = (
        time.perf_counter() - start
    )

    print("\n" + "=" * 60)

    print(
        "           PERFORMANCE COMPARISON"
    )

    print("=" * 60)

    print(
        f"Brute Force Result : {brute_result}"
    )

    print(
        f"Brute Force Time   : "
        f"{brute_time:.10f} seconds"
    )

    print(
        f"\nOptimized Result   : {optimized_result}"
    )

    print(
        f"Optimized Time     : "
        f"{optimized_time:.10f} seconds"
    )

    print("=" * 60)

    print(
        "\nBrute Force Complexity : O(n²)"
    )

    print(
        "Optimized Complexity   : O(n)"
    )

    print("=" * 60)


def main():

    print("=" * 60)

    print(
        "          TWO-SUM OPTIMIZATION"
    )

    print("=" * 60)

    numbers = [
        10,
        25,
        37,
        42,
        56,
        63,
        71,
        89,
        100
    ]

    target = int(
        input(
            "\nEnter target value: "
        )
    )

    result = two_sum_optimized(
        numbers,
        target
    )

    if result:

        print(
            f"\nPair found: "
            f"{result[0]} + {result[1]} = {target}"
        )

    else:

        print(
            "\nNo pair found."
        )

    compare_performance(
        numbers,
        target
    )


if __name__ == "__main__":

    main()