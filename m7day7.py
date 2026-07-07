# ==========================================================
# Month 7 - Day 7
# Sliding Window Basics
#
# Topics Covered:
# 1. Maximum Sum Subarray (Fixed Window)
# 2. Smallest Subarray with Sum >= Target
# 3. Longest Unique Substring
# 4. Maximum Consecutive Ones
# 5. Fixed Window Average
# 6. Maximum Element in Every Window
# ==========================================================

from collections import deque

print("=" * 60)
print("1. MAXIMUM SUM SUBARRAY (Fixed Window)")
print("=" * 60)

arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)

print("Array :", arr)
print("Window Size :", k)
print("Maximum Sum :", max_sum)


print("\n" + "=" * 60)
print("2. SMALLEST SUBARRAY WITH SUM >= TARGET")
print("=" * 60)

arr = [2, 3, 1, 2, 4, 3]
target = 7

left = 0
current_sum = 0
min_length = float('inf')

for right in range(len(arr)):
    current_sum += arr[right]

    while current_sum >= target:
        min_length = min(min_length, right - left + 1)
        current_sum -= arr[left]
        left += 1

print("Array :", arr)
print("Target :", target)
print("Smallest Length :", min_length)


print("\n" + "=" * 60)
print("3. LONGEST UNIQUE SUBSTRING")
print("=" * 60)

s = "abcabcbb"

left = 0
seen = {}
max_len = 0

for right in range(len(s)):
    if s[right] in seen and seen[s[right]] >= left:
        left = seen[s[right]] + 1

    seen[s[right]] = right
    max_len = max(max_len, right - left + 1)

print("String :", s)
print("Longest Unique Length :", max_len)


print("\n" + "=" * 60)
print("4. MAXIMUM CONSECUTIVE ONES")
print("=" * 60)

nums = [1, 1, 0, 1, 1, 1, 0, 1]

count = 0
maximum = 0

for num in nums:
    if num == 1:
        count += 1
        maximum = max(maximum, count)
    else:
        count = 0

print("Array :", nums)
print("Maximum Consecutive Ones :", maximum)


print("\n" + "=" * 60)
print("5. FIXED WINDOW AVERAGE")
print("=" * 60)

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

window_sum = sum(arr[:k])
averages = [window_sum / k]

for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]
    averages.append(window_sum / k)

print("Array :", arr)
print("Window Size :", k)
print("Averages :", averages)


print("\n" + "=" * 60)
print("6. MAXIMUM ELEMENT IN EVERY WINDOW")
print("=" * 60)

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

dq = deque()
result = []

for i in range(len(arr)):

    while dq and dq[0] <= i - k:
        dq.popleft()

    while dq and arr[dq[-1]] < arr[i]:
        dq.pop()

    dq.append(i)

    if i >= k - 1:
        result.append(arr[dq[0]])

print("Array :", arr)
print("Window Size :", k)
print("Maximums :", result)


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ Sliding Window

Used for contiguous subarrays/substrings.

--------------------------------------------

✔ Fixed Size Window

Examples:
• Maximum Sum Subarray
• Average of K Elements
• Maximum in Every Window

Time:
O(n)

--------------------------------------------

✔ Variable Size Window

Examples:
• Smallest Subarray
• Longest Substring
• Minimum Window Problems

Time:
O(n)

--------------------------------------------

✔ Longest Unique Substring

Use:
Dictionary + Sliding Window

--------------------------------------------

✔ Maximum Consecutive Ones

Keep a running count.

--------------------------------------------

✔ Maximum Element in Window

Optimal:
Deque

Time:
O(n)

--------------------------------------------

Interview Tip:

Whenever you hear:

• Continuous
• Contiguous
• Window Size
• Longest Substring
• Shortest Subarray

Think:

👉 Sliding Window

It often reduces O(n²) solutions to O(n).
""")