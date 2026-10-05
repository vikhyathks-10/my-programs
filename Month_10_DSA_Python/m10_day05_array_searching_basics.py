# MONTH 10 - DAY 5
# Array Searching Basics
# Programs 21-25

# ---------------------------------------------------------
# ARRAY INPUT
# ---------------------------------------------------------
def get_array() -> list[int]:
    return list(map(
        int,
        input("Enter array elements separated by spaces: ").split()
    ))


# ---------------------------------------------------------
# 21. LINEAR SEARCH
# ---------------------------------------------------------
def linear_search(arr: list[int], target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


# ---------------------------------------------------------
# 22. FIND FIRST OCCURRENCE
# ---------------------------------------------------------
def first_occurrence(arr: list[int], target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


# ---------------------------------------------------------
# 23. FIND LAST OCCURRENCE
# ---------------------------------------------------------
def last_occurrence(arr: list[int], target: int) -> int:
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i

    return -1


# ---------------------------------------------------------
# 24. COUNT OCCURRENCES
# ---------------------------------------------------------
def count_occurrences(arr: list[int], target: int) -> int:
    count = 0

    for element in arr:
        if element == target:
            count += 1

    return count


# ---------------------------------------------------------
# 25. FIND ALL POSITIONS
# ---------------------------------------------------------
def all_positions(arr: list[int], target: int) -> list[int]:
    positions: list[int] = []

    for i in range(len(arr)):
        if arr[i] == target:
            positions.append(i)

    return positions


# ---------------------------------------------------------
# PROGRAM 21
# ---------------------------------------------------------
def program_21(arr: list[int]) -> None:
    target = int(input("Enter target element: "))

    index = linear_search(arr, target)

    if index == -1:
        print("Element not found.")
    else:
        print("Element found at index:", index)
        print("Position:", index + 1)


# ---------------------------------------------------------
# PROGRAM 22
# ---------------------------------------------------------
def program_22(arr: list[int]) -> None:
    target = int(input("Enter target element: "))

    index = first_occurrence(arr, target)

    if index == -1:
        print("Element not found.")
    else:
        print("First occurrence at index:", index)
        print("Position:", index + 1)


# ---------------------------------------------------------
# PROGRAM 23
# ---------------------------------------------------------
def program_23(arr: list[int]) -> None:
    target = int(input("Enter target element: "))

    index = last_occurrence(arr, target)

    if index == -1:
        print("Element not found.")
    else:
        print("Last occurrence at index:", index)
        print("Position:", index + 1)


# ---------------------------------------------------------
# PROGRAM 24
# ---------------------------------------------------------
def program_24(arr: list[int]) -> None:
    target = int(input("Enter target element: "))

    count = count_occurrences(arr, target)

    print("Number of occurrences:", count)


# ---------------------------------------------------------
# PROGRAM 25
# ---------------------------------------------------------
def program_25(arr: list[int]) -> None:
    target = int(input("Enter target element: "))

    positions = all_positions(arr, target)

    if not positions:
        print("Element not found.")
    else:
        print("Indices:", positions)
        print("Positions:", [index + 1 for index in positions])


# ---------------------------------------------------------
# DISPLAY ARRAY
# ---------------------------------------------------------
def display_array(arr: list[int]) -> None:
    if not arr:
        print("Array is empty.")
    else:
        print("Array:", arr)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main() -> None:
    arr: list[int] = []

    while True:
        print("\n======================================")
        print(" MONTH 10 - DAY 5")
        print(" ARRAY SEARCHING BASICS")
        print("======================================")
        print("1. Enter / Create array")
        print("2. Display array")
        print("3. Linear search (Program 21)")
        print("4. Find first occurrence (Program 22)")
        print("5. Find last occurrence (Program 23)")
        print("6. Count occurrences (Program 24)")
        print("7. Find all positions (Program 25)")
        print("8. Run all programs")
        print("9. Exit")
        print("======================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        try:
            if choice == 1:
                arr = get_array()
                print("Array created successfully.")
                display_array(arr)

            elif choice == 2:
                display_array(arr)

            elif choice == 3:
                if not arr:
                    print("Please create an array first.")
                else:
                    program_21(arr)

            elif choice == 4:
                if not arr:
                    print("Please create an array first.")
                else:
                    program_22(arr)

            elif choice == 5:
                if not arr:
                    print("Please create an array first.")
                else:
                    program_23(arr)

            elif choice == 6:
                if not arr:
                    print("Please create an array first.")
                else:
                    program_24(arr)

            elif choice == 7:
                if not arr:
                    print("Please create an array first.")
                else:
                    program_25(arr)

            elif choice == 8:
                if not arr:
                    print("Please create an array first.")
                    continue

                print("\n========== RUNNING ALL PROGRAMS ==========")

                print("\nProgram 21: Linear Search")
                program_21(arr)

                print("\nProgram 22: First Occurrence")
                program_22(arr)

                print("\nProgram 23: Last Occurrence")
                program_23(arr)

                print("\nProgram 24: Count Occurrences")
                program_24(arr)

                print("\nProgram 25: All Positions")
                program_25(arr)

            elif choice == 9:
                print("Exiting Month 10 - Day 5. Keep practicing!")
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