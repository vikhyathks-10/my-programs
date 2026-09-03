# ============================================================
# DAY 3 — ARRAY MANIPULATION
# Programs 11–15
# ============================================================


# ------------------------------------------------------------
# 11. Remove Duplicates from Sorted Array
# ------------------------------------------------------------

def remove_duplicates():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter sorted array: ").split()))

    if n == 0:
        print("Array is empty.")
        return

    # Two-pointer approach
    unique_index = 1

    for i in range(1, n):

        if arr[i] != arr[unique_index - 1]:
            arr[unique_index] = arr[i]
            unique_index += 1

    print("Array after removing duplicates:",
          arr[:unique_index])

    print("Number of unique elements:", unique_index)
    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 12. Move All Zeroes to the End
# ------------------------------------------------------------

def move_zeroes():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    position = 0

    # Move non-zero elements to the front
    for i in range(n):

        if arr[i] != 0:
            arr[position] = arr[i]
            position += 1

    # Fill remaining positions with zero
    while position < n:
        arr[position] = 0
        position += 1

    print("Array after moving zeroes:", arr)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 13. Move All Negative Numbers to the Beginning
# ------------------------------------------------------------

def move_negatives():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    position = 0

    for i in range(n):

        if arr[i] < 0:
            arr[position], arr[i] = arr[i], arr[position]
            position += 1

    print("Array after moving negatives:", arr)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 14. Left Rotate Array by One Position
# ------------------------------------------------------------

def left_rotate():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    if n == 0:
        print("Array is empty.")
        return

    first = arr[0]

    # Shift elements one position to the left
    for i in range(n - 1):
        arr[i] = arr[i + 1]

    arr[n - 1] = first

    print("Array after left rotation:", arr)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 15. Right Rotate Array by One Position
# ------------------------------------------------------------

def right_rotate():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    if n == 0:
        print("Array is empty.")
        return

    last = arr[n - 1]

    # Shift elements one position to the right
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last

    print("Array after right rotation:", arr)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 60)
        print("          DAY 3 — ARRAY MANIPULATION")
        print("=" * 60)

        print("11. Remove Duplicates from Sorted Array")
        print("12. Move All Zeroes to the End")
        print("13. Move All Negative Numbers to the Beginning")
        print("14. Left Rotate Array by One Position")
        print("15. Right Rotate Array by One Position")
        print("16. Run All Programs")
        print("17. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "11":
            remove_duplicates()

        elif choice == "12":
            move_zeroes()

        elif choice == "13":
            move_negatives()

        elif choice == "14":
            left_rotate()

        elif choice == "15":
            right_rotate()

        elif choice == "16":

            print("\n========== PROGRAM 11 ==========")
            remove_duplicates()

            print("\n========== PROGRAM 12 ==========")
            move_zeroes()

            print("\n========== PROGRAM 13 ==========")
            move_negatives()

            print("\n========== PROGRAM 14 ==========")
            left_rotate()

            print("\n========== PROGRAM 15 ==========")
            right_rotate()

        elif choice == "17":
            print("\nDay 3 completed! 🚀")
            break

        else:
            print("Invalid choice. Please try again.")


main()