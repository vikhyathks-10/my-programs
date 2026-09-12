# ============================================================
# DAY 12 — BINARY SEARCH
# Programs 56–60
# ============================================================


# ------------------------------------------------------------
# 56. Implement Binary Search
# ------------------------------------------------------------

def binary_search():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter sorted array: ").split()))
    target = int(input("Enter target: "))

    left = 0
    right = n - 1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            print("Element found at index:", mid)
            print("Time Complexity: O(log N)")
            print("Space Complexity: O(1)")
            return

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    print("Element not found.")

    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 57. Find First Occurrence Using Binary Search
# ------------------------------------------------------------

def first_occurrence_binary():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter sorted array: ").split()))
    target = int(input("Enter target: "))

    left = 0
    right = n - 1

    answer = -1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:

            answer = mid

            # Search further to the left
            right = mid - 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    if answer != -1:
        print("First occurrence:", answer)
    else:
        print("Element not found.")

    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 58. Find Last Occurrence Using Binary Search
# ------------------------------------------------------------

def last_occurrence_binary():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter sorted array: ").split()))
    target = int(input("Enter target: "))

    left = 0
    right = n - 1

    answer = -1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:

            answer = mid

            # Search further to the right
            left = mid + 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    if answer != -1:
        print("Last occurrence:", answer)
    else:
        print("Element not found.")

    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 59. Count Occurrences Using Binary Search
# ------------------------------------------------------------

def count_occurrences_binary():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter sorted array: ").split()))
    target = int(input("Enter target: "))

    # Find first occurrence
    left = 0
    right = n - 1
    first = -1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            first = mid
            right = mid - 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    # Find last occurrence
    left = 0
    right = n - 1
    last = -1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            last = mid
            left = mid + 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    if first == -1:
        print("Element not found.")
        count = 0
    else:
        count = last - first + 1
        print("First occurrence:", first)
        print("Last occurrence:", last)
        print("Number of occurrences:", count)

    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 60. Find Insertion Position
# ------------------------------------------------------------

def insertion_position():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter sorted array: ").split()))
    target = int(input("Enter target: "))

    left = 0
    right = n - 1

    # Position where target should be inserted
    position = n

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] >= target:
            position = mid
            right = mid - 1

        else:
            left = mid + 1

    print("Insertion position:", position)

    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 65)
        print("                DAY 12 — BINARY SEARCH")
        print("=" * 65)

        print("56. Implement Binary Search")
        print("57. Find First Occurrence")
        print("58. Find Last Occurrence")
        print("59. Count Occurrences")
        print("60. Find Insertion Position")
        print("61. Run All Programs")
        print("62. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "56":
            binary_search()

        elif choice == "57":
            first_occurrence_binary()

        elif choice == "58":
            last_occurrence_binary()

        elif choice == "59":
            count_occurrences_binary()

        elif choice == "60":
            insertion_position()

        elif choice == "61":

            print("\n========== PROGRAM 56 ==========")
            binary_search()

            print("\n========== PROGRAM 57 ==========")
            first_occurrence_binary()

            print("\n========== PROGRAM 58 ==========")
            last_occurrence_binary()

            print("\n========== PROGRAM 59 ==========")
            count_occurrences_binary()

            print("\n========== PROGRAM 60 ==========")
            insertion_position()

        elif choice == "62":
            print("\nDay 12 completed! 🚀")
            break

        else:
            print("Invalid choice. Please try again.")


main()