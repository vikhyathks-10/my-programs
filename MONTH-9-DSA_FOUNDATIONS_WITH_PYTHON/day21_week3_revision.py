# ============================================================
# DAY 21 — WEEK 3 REVISION
# Programs 101–105
# ============================================================


# ------------------------------------------------------------
# PROGRAM 101 — Sort Array Containing Only 0s and 1s
# ------------------------------------------------------------

def sort_zeros_ones():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array containing only 0s and 1s: ").split()))

    left = 0
    right = n - 1

    while left < right:

        # Find 1 from the left
        while left < right and arr[left] == 0:
            left += 1

        # Find 0 from the right
        while left < right and arr[right] == 1:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

    print("Sorted array:", arr)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 102 — Sort Array Containing 0s, 1s and 2s
# ------------------------------------------------------------

def sort_zeros_ones_twos():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array containing 0s, 1s and 2s: ").split()))

    low = 0
    mid = 0
    high = n - 1

    # Dutch National Flag Algorithm
    while mid <= high:

        if arr[mid] == 0:

            arr[low], arr[mid] = arr[mid], arr[low]

            low += 1
            mid += 1

        elif arr[mid] == 1:

            mid += 1

        else:

            arr[mid], arr[high] = arr[high], arr[mid]

            high -= 1

    print("Sorted array:", arr)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 103 — Find K-th Largest Element
# ------------------------------------------------------------

def kth_largest():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    k = int(input("Enter K: "))

    if k < 1 or k > n:

        print("Invalid K.")
        return

    # Quickselect using a partition based on largest side
    def partition(low, high):

        pivot = arr[high]

        i = low - 1

        for j in range(low, high):

            if arr[j] <= pivot:

                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    target_index = n - k

    low = 0
    high = n - 1

    while low <= high:

        pivot_index = partition(low, high)

        if pivot_index == target_index:

            print(f"{k}-th largest element:", arr[pivot_index])

            print("Average Time Complexity: O(N)")
            print("Worst Case Time Complexity: O(N²)")
            print("Space Complexity: O(1)")
            return

        elif pivot_index < target_index:

            low = pivot_index + 1

        else:

            high = pivot_index - 1


# ------------------------------------------------------------
# PROGRAM 104 — Find Duplicate Using Hashing
# ------------------------------------------------------------

def duplicate_using_hashing():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    seen = set()

    duplicates = []

    for value in arr:

        if value in seen:

            if value not in duplicates:
                duplicates.append(value)

        else:

            seen.add(value)

    if len(duplicates) == 0:

        print("No duplicate elements found.")

    else:

        print("Duplicate elements:", duplicates)

    print("Average Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# PROGRAM 105 — Find Two Pairs With the Same Sum
# ------------------------------------------------------------

def two_pairs_same_sum():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    # Dictionary:
    # sum -> pair of elements
    pair_sum = {}

    found = False

    for i in range(n):

        for j in range(i + 1, n):

            current_sum = arr[i] + arr[j]

            if current_sum in pair_sum:

                previous_pair = pair_sum[current_sum]

                # Make sure all four indices are different
                if (previous_pair[0] != i and
                    previous_pair[0] != j and
                    previous_pair[1] != i and
                    previous_pair[1] != j):

                    print("Two pairs with the same sum found:")

                    print(
                        "Pair 1:",
                        previous_pair[2],
                        "+",
                        previous_pair[3],
                        "=",
                        current_sum
                    )

                    print(
                        "Pair 2:",
                        arr[i],
                        "+",
                        arr[j],
                        "=",
                        current_sum
                    )

                    found = True
                    break

            else:

                pair_sum[current_sum] = (
                    i,
                    j,
                    arr[i],
                    arr[j]
                )

        if found:
            break

    if not found:

        print("No two pairs with the same sum found.")

    print("Average Time Complexity: O(N²)")
    print("Space Complexity: O(N²)")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main():

    while True:

        print("\n" + "=" * 65)
        print("               DAY 21 — WEEK 3 REVISION")
        print("=" * 65)

        print("101. Sort Array Containing Only 0s and 1s")
        print("102. Sort Array Containing 0s, 1s and 2s")
        print("103. Find K-th Largest Element")
        print("104. Find Duplicate Using Hashing")
        print("105. Find Two Pairs With the Same Sum")
        print("106. Run All Programs")
        print("107. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "101":

            print("\n========== PROGRAM 101 ==========")
            sort_zeros_ones()

        elif choice == "102":

            print("\n========== PROGRAM 102 ==========")
            sort_zeros_ones_twos()

        elif choice == "103":

            print("\n========== PROGRAM 103 ==========")
            kth_largest()

        elif choice == "104":

            print("\n========== PROGRAM 104 ==========")
            duplicate_using_hashing()

        elif choice == "105":

            print("\n========== PROGRAM 105 ==========")
            two_pairs_same_sum()

        elif choice == "106":

            print("\n========== PROGRAM 101 ==========")
            sort_zeros_ones()

            print("\n========== PROGRAM 102 ==========")
            sort_zeros_ones_twos()

            print("\n========== PROGRAM 103 ==========")
            kth_largest()

            print("\n========== PROGRAM 104 ==========")
            duplicate_using_hashing()

            print("\n========== PROGRAM 105 ==========")
            two_pairs_same_sum()

        elif choice == "107":

            print("\n🎉 WEEK 3 COMPLETED!")
            print("Programs 101–105 completed.")
            print("Total DSA programs completed: 105")
            break

        else:

            print("❌ Invalid choice. Please try again.")


# Start program
main()