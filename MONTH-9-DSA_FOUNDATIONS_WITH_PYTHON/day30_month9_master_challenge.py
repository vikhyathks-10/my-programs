# =========================================================
# DAY 30 - MONTH 9 DSA MASTER CHALLENGE
# Programs 146 - 150
# =========================================================


# ---------------------------------------------------------
# 146. Two Sum
# ---------------------------------------------------------
def two_sum():
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target: "))

    seen = {}

    for i in range(len(arr)):

        required = target - arr[i]

        if required in seen:
            print("Pair found!")
            print("Indices:", seen[required], i)
            print("Values:", required, arr[i])
            print("Complexity: O(N) average time, O(N) space")
            return

        seen[arr[i]] = i

    print("No pair found.")
    print("Complexity: O(N) average time, O(N) space")


# ---------------------------------------------------------
# 147. Maximum Subarray
# ---------------------------------------------------------
def maximum_subarray():
    arr = list(map(int, input("Enter array elements: ").split()))

    if not arr:
        print("Array is empty.")
        return

    current_sum = arr[0]
    max_sum = arr[0]

    start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(arr)):

        # Decide whether to:
        # 1. Continue current subarray
        # 2. Start a new subarray

        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start
            best_end = i

    print("Maximum subarray sum:", max_sum)
    print("Maximum subarray:", arr[best_start:best_end + 1])

    print("Complexity: O(N) time, O(1) extra space")


# ---------------------------------------------------------
# 148. Longest Substring Without Repeating Characters
# ---------------------------------------------------------
def longest_unique_substring():
    s = input("Enter a string: ")

    seen = set()

    left = 0
    max_length = 0
    best_start = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length
            best_start = left

    best_substring = s[best_start:best_start + max_length]

    print("Longest substring:", best_substring)
    print("Length:", max_length)

    print("Complexity: O(N) time, O(K) space")


# ---------------------------------------------------------
# 149. Subarray Sum Equals K
# ---------------------------------------------------------
def subarray_sum_k():
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
# 150. Search in Rotated Sorted Array
# ---------------------------------------------------------
def search_rotated_array():
    arr = list(map(int, input("Enter rotated sorted array: ").split()))
    target = int(input("Enter target: "))

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        # Target found
        if arr[mid] == target:
            print("Target found at index:", mid)
            print("Complexity: O(log N) time, O(1) space")
            return

        # Left half is sorted
        if arr[left] <= arr[mid]:

            # Target lies inside sorted left half
            if arr[left] <= target < arr[mid]:
                right = mid - 1

            else:
                left = mid + 1

        # Right half is sorted
        else:

            # Target lies inside sorted right half
            if arr[mid] < target <= arr[right]:
                left = mid + 1

            else:
                right = mid - 1

    print("Target not found.")
    print("Complexity: O(log N) time, O(1) space")


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main():

    while True:

        print("\n================================================")
        print("       DAY 30 - MONTH 9 MASTER CHALLENGE")
        print("================================================")
        print("146. Two Sum")
        print("147. Maximum Subarray")
        print("148. Longest Substring Without Repeating Characters")
        print("149. Subarray Sum Equals K")
        print("150. Search in Rotated Sorted Array")
        print("151. Run All Programs")
        print("152. Exit")
        print("================================================")

        choice = int(input("Enter your choice: "))

        if choice == 146:
            two_sum()

        elif choice == 147:
            maximum_subarray()

        elif choice == 148:
            longest_unique_substring()

        elif choice == 149:
            subarray_sum_k()

        elif choice == 150:
            search_rotated_array()

        elif choice == 151:
            print("\nRunning all Day 30 programs...\n")

            two_sum()
            maximum_subarray()
            longest_unique_substring()
            subarray_sum_k()
            search_rotated_array()

        elif choice == 152:
            print("\n🏆 Month 9 DSA Master Challenge Complete!")
            print("150 DSA programs completed! 🔥")
            break

        else:
            print("Invalid choice. Please try again.")


# ---------------------------------------------------------
# PROGRAM START
# ---------------------------------------------------------
if __name__ == "__main__":
    main()