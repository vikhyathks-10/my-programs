# 🔹 DAY 27 - MINI PROBLEMS


# 🔹 1. Check if Array is Subset of Another
def is_subset(arr1, arr2):
    return set(arr2).issubset(set(arr1))


# 🔹 2. First Unique Character
def first_unique(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1


# 🔹 3. Leaders in Array
def leaders(arr):
    result = []
    max_right = float('-inf')

    for num in reversed(arr):
        if num > max_right:
            result.append(num)
            max_right = num

    return result[::-1]


# 🔹 4. Check Two Strings Rotation
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)


# 🔹 5. Equilibrium Index
def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        total -= arr[i]
        if left_sum == total:
            return i
        left_sum += arr[i]

    return -1


# 🔹 MAIN PROGRAM

print("\n--- Subset Check ---")
print(is_subset([1, 2, 3, 4], [2, 3]))


print("\n--- First Unique Character ---")
print(first_unique("leetcode"))


print("\n--- Leaders in Array ---")
print(leaders([16, 17, 4, 3, 5, 2]))


print("\n--- String Rotation ---")
print(is_rotation("abcd", "cdab"))


print("\n--- Equilibrium Index ---")
print(equilibrium_index([1, 3, 5, 2, 2]))