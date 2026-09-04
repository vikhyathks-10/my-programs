# ============================================================
# DAY 4 — ARRAY ROTATION & REARRANGEMENT
# Programs 16–20
# ============================================================


# ------------------------------------------------------------
# 16. Left Rotate Array by K Positions
# ------------------------------------------------------------

def left_rotate_k():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter K: "))

    if n == 0:
        print("Array is empty.")
        return

    k = k % n

    # Reverse first K elements
    left = 0
    right = k - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    # Reverse remaining elements
    left = k
    right = n - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    # Reverse the complete array
    left = 0
    right = n - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    print("Array after left rotation:", arr)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 17. Right Rotate Array by K Positions
# ------------------------------------------------------------

def right_rotate_k():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter K: "))

    if n == 0:
        print("Array is empty.")
        return

    k = k % n

    # Reverse complete array
    left = 0
    right = n - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    # Reverse first K elements
    left = 0
    right = k - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    # Reverse remaining elements
    left = k
    right = n - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    print("Array after right rotation:", arr)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 18. Reverse Array in Groups of K
# ------------------------------------------------------------

def reverse_groups():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter K: "))

    if n == 0:
        print("Array is empty.")
        return

    if k <= 0:
        print("K must be greater than 0.")
        return

    # Reverse every group of K
    for start in range(0, n, k):

        left = start
        right = min(start + k - 1, n - 1)

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    print("Array after reversing groups:", arr)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 19. Rearrange Positive and Negative Numbers
# ------------------------------------------------------------

def rearrange_positive_negative():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    # Partition negatives to the beginning
    position = 0

    for i in range(n):

        if arr[i] < 0:
            arr[position], arr[i] = arr[i], arr[position]
            position += 1

    print("Rearranged array:", arr)

    print("Negative numbers are placed before positive numbers.")
    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 20. Rearrange Array Alternately Using Maximum/Minimum
# ------------------------------------------------------------

def rearrange_max_min():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    if n == 0:
        print("Array is empty.")
        return

    # This method requires a sorted array.
    # Sort manually using selection sort so that
    # we understand the algorithm.

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    result = []

    left = 0
    right = n - 1

    while left <= right:

        if left == right:
            result.append(arr[left])
        else:
            result.append(arr[right])
            result.append(arr[left])

        left += 1
        right -= 1

    print("Original sorted array:", arr)
    print("Maximum-Minimum arrangement:", result)

    print("Time Complexity: O(N²)")
    print("Space Complexity: O(N)")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 65)
        print("       DAY 4 — ARRAY ROTATION & REARRANGEMENT")
        print("=" * 65)

        print("16. Left Rotate Array by K Positions")
        print("17. Right Rotate Array by K Positions")
        print("18. Reverse Array in Groups of K")
        print("19. Rearrange Positive and Negative Numbers")
        print("20. Rearrange Array Alternately Using Max/Min")
        print("21. Run All Programs")
        print("22. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "16":
            left_rotate_k()

        elif choice == "17":
            right_rotate_k()

        elif choice == "18":
            reverse_groups()

        elif choice == "19":
            rearrange_positive_negative()

        elif choice == "20":
            rearrange_max_min()

        elif choice == "21":

            print("\n========== PROGRAM 16 ==========")
            left_rotate_k()

            print("\n========== PROGRAM 17 ==========")
            right_rotate_k()

            print("\n========== PROGRAM 18 ==========")
            reverse_groups()

            print("\n========== PROGRAM 19 ==========")
            rearrange_positive_negative()

            print("\n========== PROGRAM 20 ==========")
            rearrange_max_min()

        elif choice == "22":
            print("\nDay 4 completed! 🚀")
            break

        else:
            print("Invalid choice. Please try again.")


main()