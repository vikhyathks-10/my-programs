# ============================================================
# DAY 15 — BUBBLE & SELECTION SORT
# Programs 71–75
# ============================================================


# ------------------------------------------------------------
# PROGRAM 71 — Bubble Sort
# ------------------------------------------------------------

def bubble_sort():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Sorted array:", arr)

    print("Time Complexity: O(N²)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 72 — Optimized Bubble Sort
# ------------------------------------------------------------

def optimized_bubble_sort():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swap happened, array is already sorted
        if not swapped:
            break

    print("Sorted array:", arr)

    print("Best Case Time Complexity: O(N)")
    print("Worst Case Time Complexity: O(N²)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 73 — Selection Sort
# ------------------------------------------------------------

def selection_sort():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    print("Sorted array:", arr)

    print("Time Complexity: O(N²)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 74 — Sort Array in Descending Order
# ------------------------------------------------------------

def descending_sort():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    # Selection sort in descending order
    for i in range(n - 1):

        max_index = i

        for j in range(i + 1, n):

            if arr[j] > arr[max_index]:
                max_index = j

        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]

    print("Array in descending order:", arr)

    print("Time Complexity: O(N²)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 75 — Count Swaps in Bubble Sort
# ------------------------------------------------------------

def count_bubble_swaps():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    swap_count = 0

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swap_count += 1
                swapped = True

        if not swapped:
            break

    print("Sorted array:", arr)
    print("Number of swaps:", swap_count)

    print("Best Case Time Complexity: O(N)")
    print("Worst Case Time Complexity: O(N²)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main():

    while True:

        print("\n" + "=" * 65)
        print("              DAY 15 — BUBBLE & SELECTION SORT")
        print("=" * 65)

        print("71. Bubble Sort")
        print("72. Optimized Bubble Sort")
        print("73. Selection Sort")
        print("74. Sort Array in Descending Order")
        print("75. Count Swaps in Bubble Sort")
        print("76. Run All Programs")
        print("77. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "71":

            print("\n========== PROGRAM 71 ==========")
            bubble_sort()

        elif choice == "72":

            print("\n========== PROGRAM 72 ==========")
            optimized_bubble_sort()

        elif choice == "73":

            print("\n========== PROGRAM 73 ==========")
            selection_sort()

        elif choice == "74":

            print("\n========== PROGRAM 74 ==========")
            descending_sort()

        elif choice == "75":

            print("\n========== PROGRAM 75 ==========")
            count_bubble_swaps()

        elif choice == "76":

            print("\n========== PROGRAM 71 ==========")
            bubble_sort()

            print("\n========== PROGRAM 72 ==========")
            optimized_bubble_sort()

            print("\n========== PROGRAM 73 ==========")
            selection_sort()

            print("\n========== PROGRAM 74 ==========")
            descending_sort()

            print("\n========== PROGRAM 75 ==========")
            count_bubble_swaps()

        elif choice == "77":

            print("\n🎉 DAY 15 COMPLETED!")
            print("Programs 71–75 completed.")
            break

        else:

            print("❌ Invalid choice. Please try again.")


# Start program
main()