# ============================================================
# DAY 17 — MERGE SORT
# Programs 81–85
# ============================================================


# ------------------------------------------------------------
# PROGRAM 81 — Implement Merge Sort
# ------------------------------------------------------------

def merge_sort_program():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    def merge_sort(arr):

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    def merge(left, right):

        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add remaining elements
        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    arr = merge_sort(arr)

    print("Sorted array:", arr)

    print("Time Complexity: O(N log N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# PROGRAM 82 — Merge Two Sorted Arrays
# ------------------------------------------------------------

def merge_two_sorted_arrays():

    n = int(input("Enter size of first array: "))
    arr1 = list(map(int, input("Enter first sorted array: ").split()))

    m = int(input("Enter size of second array: "))
    arr2 = list(map(int, input("Enter second sorted array: ").split()))

    result = []

    i = 0
    j = 0

    while i < n and j < m:

        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Remaining elements from first array
    while i < n:
        result.append(arr1[i])
        i += 1

    # Remaining elements from second array
    while j < m:
        result.append(arr2[j])
        j += 1

    print("Merged sorted array:", result)

    print("Time Complexity: O(N + M)")
    print("Space Complexity: O(N + M)")


# ------------------------------------------------------------
# PROGRAM 83 — Find Intersection Using Sorted Arrays
# ------------------------------------------------------------

def intersection_sorted_arrays():

    n = int(input("Enter size of first array: "))
    arr1 = list(map(int, input("Enter first sorted array: ").split()))

    m = int(input("Enter size of second array: "))
    arr2 = list(map(int, input("Enter second sorted array: ").split()))

    i = 0
    j = 0

    intersection = []

    while i < n and j < m:

        if arr1[i] < arr2[j]:
            i += 1

        elif arr1[i] > arr2[j]:
            j += 1

        else:
            # Avoid duplicate values in result
            if not intersection or intersection[-1] != arr1[i]:
                intersection.append(arr1[i])

            i += 1
            j += 1

    print("Intersection:", intersection)

    print("Time Complexity: O(N + M)")
    print("Space Complexity: O(K)")
    print("K = number of unique common elements")


# ------------------------------------------------------------
# PROGRAM 84 — Count Inversions Using Merge Sort
# ------------------------------------------------------------

def count_inversions():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    def merge_and_count(left, right):

        result = []

        i = 0
        j = 0
        inversions = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:

                result.append(left[i])
                i += 1

            else:

                result.append(right[j])

                # Every remaining element in left
                # forms an inversion with right[j]
                inversions += len(left) - i

                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result, inversions

    def merge_sort_and_count(arr):

        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2

        left, left_count = merge_sort_and_count(arr[:mid])
        right, right_count = merge_sort_and_count(arr[mid:])

        merged, cross_count = merge_and_count(left, right)

        total_count = left_count + right_count + cross_count

        return merged, total_count

    sorted_arr, inversion_count = merge_sort_and_count(arr)

    print("Sorted array:", sorted_arr)
    print("Number of inversions:", inversion_count)

    print("Time Complexity: O(N log N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# PROGRAM 85 — Find Smaller Elements on the Right
# ------------------------------------------------------------

def smaller_elements_on_right():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    # Each item stores:
    # [value, original_index]
    items = []

    for i in range(n):
        items.append([arr[i], i])

    counts = [0] * n

    def merge_sort(left, right):

        if right - left <= 1:
            return

        mid = (left + right) // 2

        merge_sort(left, mid)
        merge_sort(mid, right)

        merge(left, mid, right)

    def merge(left, mid, right):

        temp = []

        i = left
        j = mid

        # Number of right-side elements already placed
        # before the current left element
        smaller_count = 0

        while i < mid and j < right:

            if items[j][0] < items[i][0]:

                temp.append(items[j])
                smaller_count += 1
                j += 1

            else:

                counts[items[i][1]] += smaller_count
                temp.append(items[i])
                i += 1

        # Remaining left elements
        while i < mid:

            counts[items[i][1]] += smaller_count
            temp.append(items[i])
            i += 1

        # Remaining right elements
        while j < right:

            temp.append(items[j])
            j += 1

        # Copy merged values back
        for k in range(len(temp)):
            items[left + k] = temp[k]

    merge_sort(0, n)

    print("Original array:", arr)
    print("Smaller elements on the right:", counts)

    print("Time Complexity: O(N log N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main():

    while True:

        print("\n" + "=" * 65)
        print("                  DAY 17 — MERGE SORT")
        print("=" * 65)

        print("81. Implement Merge Sort")
        print("82. Merge Two Sorted Arrays")
        print("83. Find Intersection Using Sorted Arrays")
        print("84. Count Inversions Using Merge Sort")
        print("85. Find Smaller Elements on the Right")
        print("86. Run All Programs")
        print("87. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "81":

            print("\n========== PROGRAM 81 ==========")
            merge_sort_program()

        elif choice == "82":

            print("\n========== PROGRAM 82 ==========")
            merge_two_sorted_arrays()

        elif choice == "83":

            print("\n========== PROGRAM 83 ==========")
            intersection_sorted_arrays()

        elif choice == "84":

            print("\n========== PROGRAM 84 ==========")
            count_inversions()

        elif choice == "85":

            print("\n========== PROGRAM 85 ==========")
            smaller_elements_on_right()

        elif choice == "86":

            print("\n========== PROGRAM 81 ==========")
            merge_sort_program()

            print("\n========== PROGRAM 82 ==========")
            merge_two_sorted_arrays()

            print("\n========== PROGRAM 83 ==========")
            intersection_sorted_arrays()

            print("\n========== PROGRAM 84 ==========")
            count_inversions()

            print("\n========== PROGRAM 85 ==========")
            smaller_elements_on_right()

        elif choice == "87":

            print("\n🎉 DAY 17 COMPLETED!")
            print("Programs 81–85 completed.")
            break

        else:

            print("❌ Invalid choice. Please try again.")


# Start program
main()