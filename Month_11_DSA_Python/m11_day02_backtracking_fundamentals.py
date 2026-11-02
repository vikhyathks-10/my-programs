
from __future__ import annotations


# ============================================================
# PROGRAM 6 — GENERATE ALL PERMUTATIONS OF AN ARRAY
# ============================================================

def generate_array_permutations(numbers: list[int]) -> list[list[int]]:
    result: list[list[int]] = []

    numbers = sorted(numbers)
    used = [False] * len(numbers)

    def backtrack(current: list[int]) -> None:

        # Base case: all elements have been selected.
        if len(current) == len(numbers):
            result.append(current.copy())
            return

        for i in range(len(numbers)):

            if used[i]:
                continue

            # Skip duplicate permutations.
            if (
                i > 0
                and numbers[i] == numbers[i - 1]
                and not used[i - 1]
            ):
                continue

            used[i] = True
            current.append(numbers[i])

            backtrack(current)

            # Backtracking.
            current.pop()
            used[i] = False

    backtrack([])
    return result


def program_6() -> None:
    print("\nPROGRAM 6 — ARRAY PERMUTATIONS")

    numbers = list(map(int, input("Enter array elements: ").split()))

    permutations = generate_array_permutations(numbers)

    print("\nAll unique permutations:")

    for index, permutation in enumerate(permutations, start=1):
        print(f"{index}. {permutation}")

    print("Total permutations:", len(permutations))


# ============================================================
# PROGRAM 7 — GENERATE ALL SUBSETS USING BACKTRACKING
# ============================================================

def generate_array_subsets(numbers: list[int]) -> list[list[int]]:
    result: list[list[int]] = []

    numbers = sorted(numbers)

    def backtrack(start: int, current: list[int]) -> None:

        # Store the current subset.
        result.append(current.copy())

        for i in range(start, len(numbers)):

            # Skip duplicate subsets.
            if i > start and numbers[i] == numbers[i - 1]:
                continue

            current.append(numbers[i])

            backtrack(i + 1, current)

            # Backtracking.
            current.pop()

    backtrack(0, [])
    return result


def program_7() -> None:
    print("\nPROGRAM 7 — ARRAY SUBSETS")

    numbers = list(map(int, input("Enter array elements: ").split()))

    subsets = generate_array_subsets(numbers)

    print("\nAll unique subsets:")

    for index, subset in enumerate(subsets, start=1):
        print(f"{index}. {subset}")

    print("Total subsets:", len(subsets))


# ============================================================
# PROGRAM 8 — COMBINATIONS OF K NUMBERS FROM 1 TO N
# ============================================================

def generate_k_combinations(n: int, k: int) -> list[list[int]]:
    result: list[list[int]] = []

    if n < 0 or k < 0 or k > n:
        return result

    def backtrack(start: int, current: list[int]) -> None:

        # Stop when exactly k numbers have been selected.
        if len(current) == k:
            result.append(current.copy())
            return

        # Number of elements still needed.
        remaining = k - len(current)

        # Avoid exploring values that cannot complete a combination.
        last_start = n - remaining + 1

        for number in range(start, last_start + 1):

            current.append(number)

            backtrack(number + 1, current)

            current.pop()

    backtrack(1, [])
    return result


def program_8() -> None:
    print("\nPROGRAM 8 — COMBINATIONS OF K NUMBERS")

    n = int(input("Enter N: "))
    k = int(input("Enter K: "))

    combinations = generate_k_combinations(n, k)

    print(f"\nCombinations of {k} numbers from 1 to {n}:")

    for index, combination in enumerate(combinations, start=1):
        print(f"{index}. {combination}")

    print("Total combinations:", len(combinations))


# ============================================================
# PROGRAM 9 — COMBINATION SUM
# ============================================================

def find_combination_sum(
    candidates: list[int],
    target: int
) -> list[list[int]]:

    if any(number <= 0 for number in candidates):
        raise ValueError("All candidates must be positive integers.")

    candidates = sorted(set(candidates))
    result: list[list[int]] = []

    def backtrack(
        start: int,
        remaining: int,
        current: list[int]
    ) -> None:

        # Target reached.
        if remaining == 0:
            result.append(current.copy())
            return

        for i in range(start, len(candidates)):

            number = candidates[i]

            # Sorted candidates allow early termination.
            if number > remaining:
                break

            current.append(number)

            # Reuse the same candidate if needed.
            backtrack(i, remaining - number, current)

            # Backtracking.
            current.pop()

    if target < 0:
        return result

    backtrack(0, target, [])
    return result


def program_9() -> None:
    print("\nPROGRAM 9 — COMBINATION SUM")

    candidates = list(
        map(int, input("Enter candidate numbers: ").split())
    )

    target = int(input("Enter target sum: "))

    try:
        combinations = find_combination_sum(candidates, target)

        print("\nValid combinations:")

        if combinations:
            for index, combination in enumerate(combinations, start=1):
                print(f"{index}. {combination}")
        else:
            print("No combinations found.")

        print("Total combinations:", len(combinations))

    except ValueError as error:
        print("Error:", error)


# ============================================================
# PROGRAM 10 — RAT IN A MAZE
# ============================================================

def solve_rat_maze(
    maze: list[list[int]]
) -> list[str]:

    n = len(maze)

    if n == 0 or any(len(row) != n for row in maze):
        return []

    # Starting or ending cell is blocked.
    if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        return []

    result: list[str] = []

    # Directions: Down, Left, Right, Up.
    directions = [
        (1, 0, "D"),
        (0, -1, "L"),
        (0, 1, "R"),
        (-1, 0, "U")
    ]

    visited = [[False] * n for _ in range(n)]

    def backtrack(
        row: int,
        col: int,
        path: str
    ) -> None:

        # Destination reached.
        if row == n - 1 and col == n - 1:
            result.append(path)
            return

        visited[row][col] = True

        for row_change, col_change, direction in directions:

            new_row = row + row_change
            new_col = col + col_change

            # Check boundaries.
            if not (0 <= new_row < n and 0 <= new_col < n):
                continue

            # Check whether the cell is open and unvisited.
            if (
                maze[new_row][new_col] == 1
                and not visited[new_row][new_col]
            ):

                backtrack(
                    new_row,
                    new_col,
                    path + direction
                )

        # Backtracking: allow this cell in another path.
        visited[row][col] = False

    backtrack(0, 0, "")

    return sorted(result)


def program_10() -> None:
    print("\nPROGRAM 10 — RAT IN A MAZE")

    n = int(input("Enter maze size N: "))

    if n <= 0:
        print("Maze size must be positive.")
        return

    print("Enter the maze row by row.")
    print("Use 1 for an open cell and 0 for a blocked cell.")

    maze: list[list[int]] = []

    for row in range(n):
        values = list(
            map(int, input(f"Row {row + 1}: ").split())
        )

        if len(values) != n or any(value not in (0, 1) for value in values):
            print("Invalid row. Enter exactly N values containing only 0 or 1.")
            return

        maze.append(values)

    paths = solve_rat_maze(maze)

    print("\nPossible paths:")

    if paths:
        for index, path in enumerate(paths, start=1):
            print(f"{index}. {path}")
    else:
        print("No valid path exists.")

    print("Total paths:", len(paths))


# ============================================================
# RUN ALL PROGRAMS
# ============================================================

def run_all() -> None:

    print("\n========== PROGRAM 6 ==========")
    program_6()

    print("\n========== PROGRAM 7 ==========")
    program_7()

    print("\n========== PROGRAM 8 ==========")
    program_8()

    print("\n========== PROGRAM 9 ==========")
    program_9()

    print("\n========== PROGRAM 10 ==========")
    program_10()


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:

    while True:

        print("\n" + "=" * 55)
        print("       MONTH 11 — DAY 2: BACKTRACKING FUNDAMENTALS")
        print("=" * 55)

        print("6. Generate All Permutations of an Array")
        print("7. Generate All Subsets of an Array")
        print("8. Combinations of K Numbers from 1 to N")
        print("9. Combination Sum")
        print("10. Rat in a Maze")
        print("11. Run All Programs")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "6":
            program_6()

        elif choice == "7":
            program_7()

        elif choice == "8":
            program_8()

        elif choice == "9":
            program_9()

        elif choice == "10":
            program_10()

        elif choice == "11":
            run_all()

        elif choice == "0":
            print("\nDay 2 Backtracking Fundamentals Completed!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
