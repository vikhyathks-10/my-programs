# ==========================================================
# Month 7 - Day 11
# Array Interview Problems
#
# Topics Covered:
# 1. Rotate Array
# 2. Product Except Self
# 3. Peak Element
# 4. Maximum Difference
# 5. Merge Intervals
# 6. Intersection of Arrays
# ==========================================================

print("=" * 60)
print("1. ROTATE ARRAY")
print("=" * 60)

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

k = k % len(arr)

rotated = arr[-k:] + arr[:-k]

print("Original Array :", arr)
print("Rotate by", k)
print("Rotated Array :", rotated)


print("\n" + "=" * 60)
print("2. PRODUCT EXCEPT SELF")
print("=" * 60)

nums = [1, 2, 3, 4]

left = [1] * len(nums)
right = [1] * len(nums)

for i in range(1, len(nums)):
    left[i] = left[i - 1] * nums[i - 1]

for i in range(len(nums) - 2, -1, -1):
    right[i] = right[i + 1] * nums[i + 1]

answer = []

for i in range(len(nums)):
    answer.append(left[i] * right[i])

print("Original :", nums)
print("Product Except Self :", answer)


print("\n" + "=" * 60)
print("3. PEAK ELEMENT")
print("=" * 60)

nums = [1, 3, 20, 4, 1, 0]

peak = -1

for i in range(len(nums)):

    left = nums[i - 1] if i > 0 else float("-inf")
    right = nums[i + 1] if i < len(nums) - 1 else float("-inf")

    if nums[i] > left and nums[i] > right:
        peak = nums[i]
        break

print("Array :", nums)
print("Peak Element :", peak)


print("\n" + "=" * 60)
print("4. MAXIMUM DIFFERENCE")
print("=" * 60)

prices = [7, 1, 5, 3, 6, 4]

minimum = prices[0]
maximum_profit = 0

for price in prices[1:]:

    if price < minimum:
        minimum = price

    maximum_profit = max(maximum_profit, price - minimum)

print("Prices :", prices)
print("Maximum Difference :", maximum_profit)


print("\n" + "=" * 60)
print("5. MERGE INTERVALS")
print("=" * 60)

intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort()

merged = [intervals[0]]

for current in intervals[1:]:

    previous = merged[-1]

    if current[0] <= previous[1]:
        previous[1] = max(previous[1], current[1])
    else:
        merged.append(current)

print("Intervals :", intervals)
print("Merged :", merged)


print("\n" + "=" * 60)
print("6. INTERSECTION OF ARRAYS")
print("=" * 60)

arr1 = [1,2,2,3,4]
arr2 = [2,2,4,6]

intersection = list(set(arr1) & set(arr2))

print("Array 1 :", arr1)
print("Array 2 :", arr2)
print("Intersection :", intersection)


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ Rotate Array

Methods:
1. Slicing
2. Reversal Algorithm
3. Extra Array

Time:
O(n)

--------------------------------------------

✔ Product Except Self

Use:

Left Product
+
Right Product

Without division.

Time:
O(n)

--------------------------------------------

✔ Peak Element

Element greater than
both neighbours.

Can also be solved
using Binary Search.

--------------------------------------------

✔ Maximum Difference

Keep track of:

Minimum element so far.

Time:
O(n)

--------------------------------------------

✔ Merge Intervals

1. Sort intervals.
2. Merge overlapping intervals.

Time:
O(n log n)

--------------------------------------------

✔ Intersection of Arrays

Use:

set()

Time:
O(n)

--------------------------------------------

Interview Tip

Whenever the question contains:

✔ Array
✔ Range
✔ Interval
✔ Rotation
✔ Profit
✔ Product

Think about:

• Prefix/Suffix Arrays
• Two Pointers
• Sorting
• Hash Set
• Greedy

Most optimal solutions
are O(n) or O(n log n).
""")