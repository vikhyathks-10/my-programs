# ============================================================
# DAY 6 — ARRAY PROBLEM SOLVING
# Programs 26–30
# ============================================================


# ------------------------------------------------------------
# 26. Find Missing Number from 1..N
# ------------------------------------------------------------

def find_missing_number():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter N-1 numbers: ").split()))

    # Sum of numbers from 1 to N
    expected_sum = n * (n + 1) // 2

    actual_sum = 0

    for num in arr:
        actual_sum += num

    missing = expected_sum - actual_sum

    print("Missing number:", missing)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 27. Find Duplicate Number
# ------------------------------------------------------------

def find_duplicate():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    seen = set()
    duplicate = -1

    for num in arr:

        if num in seen:
            duplicate = num
            break

        seen.add(num)

    if duplicate != -1:
        print("Duplicate number:", duplicate)
    else:
        print("No duplicate found.")

    print("Average Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# 28. Find Two Numbers with Given Sum
# ------------------------------------------------------------

def two_sum():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target sum: "))

    seen = set()
    found = False

    for num in arr:

        required = target - num

        if required in seen:
            print("Pair found:", required, "+", num,
                  "=", target)
            found = True
            break

        seen.add(num)

    if not found:
        print("No pair found.")

    print("Average Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# 29. Find Intersection of Two Arrays
# ------------------------------------------------------------

def intersection():

    n1 = int(input("Enter size of first array: "))
    arr1 = list(map(int, input("Enter first array: ").split()))

    n2 = int(input("Enter size of second array: "))
    arr2 = list(map(int, input("Enter second array: ").split()))

    set1 = set(arr1)
    result = set()

    for num in arr2:

        if num in set1:
            result.add(num)

    print("Intersection:", list(result))

    print("Average Time Complexity: O(N + M)")
    print("Space Complexity: O(N + M)")


# ------------------------------------------------------------
# 30. Find Union of Two Arrays
# ------------------------------------------------------------

def union():

    n1 = int(input("Enter size of first array: "))
    arr1 = list(map(int, input("Enter first array: ").split()))

    n2 = int(input("Enter size of second array: "))
    arr2 = list(map(int, input("Enter second array: ").split()))

    result = set()

    for num in arr1:
        result.add(num)

    for num in arr2:
        result.add(num)

    print("Union:", list(result))

    print("Average Time Complexity: O(N + M)")
    print("Space Complexity: O(N + M)")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 65)
        print("            DAY 6 — ARRAY PROBLEM SOLVING")
        print("=" * 65)

        print("26. Find Missing Number from 1..N")
        print("27. Find Duplicate Number")
        print("28. Find Two Numbers with Given Sum")
        print("29. Find Intersection of Two Arrays")
        print("30. Find Union of Two Arrays")
        print("31. Run All Programs")
        print("32. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "26":
            find_missing_number()

        elif choice == "27":
            find_duplicate()

        elif choice == "28":
            two_sum()

        elif choice == "29":
            intersection()

        elif choice == "30":
            union()

        elif choice == "31":

            print("\n========== PROGRAM 26 ==========")
            find_missing_number()

            print("\n========== PROGRAM 27 ==========")
            find_duplicate()

            print("\n========== PROGRAM 28 ==========")
            two_sum()

            print("\n========== PROGRAM 29 ==========")
            intersection()

            print("\n========== PROGRAM 30 ==========")
            union()

        elif choice == "32":
            print("\nDay 6 completed! 🚀")
            break

        else:
            print("Invalid choice. Please try again.")


main()