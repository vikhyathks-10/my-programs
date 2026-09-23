# ============================================================
# DAY 23 — TWO-POINTER PROBLEMS
# Programs 111–115
# ============================================================


# ------------------------------------------------------------
# PROGRAM 111 — Pair With Target Sum
# ------------------------------------------------------------

def pair_target_sum():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter sorted array: ").split()))

    target = int(input("Enter target sum: "))

    left = 0
    right = n - 1

    while left < right:

        current_sum = arr[left] + arr[right]

        if current_sum == target:

            print("Pair found:", arr[left], "and", arr[right])
            print("Sum:", current_sum)

            print("Time Complexity: O(N)")
            print("Space Complexity: O(1)")
            return

        elif current_sum < target:

            left += 1

        else:

            right -= 1

    print("No pair found.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 112 — Three Sum — Basic Version
# ------------------------------------------------------------

def three_sum_basic():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    target = int(input("Enter target sum: "))

    # Sort the array first
    arr.sort()

    found = False

    for i in range(n - 2):

        left = i + 1
        right = n - 1

        while left < right:

            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:

                print(
                    "Triplet found:",
                    arr[i],
                    arr[left],
                    arr[right]
                )

                found = True

                # Move both pointers
                left += 1
                right -= 1

            elif current_sum < target:

                left += 1

            else:

                right -= 1

    if not found:
        print("No triplet found.")

    print("Time Complexity: O(N²)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# PROGRAM 113 — Container With Most Water
# ------------------------------------------------------------

def container_most_water():

    n = int(input("Enter N: "))
    height = list(map(int, input("Enter heights: ").split()))

    left = 0
    right = n - 1

    max_area = 0

    while left < right:

        width = right - left

        current_height = min(height[left], height[right])

        area = width * current_height

        if area > max_area:
            max_area = area

        # Move the pointer with smaller height
        if height[left] < height[right]:

            left += 1

        else:

            right -= 1

    print("Maximum water area:", max_area)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 114 — Merge Two Sorted Arrays Using Two Pointers
# ------------------------------------------------------------

def merge_sorted_arrays():

    n = int(input("Enter size of first array: "))
    arr1 = list(map(int, input("Enter first sorted array: ").split()))

    m = int(input("Enter size of second array: "))
    arr2 = list(map(int, input("Enter second sorted array: ").split()))

    result = []

    left = 0
    right = 0

    while left < n and right < m:

        if arr1[left] <= arr2[right]:

            result.append(arr1[left])
            left += 1

        else:

            result.append(arr2[right])
            right += 1

    # Remaining elements from first array
    while left < n:

        result.append(arr1[left])
        left += 1

    # Remaining elements from second array
    while right < m:

        result.append(arr2[right])
        right += 1

    print("Merged sorted array:", result)

    print("Time Complexity: O(N + M)")
    print("Space Complexity: O(N + M)")


# ------------------------------------------------------------
# PROGRAM 115 — Find Closest Pair to a Target
# ------------------------------------------------------------

def closest_pair():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter sorted array: ").split()))

    target = int(input("Enter target: "))

    left = 0
    right = n - 1

    best_left = 0
    best_right = n - 1

    smallest_difference = abs(
        arr[left] + arr[right] - target
    )

    while left < right:

        current_sum = arr[left] + arr[right]

        current_difference = abs(current_sum - target)

        if current_difference < smallest_difference:

            smallest_difference = current_difference

            best_left = left
            best_right = right

        if current_sum < target:

            left += 1

        elif current_sum > target:

            right -= 1

        else:

            # Exact target found
            best_left = left
            best_right = right
            break

    print(
        "Closest pair:",
        arr[best_left],
        "and",
        arr[best_right]
    )

    print(
        "Pair sum:",
        arr[best_left] + arr[best_right]
    )

    print(
        "Difference from target:",
        abs(arr[best_left] + arr[best_right] - target)
    )

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main():

    while True:

        print("\n" + "=" * 65)
        print("              DAY 23 — TWO-POINTER PROBLEMS")
        print("=" * 65)

        print("111. Pair With Target Sum")
        print("112. Three Sum — Basic Version")
        print("113. Container With Most Water")
        print("114. Merge Two Sorted Arrays Using Two Pointers")
        print("115. Find Closest Pair to a Target")
        print("116. Run All Programs")
        print("117. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "111":

            print("\n========== PROGRAM 111 ==========")
            pair_target_sum()

        elif choice == "112":

            print("\n========== PROGRAM 112 ==========")
            three_sum_basic()

        elif choice == "113":

            print("\n========== PROGRAM 113 ==========")
            container_most_water()

        elif choice == "114":

            print("\n========== PROGRAM 114 ==========")
            merge_sorted_arrays()

        elif choice == "115":

            print("\n========== PROGRAM 115 ==========")
            closest_pair()

        elif choice == "116":

            print("\n========== PROGRAM 111 ==========")
            pair_target_sum()

            print("\n========== PROGRAM 112 ==========")
            three_sum_basic()

            print("\n========== PROGRAM 113 ==========")
            container_most_water()

            print("\n========== PROGRAM 114 ==========")
            merge_sorted_arrays()

            print("\n========== PROGRAM 115 ==========")
            closest_pair()

        elif choice == "117":

            print("\n🎉 DAY 23 COMPLETED!")
            print("Programs 111–115 completed.")
            print("Total DSA programs completed: 115")
            break

        else:

            print("❌ Invalid choice. Please try again.")


# Start program
main()