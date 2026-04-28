# 🔹 DAY 28 - INTERVIEW STYLE QUESTIONS


# 🔹 Q1: Longest Consecutive Sequence (O(n))
def longest_consecutive(arr):
    num_set = set(arr)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:   # start of sequence
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


# 🔹 Q2: Product of Array Except Self
def product_except_self(arr):
    n = len(arr)
    result = [1] * n

    left = 1
    for i in range(n):
        result[i] = left
        left *= arr[i]

    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= arr[i]

    return result


# 🔹 Q3: Valid Parentheses (Stack)
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        else:
            if not stack or stack[-1] != mapping.get(ch):
                return False
            stack.pop()

    return not stack


# 🔹 Q4: Minimum Size Subarray Sum (Sliding Window)
def min_subarray_len(target, arr):
    left = 0
    curr_sum = 0
    min_len = float('inf')

    for right in range(len(arr)):
        curr_sum += arr[right]

        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= arr[left]
            left += 1

    return min_len if min_len != float('inf') else 0


# 🔹 Q5: Group Anagrams
def group_anagrams(strs):
    anagram_map = {}

    for word in strs:
        key = tuple(sorted(word))
        anagram_map.setdefault(key, []).append(word)

    return list(anagram_map.values())


# 🔹 MAIN PROGRAM

print("\n--- Q1: Longest Consecutive ---")
print(longest_consecutive([100, 4, 200, 1, 3, 2]))


print("\n--- Q2: Product Except Self ---")
print(product_except_self([1, 2, 3, 4]))


print("\n--- Q3: Valid Parentheses ---")
print(is_valid_parentheses("{[()]}"))


print("\n--- Q4: Min Subarray Length ---")
print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))


print("\n--- Q5: Group Anagrams ---")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))