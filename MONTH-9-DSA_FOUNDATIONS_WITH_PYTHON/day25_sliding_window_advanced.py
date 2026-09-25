# DAY 25 - Sliding Window Advanced
# Programs 121 - 125


# ---------------------------------------------------------
# 121. Longest Substring Without Repeating Characters
# ---------------------------------------------------------
def longest_unique_substring():
    s = input("Enter a string: ")

    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        current_length = right - left + 1
        max_length = max(max_length, current_length)

    print("Longest substring length:", max_length)
    print("Complexity: O(N) time, O(K) space")


# ---------------------------------------------------------
# 122. Longest Substring With At Most K Distinct Characters
# ---------------------------------------------------------
def longest_k_distinct():
    s = input("Enter a string: ")
    k = int(input("Enter K: "))

    frequency = {}
    left = 0
    max_length = 0

    for right in range(len(s)):

        frequency[s[right]] = frequency.get(s[right], 0) + 1

        while len(frequency) > k:
            frequency[s[left]] -= 1

            if frequency[s[left]] == 0:
                del frequency[s[left]]

            left += 1

        current_length = right - left + 1
        max_length = max(max_length, current_length)

    print("Longest substring length:", max_length)
    print("Complexity: O(N) time, O(K) space")


# ---------------------------------------------------------
# 123. Smallest Subarray With Sum >= K
# ---------------------------------------------------------
def smallest_subarray_sum():
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter K: "))

    left = 0
    window_sum = 0
    min_length = float("inf")

    for right in range(len(arr)):

        window_sum += arr[right]

        while window_sum >= k:
            current_length = right - left + 1
            min_length = min(min_length, current_length)

            window_sum -= arr[left]
            left += 1

    if min_length == float("inf"):
        print("No subarray found")
    else:
        print("Smallest subarray length:", min_length)

    print("Complexity: O(N) time, O(1) space")

    print("Note: This sliding-window method assumes non-negative elements.")


# ---------------------------------------------------------
# 124. Maximum Consecutive 1s
# ---------------------------------------------------------
def maximum_consecutive_ones():
    arr = list(map(int, input("Enter binary array: ").split()))

    left = 0
    zero_count = 0
    max_length = 0

    for right in range(len(arr)):

        if arr[right] == 0:
            zero_count += 1

        while zero_count > 0:
            if arr[left] == 0:
                zero_count -= 1

            left += 1

        current_length = right - left + 1
        max_length = max(max_length, current_length)

    print("Maximum consecutive 1s:", max_length)
    print("Complexity: O(N) time, O(1) space")


# ---------------------------------------------------------
# 125. Longest Subarray Containing At Most K Zeroes
# ---------------------------------------------------------
def longest_at_most_k_zeroes():
    arr = list(map(int, input("Enter binary array: ").split()))
    k = int(input("Enter maximum number of zeroes allowed: "))

    left = 0
    zero_count = 0
    max_length = 0

    for right in range(len(arr)):

        if arr[right] == 0:
            zero_count += 1

        while zero_count > k:
            if arr[left] == 0:
                zero_count -= 1

            left += 1

        current_length = right - left + 1
        max_length = max(max_length, current_length)

    print("Longest subarray length:", max_length)
    print("Complexity: O(N) time, O(1) space")


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main():

    while True:

        print("\n==========================================")
        print(" DAY 25 - SLIDING WINDOW ADVANCED")
        print("==========================================")
        print("121. Longest substring without repeating characters")
        print("122. Longest substring with at most K distinct characters")
        print("123. Smallest subarray with sum >= K")
        print("124. Maximum consecutive 1s")
        print("125. Longest subarray containing at most K zeroes")
        print("126. Run All Programs")
        print("127. Exit")
        print("==========================================")

        choice = int(input("Enter your choice: "))

        if choice == 121:
            longest_unique_substring()

        elif choice == 122:
            longest_k_distinct()

        elif choice == 123:
            smallest_subarray_sum()

        elif choice == 124:
            maximum_consecutive_ones()

        elif choice == 125:
            longest_at_most_k_zeroes()

        elif choice == 126:
            print("\nRunning all Day 25 programs...\n")

            longest_unique_substring()
            longest_k_distinct()
            smallest_subarray_sum()
            maximum_consecutive_ones()
            longest_at_most_k_zeroes()

        elif choice == 127:
            print("Exiting Day 25 program. Keep grinding! 🔥")
            break

        else:
            print("Invalid choice. Please try again.")


# Program starts here
if __name__ == "__main__":
    main()