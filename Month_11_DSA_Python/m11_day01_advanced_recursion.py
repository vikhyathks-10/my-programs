
from __future__ import annotations


# ============================================================
# PROGRAM 1 — GENERATE ALL SUBSEQUENCES OF A STRING
# ============================================================

def generate_subsequences(text: str) -> list[str]:
    result: list[str] = []

    def backtrack(index: int, current: str) -> None:
        # Base case: all characters have been considered.
        if index == len(text):
            result.append(current)
            return

        # Choice 1: Include the current character.
        backtrack(index + 1, current + text[index])

        # Choice 2: Exclude the current character.
        backtrack(index + 1, current)

    backtrack(0, "")
    return result


def program_1() -> None:
    print("\nPROGRAM 1 — GENERATE ALL SUBSEQUENCES")

    text = input("Enter a string: ")

    subsequences = generate_subsequences(text)

    print("\nAll subsequences:")
    for index, subsequence in enumerate(subsequences, start=1):
        print(f"{index}. {subsequence!r}")

    print("Total subsequences:", len(subsequences))


# ============================================================
# PROGRAM 2 — GENERATE ALL SUBSETS OF AN INTEGER ARRAY
# ============================================================

def generate_subsets(numbers: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    numbers.sort()

    def backtrack(index: int, current: list[int]) -> None:
        # Every current selection is a valid subset.
        result.append(current.copy())

        for i in range(index, len(numbers)):

            # Skip duplicate values at the same recursion level.
            if i > index and numbers[i] == numbers[i - 1]:
                continue

            current.append(numbers[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


def program_2() -> None:
    print("\nPROGRAM 2 — GENERATE ALL SUBSETS")

    numbers = list(map(int, input("Enter array elements: ").split()))

    subsets = generate_subsets(numbers)

    print("\nAll subsets:")
    for index, subset in enumerate(subsets, start=1):
        print(f"{index}. {subset}")

    print("Total unique subsets:", len(subsets))


# ============================================================
# PROGRAM 3 — COMBINATION SUM
# ============================================================

def combination_sum(
    candidates: list[int],
    target: int
) -> list[list[int]]:

    if any(number <= 0 for number in candidates):
        raise ValueError("Candidates must be positive integers.")

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

            # Since candidates are sorted, larger values can be skipped.
            if number > remaining:
                break

            current.append(number)

            # Use i instead of i + 1 to allow reuse.
            backtrack(i, remaining - number, current)

            current.pop()

    backtrack(0, target, [])
    return result


def program_3() -> None:
    print("\nPROGRAM 3 — COMBINATION SUM")

    candidates = list(
        map(int, input("Enter candidate numbers: ").split())
    )

    target = int(input("Enter target sum: "))

    try:
        combinations = combination_sum(candidates, target)

        print("\nCombinations:")
        if combinations:
            for index, combination in enumerate(combinations, start=1):
                print(f"{index}. {combination}")
        else:
            print("No valid combinations found.")

        print("Total combinations:", len(combinations))

    except ValueError as error:
        print("Error:", error)


# ============================================================
# PROGRAM 4 — GENERATE ALL UNIQUE PERMUTATIONS OF A STRING
# ============================================================

def generate_permutations(text: str) -> list[str]:
    result: list[str] = []

    characters = sorted(text)
    used = [False] * len(characters)

    def backtrack(current: str) -> None:

        # A permutation is complete when its length equals the input.
        if len(current) == len(characters):
            result.append(current)
            return

        for i in range(len(characters)):

            if used[i]:
                continue

            # Avoid generating duplicate permutations.
            if (
                i > 0
                and characters[i] == characters[i - 1]
                and not used[i - 1]
            ):
                continue

            used[i] = True
            backtrack(current + characters[i])
            used[i] = False

    backtrack("")
    return result


def program_4() -> None:
    print("\nPROGRAM 4 — GENERATE ALL PERMUTATIONS")

    text = input("Enter a string: ")

    permutations = generate_permutations(text)

    print("\nUnique permutations:")
    for index, permutation in enumerate(permutations, start=1):
        print(f"{index}. {permutation}")

    print("Total unique permutations:", len(permutations))


# ============================================================
# PROGRAM 5 — JOSEPHUS PROBLEM USING RECURSION
# ============================================================

def josephus(n: int, k: int) -> int:
    """
    Returns the safe position using 1-based indexing.
    """

    if n <= 0 or k <= 0:
        raise ValueError("Both n and k must be positive.")

    def solve(size: int) -> int:
        # Base case: only one person remains.
        if size == 1:
            return 0

        # Recursive result using 0-based indexing.
        return (solve(size - 1) + k) % size

    # Convert the 0-based answer to 1-based indexing.
    return solve(n) + 1


def program_5() -> None:
    print("\nPROGRAM 5 — JOSEPHUS PROBLEM")

    n = int(input("Enter number of people: "))
    k = int(input("Enter elimination interval: "))

    try:
        position = josephus(n, k)
        print("Safe position:", position)

    except ValueError as error:
        print("Error:", error)


# ============================================================
# RUN ALL PROGRAMS
# ============================================================

def run_all() -> None:
    print("\n========== PROGRAM 1 ==========")
    program_1()

    print("\n========== PROGRAM 2 ==========")
    program_2()

    print("\n========== PROGRAM 3 ==========")
    program_3()

    print("\n========== PROGRAM 4 ==========")
    program_4()

    print("\n========== PROGRAM 5 ==========")
    program_5()


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:
    while True:
        print("\n" + "=" * 55)
        print("       MONTH 11 — DAY 1: ADVANCED RECURSION")
        print("=" * 55)

        print("1. Generate All Subsequences of a String")
        print("2. Generate All Subsets of an Array")
        print("3. Combination Sum")
        print("4. Generate All Permutations of a String")
        print("5. Josephus Problem")
        print("6. Run All Programs")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            program_1()

        elif choice == "2":
            program_2()

        elif choice == "3":
            program_3()

        elif choice == "4":
            program_4()

        elif choice == "5":
            program_5()

        elif choice == "6":
            run_all()

        elif choice == "0":
            print("\nDay 1 Advanced Recursion Completed!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
