# DAY 27 - PREFIX SUM PROBLEMS
# Programs 131 - 135


# ---------------------------------------------------------
# 131. Maximum Subarray Sum Using Prefix Concepts
# ---------------------------------------------------------
def maximum_subarray_prefix():
    arr = list(map(int, input("Enter array elements: ").split()))

    if not arr:
        print("Array is empty.")
        return

    prefix_sum = 0
    minimum_prefix = 0

    max_sum = float("-inf")

    for value in arr:
        prefix_sum += value

        current_sum = prefix_sum - minimum_prefix
        max_sum = max(max_sum, current_sum)

        minimum_prefix = min(minimum_prefix, prefix_sum)

    print("Maximum subarray sum:", max_sum)
    print("Complexity: O(N) time, O(1) space")


# ---------------------------------------------------------
# 132. Minimum Subarray Sum
# ---------------------------------------------------------
def minimum_subarray_sum():
    arr = list(map(int, input("Enter array elements: ").split()))

    if not arr:
        print("Array is empty.")
        return

    prefix_sum = 0
    maximum_prefix = 0

    min_sum = float("inf")

    for value in arr:
        prefix_sum += value

        current_sum = prefix_sum - maximum_prefix
        min_sum = min(min_sum, current_sum)

        maximum_prefix = max(maximum_prefix, prefix_sum)

    print("Minimum subarray sum:", min_sum)
    print("Complexity: O(N) time, O(1) space")


# ---------------------------------------------------------
# 133. Find Longest Subarray With Sum K
# ---------------------------------------------------------
def longest_subarray_sum_k():
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter K: "))

    prefix_sum = 0
    max_length = 0

    # Stores first occurrence of each prefix sum
    first_occurrence = {0: -1}

    for i in range(len(arr)):

        prefix_sum += arr[i]

        required = prefix_sum - k

        if required in first_occurrence:
            length = i - first_occurrence[required]
            max_length = max(max_length, length)

        # Store ONLY the first occurrence.
        # The earliest index gives the longest subarray.
        if prefix_sum not in first_occurrence:
            first_occurrence[prefix_sum] = i

    if max_length == 0:
        print("No subarray with sum K found.")
    else:
        print("Longest subarray length:", max_length)

    print("Complexity: O(N) average time, O(N) space")


# ---------------------------------------------------------
# 134. Count Zero-Sum Subarrays
# ---------------------------------------------------------
def count_zero_sum_subarrays():
    arr = list(map(int, input("Enter array elements: ").split()))

    prefix_sum = 0
    count = 0

    # Prefix sum 0 exists before starting
    frequency = {0: 1}

    for value in arr:

        prefix_sum += value

        if prefix_sum in frequency:
            count += frequency[prefix_sum]

        frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

    print("Number of zero-sum subarrays:", count)

    print("Complexity: O(N) average time, O(N) space")


# ---------------------------------------------------------
# 135. Range Update Using Difference Array
# ---------------------------------------------------------
def range_update_difference_array():
    n = int(input("Enter array size: "))

    arr = list(map(int, input("Enter array elements: ").split()))

    if len(arr) != n:
        print("Number of elements does not match array size.")
        return

    q = int(input("Enter number of range updates: "))

    # Difference array
    diff = [0] * (n + 1)

    for query in range(q):

        left, right, value = map(
            int,
            input(
                "Enter left index, right index and value: "
            ).split()
        )

        if left < 0 or right >= n or left > right:
            print("Invalid range.")
            continue

        # Start adding value at left
        diff[left] += value

        # Stop adding value after right
        if right + 1 < n:
            diff[right + 1] -= value

    # Apply difference array using prefix sum
    current_addition = 0

    for i in range(n):
        current_addition += diff[i]
        arr[i] += current_addition

    print("Array after all range updates:")
    print(arr)

    print("Complexity: O(N + Q) time, O(N) space")


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main():

    while True:

        print("\n==========================================")
        print("      DAY 27 - PREFIX SUM PROBLEMS")
        print("==========================================")
        print("131. Maximum subarray sum using prefix concepts")
        print("132. Minimum subarray sum")
        print("133. Find longest subarray with sum K")
        print("134. Count zero-sum subarrays")
        print("135. Range update using difference array")
        print("136. Run All Programs")
        print("137. Exit")
        print("==========================================")

        choice = int(input("Enter your choice: "))

        if choice == 131:
            maximum_subarray_prefix()

        elif choice == 132:
            minimum_subarray_sum()

        elif choice == 133:
            longest_subarray_sum_k()

        elif choice == 134:
            count_zero_sum_subarrays()

        elif choice == 135:
            range_update_difference_array()

        elif choice == 136:
            print("\nRunning all Day 27 programs...\n")

            maximum_subarray_prefix()
            minimum_subarray_sum()
            longest_subarray_sum_k()
            count_zero_sum_subarrays()
            range_update_difference_array()

        elif choice == 137:
            print("Exiting Day 27. Keep grinding! 🔥")
            break

        else:
            print("Invalid choice. Please try again.")


# Program starts here
if __name__ == "__main__":
    main()