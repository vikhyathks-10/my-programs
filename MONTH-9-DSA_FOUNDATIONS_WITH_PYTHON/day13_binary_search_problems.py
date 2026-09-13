# ============================================================
# DAY 13 — BINARY SEARCH PROBLEMS
# Programs 61–65
# ============================================================


# ------------------------------------------------------------
# 61. Find Square Root Using Binary Search
# ------------------------------------------------------------

def square_root_binary_search():

    n = int(input("Enter a non-negative number: "))

    if n < 0:
        print("Square root is not defined for negative numbers.")
        return

    if n == 0 or n == 1:
        print("Integer square root:", n)
        print("Time Complexity: O(log N)")
        print("Space Complexity: O(1)")
        return

    left = 1
    right = n
    answer = 1

    while left <= right:

        mid = left + (right - left) // 2

        if mid * mid == n:
            answer = mid
            break

        elif mid * mid < n:
            answer = mid
            left = mid + 1

        else:
            right = mid - 1

    print("Integer square root:", answer)

    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 62. Search in a Rotated Sorted Array
# ------------------------------------------------------------

def search_rotated_array():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter rotated sorted array: ").split()))
    target = int(input("Enter target: "))

    left = 0
    right = n - 1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            print("Target found at index:", mid)

            print("Time Complexity: O(log N)")
            print("Space Complexity: O(1)")
            return

        # Left half is sorted
        if arr[left] <= arr[mid]:

            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:

            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    print("Target not found.")

    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 63. Find Minimum Element in Rotated Sorted Array
# ------------------------------------------------------------

def minimum_rotated_array():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter rotated sorted array: ").split()))

    left = 0
    right = n - 1

    while left < right:

        mid = left + (right - left) // 2

        if arr[mid] > arr[right]:
            # Minimum lies on the right
            left = mid + 1

        else:
            # Minimum is at mid or on the left
            right = mid

    print("Minimum element:", arr[left])

    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 64. Find Peak Element
# ------------------------------------------------------------

def find_peak_element():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    if n == 1:
        print("Peak element:", arr[0])
        print("Peak index: 0")

        print("Time Complexity: O(1)")
        print("Space Complexity: O(1)")
        return

    left = 0
    right = n - 1

    while left < right:

        mid = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            # We are on an increasing slope.
            # Peak is to the right.
            left = mid + 1

        else:
            # We are on a decreasing slope.
            # Peak is at mid or to the left.
            right = mid

    print("Peak element:", arr[left])
    print("Peak index:", left)

    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 65. Find Closest Element to a Target
# ------------------------------------------------------------

def closest_element():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter sorted array: ").split()))
    target = int(input("Enter target: "))

    left = 0
    right = n - 1

    # Exact match
    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            print("Closest element:", arr[mid])
            print("Index:", mid)

            print("Time Complexity: O(log N)")
            print("Space Complexity: O(1)")
            return

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    # At this point:
    # right = element smaller than target
    # left  = element greater than target

    if right < 0:
        closest_index = left

    elif left >= n:
        closest_index = right

    else:
        left_difference = target - arr[right]
        right_difference = arr[left] - target

        if left_difference <= right_difference:
            closest_index = right
        else:
            closest_index = left

    print("Closest element:", arr[closest_index])
    print("Index:", closest_index)

    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 65)
        print("          DAY 13 — BINARY SEARCH PROBLEMS")
        print("=" * 65)

        print("61. Find Square Root Using Binary Search")
        print("62. Search in Rotated Sorted Array")
        print("63. Find Minimum in Rotated Sorted Array")
        print("64. Find Peak Element")
        print("65. Find Closest Element to a Target")
        print("66. Run All Programs")
        print("67. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "61":
            square_root_binary_search()

        elif choice == "62":
            search_rotated_array()

        elif choice == "63":
            minimum_rotated_array()

        elif choice == "64":
            find_peak_element()

        elif choice == "65":
            closest_element()

        elif choice == "66":

            print("\n========== PROGRAM 61 ==========")
            square_root_binary_search()

            print("\n========== PROGRAM 62 ==========")
            search_rotated_array()

            print("\n========== PROGRAM 63 ==========")
            minimum_rotated_array()

            print("\n========== PROGRAM 64 ==========")
            find_peak_element()

            print("\n========== PROGRAM 65 ==========")
            closest_element()

        elif choice == "67":
            print("\nDay 13 completed! 🚀")
            break

        else:
            print("Invalid choice. Please try again.")


main()