# MONTH 10 - DAY 6
# Array Problem Solving
# Programs 26-30

# ---------------------------------------------------------
# ARRAY INPUT
# ---------------------------------------------------------
def get_array(prompt: str) -> list[int]:
    return list(map(
        int,
        input(prompt).split()
    ))


# ---------------------------------------------------------
# 26. FIND MISSING NUMBER FROM 1..N
# ---------------------------------------------------------
def find_missing_number(arr: list[int], n: int) -> int | None:
    if len(arr) != n - 1:
        return None

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)

    return expected_sum - actual_sum


# ---------------------------------------------------------
# 27. FIND DUPLICATE NUMBER
# ---------------------------------------------------------
def find_duplicate(arr: list[int]) -> int | None:
    seen: set[int] = set()

    for number in arr:
        if number in seen:
            return number

        seen.add(number)

    return None


# ---------------------------------------------------------
# 28. FIND TWO NUMBERS WITH GIVEN SUM
# ---------------------------------------------------------
def two_sum(arr: list[int], target: int) -> tuple[int, int] | None:
    seen: set[int] = set()

    for number in arr:
        complement = target - number

        if complement in seen:
            return complement, number

        seen.add(number)

    return None


# ---------------------------------------------------------
# 29. FIND INTERSECTION OF TWO ARRAYS
# ---------------------------------------------------------
def intersection(arr1: list[int], arr2: list[int]) -> list[int]:
    set1 = set(arr1)
    set2 = set(arr2)

    result = list(set1 & set2)

    return result


# ---------------------------------------------------------
# 30. FIND UNION OF TWO ARRAYS
# ---------------------------------------------------------
def union(arr1: list[int], arr2: list[int]) -> list[int]:
    result = list(set(arr1) | set(arr2))

    return result


# ---------------------------------------------------------
# PROGRAM 26
# ---------------------------------------------------------
def program_26() -> None:
    n = int(input("Enter N: "))

    if n <= 0:
        print("N must be positive.")
        return

    arr = get_array(
        f"Enter {n - 1} numbers from 1 to {n}, with one missing: "
    )

    if len(arr) != n - 1:
        print(f"Please enter exactly {n - 1} numbers.")
        return

    if any(number < 1 or number > n for number in arr):
        print(f"All numbers must be between 1 and {n}.")
        return

    missing = find_missing_number(arr, n)

    if missing is None:
        print("Invalid input.")
    else:
        print("Missing number:", missing)


# ---------------------------------------------------------
# PROGRAM 27
# ---------------------------------------------------------
def program_27() -> None:
    arr = get_array("Enter array elements: ")

    duplicate = find_duplicate(arr)

    if duplicate is None:
        print("No duplicate element found.")
    else:
        print("Duplicate element:", duplicate)


# ---------------------------------------------------------
# PROGRAM 28
# ---------------------------------------------------------
def program_28() -> None:
    arr = get_array("Enter array elements: ")
    target = int(input("Enter target sum: "))

    result = two_sum(arr, target)

    if result is None:
        print("No two numbers found with the given sum.")
    else:
        first, second = result

        print("Two numbers:", first, "and", second)
        print("Sum:", first + second)


# ---------------------------------------------------------
# PROGRAM 29
# ---------------------------------------------------------
def program_29() -> None:
    arr1 = get_array("Enter first array: ")
    arr2 = get_array("Enter second array: ")

    result = intersection(arr1, arr2)

    if result:
        print("Intersection:", result)
    else:
        print("No common elements found.")


# ---------------------------------------------------------
# PROGRAM 30
# ---------------------------------------------------------
def program_30() -> None:
    arr1 = get_array("Enter first array: ")
    arr2 = get_array("Enter second array: ")

    result = union(arr1, arr2)

    print("Union:", result)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main() -> None:

    while True:
        print("\n======================================")
        print(" MONTH 10 - DAY 6")
        print(" ARRAY PROBLEM SOLVING")
        print("======================================")
        print("26. Find missing number from 1..N")
        print("27. Find duplicate number")
        print("28. Find two numbers with given sum")
        print("29. Find intersection of two arrays")
        print("30. Find union of two arrays")
        print("31. Run all programs")
        print("32. Exit")
        print("======================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        try:
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
                print("\n========== RUNNING ALL PROGRAMS ==========")

                print("\nProgram 26: Missing Number")
                program_26()

                print("\nProgram 27: Duplicate Number")
                program_27()

                print("\nProgram 28: Two Numbers With Given Sum")
                program_28()

                print("\nProgram 29: Intersection")
                program_29()

                print("\nProgram 30: Union")
                program_30()

            elif choice == 32:
                print("Exiting Month 10 - Day 6. Keep practicing!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input. Please enter integers only.")


# ---------------------------------------------------------
# PROGRAM START
# ---------------------------------------------------------
if __name__ == "__main__":
    main()