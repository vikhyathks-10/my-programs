# 🔹 DAY 14 - REVISION PRACTICE SET


# ==================================================
# 🔹 1. Find First Unique Element
# ==================================================

def first_unique_element(arr):

    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num in arr:

        if freq[num] == 1:
            return num

    return -1


# ==================================================
# 🔹 2. Longest Word In Sentence
# ==================================================

def longest_word(sentence):

    words = sentence.split()

    longest = ""

    for word in words:

        if len(word) > len(longest):
            longest = word

    return longest


# ==================================================
# 🔹 3. Binary Search
# ==================================================

def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# ==================================================
# 🔹 4. Maximum Sum Subarray
# ==================================================

def max_subarray_sum(arr):

    current_sum = arr[0]

    max_sum = arr[0]

    for i in range(1, len(arr)):

        current_sum = max(
            arr[i],
            current_sum + arr[i]
        )

        max_sum = max(
            max_sum,
            current_sum
        )

    return max_sum


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

print("🔹 Revision Problem 1")
print(first_unique_element(
    [1, 2, 2, 3, 3, 4, 5, 5]
))


print("\n🔹 Revision Problem 2")
print(longest_word(
    "Python programming is very powerful"
))


print("\n🔹 Revision Problem 3")
print(binary_search(
    [10, 20, 30, 40, 50],
    40
))


print("\n🔹 Revision Problem 4")
print(max_subarray_sum(
    [-2, 1, -3, 4, -1, 2, 1]
))


print("\n🔹 Revision Problem 5")
print(longest_unique_substring(
    "abcabcbb"
))