# 🔹 DAY 10 - SLIDING WINDOW PROBLEMS


# ==================================================
# 🔹 1. Sliding Window Maximum
# ==================================================

def sliding_window_maximum(arr, k):

    result = []

    for i in range(len(arr) - k + 1):

        result.append(max(arr[i:i + k]))

    return result


# ==================================================
# 🔹 2. Sliding Window Sum
# ==================================================

def sliding_window_sum(arr, k):

    result = []

    window_sum = sum(arr[:k])

    result.append(window_sum)

    for i in range(k, len(arr)):

        window_sum += arr[i] - arr[i - k]

        result.append(window_sum)

    return result


# ==================================================
# 🔹 3. Fixed Size Window Average
# ==================================================

def fixed_window_average(arr, k):

    result = []

    window_sum = sum(arr[:k])

    result.append(window_sum / k)

    for i in range(k, len(arr)):

        window_sum += arr[i] - arr[i - k]

        result.append(window_sum / k)

    return result


# ==================================================
# 🔹 4. Maximum Consecutive Ones
# ==================================================

def maximum_consecutive_ones(arr):

    max_count = 0
    current_count = 0

    for num in arr:

        if num == 1:

            current_count += 1

            max_count = max(max_count,
                            current_count)

        else:

            current_count = 0

    return max_count


# ==================================================
# 🔹 5. Longest Unique Substring
# ==================================================

def longest_unique_substring(s):

    left = 0

    seen = {}

    max_length = 0

    for right in range(len(s)):

        if s[right] in seen and seen[s[right]] >= left:

            left = seen[s[right]] + 1

        seen[s[right]] = right

        max_length = max(
            max_length,
            right - left + 1
        )

    return max_length


# ==================================================
# 🔹 MAIN PROGRAM
# ==================================================

arr = [1, 3, -1, -3, 5, 3, 6, 7]

print("Array:")
print(arr)


print("\n🔹 Sliding Window Maximum (k=3)")
print(sliding_window_maximum(arr, 3))


print("\n🔹 Sliding Window Sum (k=3)")
print(sliding_window_sum(arr, 3))


print("\n🔹 Fixed Size Window Average (k=3)")
print(fixed_window_average(arr, 3))


print("\n🔹 Maximum Consecutive Ones")

binary_arr = [1, 1, 0, 1, 1, 1, 0, 1]

print(maximum_consecutive_ones(binary_arr))


print("\n🔹 Longest Unique Substring")

print(
    longest_unique_substring(
        "abcabcbb"
    )
)