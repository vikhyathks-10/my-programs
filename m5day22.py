# 🔹 DAY 22 - LEETCODE BASICS


# 🔹 1. Two Sum

def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):

        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i


# 🔹 2. Reverse String

def reverse_string(s):

    left = 0
    right = len(s) - 1

    s = list(s)

    while left < right:

        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

    return "".join(s)


# 🔹 3. Palindrome Number

def is_palindrome(x):

    return str(x) == str(x)[::-1]


# 🔹 4. Missing Number

def missing_number(nums):

    n = len(nums)

    expected = n * (n + 1) // 2

    return expected - sum(nums)


# 🔹 5. Remove Duplicates from Sorted Array

def remove_duplicates(nums):

    if not nums:
        return 0

    i = 0

    for j in range(1, len(nums)):

        if nums[j] != nums[i]:

            i += 1
            nums[i] = nums[j]

    return i + 1


# 🔹 MAIN PROGRAM

print("\n--- Two Sum ---")

print(two_sum([2, 7, 11, 15], 9))


print("\n--- Reverse String ---")

print(reverse_string("python"))


print("\n--- Palindrome Number ---")

print(is_palindrome(121))
print(is_palindrome(123))


print("\n--- Missing Number ---")

print(missing_number([3, 0, 1]))


print("\n--- Remove Duplicates ---")

arr = [1, 1, 2, 2, 3]

length = remove_duplicates(arr)

print("Length:", length)

print("Updated Array:", arr[:length])