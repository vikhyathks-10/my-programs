# DAY 26 - PREFIX SUM
# Programs 126 - 130


# ---------------------------------------------------------
# 126. Build Prefix-Sum Array
# ---------------------------------------------------------
def build_prefix_sum():
    arr = list(map(int, input("Enter array elements: ").split()))

    prefix = [0] * len(arr)

    if len(arr) > 0:
        prefix[0] = arr[0]

        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] + arr[i]

    print("Original array :", arr)
    print("Prefix sum     :", prefix)

    print("Complexity: O(N) time, O(N) space")


# ---------------------------------------------------------
# 127. Range Sum Queries
# ---------------------------------------------------------
def range_sum_queries():
    arr = list(map(int, input("Enter array elements: ").split()))

    n = len(arr)

    if n == 0:
        print("Array is empty.")
        return

    # Build prefix sum
    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    q = int(input("Enter number of queries: "))

    for _ in range(q):

        left, right = map(
            int,
            input("Enter left and right indices: ").split()
        )

        if left < 0 or right >= n or left > right:
            print("Invalid range.")
            continue

        if left == 0:
            result = prefix[right]
        else:
            result = prefix[right] - prefix[left - 1]

        print(f"Sum from index {left} to {right}: {result}")

    print("Prefix construction: O(N)")
    print("Each query: O(1)")
    print("Total: O(N + Q) time, O(N) space")


# ---------------------------------------------------------
# 128. Find Subarray With Given Sum
# ---------------------------------------------------------
def subarray_with_given_sum():
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target sum: "))

    prefix_sum = 0

    # Stores prefix_sum -> index
    seen = {0: -1}

    for i in range(len(arr)):

        prefix_sum += arr[i]

        required = prefix_sum - target

        if required in seen:
            start = seen[required] + 1
            end = i

            print("Subarray found.")
            print("Start index:", start)
            print("End index  :", end)
            print("Subarray   :", arr[start:end + 1])

            print("Complexity: O(N) average time, O(N) space")
            return

        if prefix_sum not in seen:
            seen[prefix_sum] = i

    print("No subarray with the given sum exists.")

    print("Complexity: O(N) average time, O(N) space")


# ---------------------------------------------------------
# 129. Count Subarrays With Sum K
# ---------------------------------------------------------
def count_subarrays_sum_k():
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter K: "))

    prefix_sum = 0
    count = 0

    # prefix_sum -> frequency
    frequency = {0: 1}

    for value in arr:

        prefix_sum += value

        required = prefix_sum - k

        if required in frequency:
            count += frequency[required]

        frequency[prefix_sum] = frequency.get(prefix_sum, 0) + 1

    print("Number of subarrays with sum", k, ":", count)

    print("Complexity: O(N) average time, O(N) space")


# ---------------------------------------------------------
# 130. Equilibrium Index Using Prefix Sums
# ---------------------------------------------------------
def equilibrium_index():
    arr = list(map(int, input("Enter array elements: ").split()))

    total_sum = sum(arr)
    left_sum = 0

    equilibrium_indices = []

    for i in range(len(arr)):

        # Remove current element from total
        # What remains is the right-side sum
        right_sum = total_sum - left_sum - arr[i]

        if left_sum == right_sum:
            equilibrium_indices.append(i)

        left_sum += arr[i]

    if equilibrium_indices:
        print("Equilibrium index/indices:", equilibrium_indices)
    else:
        print("No equilibrium index found.")

    print("Complexity: O(N) time, O(1) extra space")


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main():

    while True:

        print("\n==========================================")
        print("       DAY 26 - PREFIX SUM")
        print("==========================================")
        print("126. Build prefix-sum array")
        print("127. Range sum queries")
        print("128. Find subarray with given sum")
        print("129. Count subarrays with sum K")
        print("130. Find equilibrium index using prefix sums")
        print("131. Run All Programs")
        print("132. Exit")
        print("==========================================")

        choice = int(input("Enter your choice: "))

        if choice == 126:
            build_prefix_sum()

        elif choice == 127:
            range_sum_queries()

        elif choice == 128:
            subarray_with_given_sum()

        elif choice == 129:
            count_subarrays_sum_k()

        elif choice == 130:
            equilibrium_index()

        elif choice == 131:
            print("\nRunning all Day 26 programs...\n")

            build_prefix_sum()
            range_sum_queries()
            subarray_with_given_sum()
            count_subarrays_sum_k()
            equilibrium_index()

        elif choice == 132:
            print("Exiting Day 26. Keep going! 🔥")
            break

        else:
            print("Invalid choice. Please try again.")


# Program starts here
if __name__ == "__main__":
    main()