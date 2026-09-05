# ============================================================
# DAY 5 — ARRAY SEARCHING BASICS
# Programs 21–25
# ============================================================


# ------------------------------------------------------------
# 21. Linear Search
# ------------------------------------------------------------

def linear_search():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target: "))

    found = False

    for i in range(n):
        if arr[i] == target:
            print("Element found at index:", i)
            found = True
            break

    if not found:
        print("Element not found.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 22. Find First Occurrence
# ------------------------------------------------------------

def first_occurrence():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target: "))

    index = -1

    for i in range(n):
        if arr[i] == target:
            index = i
            break

    if index != -1:
        print("First occurrence:", index)
    else:
        print("Element not found.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 23. Find Last Occurrence
# ------------------------------------------------------------

def last_occurrence():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target: "))

    index = -1

    for i in range(n):
        if arr[i] == target:
            index = i

    if index != -1:
        print("Last occurrence:", index)
    else:
        print("Element not found.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 24. Count Occurrences of an Element
# ------------------------------------------------------------

def count_occurrences():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target: "))

    count = 0

    for i in range(n):
        if arr[i] == target:
            count += 1

    print("Number of occurrences:", count)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 25. Find All Positions of a Target
# ------------------------------------------------------------

def all_positions():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target: "))

    positions = []

    for i in range(n):
        if arr[i] == target:
            positions.append(i)

    if len(positions) == 0:
        print("Element not found.")
    else:
        print("Target found at indices:", positions)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(K)")
    print("where K = number of occurrences")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 60)
        print("          DAY 5 — ARRAY SEARCHING BASICS")
        print("=" * 60)

        print("21. Linear Search")
        print("22. Find First Occurrence")
        print("23. Find Last Occurrence")
        print("24. Count Occurrences")
        print("25. Find All Positions of a Target")
        print("26. Run All Programs")
        print("27. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "21":
            linear_search()

        elif choice == "22":
            first_occurrence()

        elif choice == "23":
            last_occurrence()

        elif choice == "24":
            count_occurrences()

        elif choice == "25":
            all_positions()

        elif choice == "26":

            print("\n========== PROGRAM 21 ==========")
            linear_search()

            print("\n========== PROGRAM 22 ==========")
            first_occurrence()

            print("\n========== PROGRAM 23 ==========")
            last_occurrence()

            print("\n========== PROGRAM 24 ==========")
            count_occurrences()

            print("\n========== PROGRAM 25 ==========")
            all_positions()

        elif choice == "27":
            print("\nDay 5 completed! 🚀")
            break

        else:
            print("Invalid choice. Please try again.")


main()