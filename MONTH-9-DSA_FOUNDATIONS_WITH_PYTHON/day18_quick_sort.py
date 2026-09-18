# ============================================================
# DAY 18 — QUICK SORT
# Programs 86–90
# ============================================================


# ------------------------------------------------------------
# PROGRAM 86 — Implement Quick Sort
# ------------------------------------------------------------

def quick_sort():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    def partition(low, high):

        pivot = arr[high]

        i = low - 1

        for j in range(low, high):

            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    def sort(low, high):

        if low < high:

            pivot_index = partition(low, high)

            sort(low, pivot_index - 1)
            sort(pivot_index + 1, high)

    sort(0, n - 1)

    print("Sorted array:", arr)

    print("Average Time Complexity: O(N log N)")
    print("Worst Case Time Complexity: O(N²)")
    print("Average Space Complexity: O(log N)")
    print("Worst Case Space Complexity: O(N)")


# ------------------------------------------------------------
# PROGRAM 87 — Implement Partition
# ------------------------------------------------------------

def partition_program():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    low = 0
    high = n - 1

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:

            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    pivot_index = i + 1

    print("Array after partition:", arr)
    print("Pivot:", pivot)
    print("Pivot index:", pivot_index)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 88 — Quick Sort Using First Element as Pivot
# ------------------------------------------------------------

def quick_sort_first_pivot():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    def partition_first(low, high):

        pivot = arr[low]

        i = low + 1
        j = high

        while True:

            # Move i while elements are smaller than pivot
            while i <= high and arr[i] <= pivot:
                i += 1

            # Move j while elements are greater than pivot
            while j >= low + 1 and arr[j] > pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

            else:
                break

        # Put pivot in its correct position
        arr[low], arr[j] = arr[j], arr[low]

        return j

    def sort(low, high):

        if low < high:

            pivot_index = partition_first(low, high)

            sort(low, pivot_index - 1)
            sort(pivot_index + 1, high)

    sort(0, n - 1)

    print("Sorted array:", arr)

    print("Average Time Complexity: O(N log N)")
    print("Worst Case Time Complexity: O(N²)")
    print("Space Complexity: O(N) worst case")


# ------------------------------------------------------------
# PROGRAM 89 — Quick Sort Using Last Element as Pivot
# ------------------------------------------------------------

def quick_sort_last_pivot():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    def partition_last(low, high):

        pivot = arr[high]

        i = low - 1

        for j in range(low, high):

            if arr[j] <= pivot:

                i += 1

                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    def sort(low, high):

        if low < high:

            pivot_index = partition_last(low, high)

            sort(low, pivot_index - 1)
            sort(pivot_index + 1, high)

    sort(0, n - 1)

    print("Sorted array:", arr)

    print("Average Time Complexity: O(N log N)")
    print("Worst Case Time Complexity: O(N²)")
    print("Space Complexity: O(N) worst case")


# ------------------------------------------------------------
# PROGRAM 90 — K-th Smallest Element Using Partition
# ------------------------------------------------------------

def kth_smallest():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    k = int(input("Enter K: "))

    if k < 1 or k > n:

        print("Invalid K.")
        return

    def partition(low, high):

        pivot = arr[high]

        i = low - 1

        for j in range(low, high):

            if arr[j] <= pivot:

                i += 1

                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    low = 0
    high = n - 1

    target_index = k - 1

    while low <= high:

        pivot_index = partition(low, high)

        if pivot_index == target_index:

            print(f"{k}-th smallest element:", arr[pivot_index])

            print("Average Time Complexity: O(N)")
            print("Worst Case Time Complexity: O(N²)")
            print("Space Complexity: O(1)")
            return

        elif pivot_index > target_index:

            high = pivot_index - 1

        else:

            low = pivot_index + 1


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main():

    while True:

        print("\n" + "=" * 65)
        print("                   DAY 18 — QUICK SORT")
        print("=" * 65)

        print("86. Implement Quick Sort")
        print("87. Implement Partition")
        print("88. Quick Sort Using First Element as Pivot")
        print("89. Quick Sort Using Last Element as Pivot")
        print("90. Find K-th Smallest Using Partition Logic")
        print("91. Run All Programs")
        print("92. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "86":

            print("\n========== PROGRAM 86 ==========")
            quick_sort()

        elif choice == "87":

            print("\n========== PROGRAM 87 ==========")
            partition_program()

        elif choice == "88":

            print("\n========== PROGRAM 88 ==========")
            quick_sort_first_pivot()

        elif choice == "89":

            print("\n========== PROGRAM 89 ==========")
            quick_sort_last_pivot()

        elif choice == "90":

            print("\n========== PROGRAM 90 ==========")
            kth_smallest()

        elif choice == "91":

            print("\n========== PROGRAM 86 ==========")
            quick_sort()

            print("\n========== PROGRAM 87 ==========")
            partition_program()

            print("\n========== PROGRAM 88 ==========")
            quick_sort_first_pivot()

            print("\n========== PROGRAM 89 ==========")
            quick_sort_last_pivot()

            print("\n========== PROGRAM 90 ==========")
            kth_smallest()

        elif choice == "92":

            print("\n🎉 DAY 18 COMPLETED!")
            print("Programs 86–90 completed.")
            break

        else:

            print("❌ Invalid choice. Please try again.")


# Start program
main()