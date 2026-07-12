# ==========================================================
# Month 7 - Day 12
# Kadane's Algorithm & Optimization
#
# Topics Covered:
# 1. Kadane's Algorithm
# 2. Maximum Circular Subarray Sum
# 3. Best Time to Buy & Sell Stock
# 4. Maximum Product Subarray
# 5. Trapping Rain Water
# 6. Optimize Nested Loops using Hash Map
# ==========================================================

print("=" * 60)
print("1. KADANE'S ALGORITHM")
print("=" * 60)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print("Array :", arr)
print("Maximum Subarray Sum :", max_sum)


print("\n" + "=" * 60)
print("2. MAXIMUM CIRCULAR SUBARRAY SUM")
print("=" * 60)

arr = [5, -3, 5]

# Normal Kadane
current = maximum = arr[0]

for num in arr[1:]:
    current = max(num, current + num)
    maximum = max(maximum, current)

# Minimum Subarray
current_min = minimum = arr[0]

for num in arr[1:]:
    current_min = min(num, current_min + num)
    minimum = min(minimum, current_min)

total = sum(arr)

if maximum < 0:
    answer = maximum
else:
    answer = max(maximum, total - minimum)

print("Array :", arr)
print("Maximum Circular Sum :", answer)


print("\n" + "=" * 60)
print("3. BEST TIME TO BUY & SELL STOCK")
print("=" * 60)

prices = [7, 1, 5, 3, 6, 4]

minimum = prices[0]
profit = 0

for price in prices:

    if price < minimum:
        minimum = price

    profit = max(profit, price - minimum)

print("Prices :", prices)
print("Maximum Profit :", profit)


print("\n" + "=" * 60)
print("4. MAXIMUM PRODUCT SUBARRAY")
print("=" * 60)

nums = [2, 3, -2, 4]

maximum = nums[0]
minimum = nums[0]
answer = nums[0]

for num in nums[1:]:

    if num < 0:
        maximum, minimum = minimum, maximum

    maximum = max(num, maximum * num)
    minimum = min(num, minimum * num)

    answer = max(answer, maximum)

print("Array :", nums)
print("Maximum Product :", answer)


print("\n" + "=" * 60)
print("5. TRAPPING RAIN WATER")
print("=" * 60)

height = [0,1,0,2,1,0,1,3,2,1,2,1]

left = 0
right = len(height) - 1

left_max = 0
right_max = 0

water = 0

while left < right:

    if height[left] < height[right]:

        if height[left] >= left_max:
            left_max = height[left]
        else:
            water += left_max - height[left]

        left += 1

    else:

        if height[right] >= right_max:
            right_max = height[right]
        else:
            water += right_max - height[right]

        right -= 1

print("Height :", height)
print("Water Trapped :", water)


print("\n" + "=" * 60)
print("6. OPTIMIZE NESTED LOOPS USING HASH MAP")
print("=" * 60)

nums = [2, 7, 11, 15]
target = 9

lookup = {}

for i, num in enumerate(nums):

    diff = target - num

    if diff in lookup:
        print("Pair Found :", diff, num)
        print("Indices :", lookup[diff], i)
        break

    lookup[num] = i


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ Kadane's Algorithm

Finds Maximum Subarray Sum

Time : O(n)
Space: O(1)

-----------------------------------------

✔ Maximum Circular Sum

Answer = max(
Normal Kadane,
Total Sum - Minimum Subarray
)

-----------------------------------------

✔ Best Time to Buy & Sell Stock

Keep track of:

Minimum Price
Maximum Profit

Time : O(n)

-----------------------------------------

✔ Maximum Product Subarray

Maintain:

Maximum Product
Minimum Product

Negative numbers can swap them.

-----------------------------------------

✔ Trapping Rain Water

Use:

Two Pointers

Time : O(n)
Space: O(1)

-----------------------------------------

✔ Optimize Nested Loops

Instead of:

for i:
    for j:

Use Dictionary / Hash Map

Reduces:

O(n²)

to

O(n)

-----------------------------------------

Interview Tip

Whenever you hear:

✔ Maximum Sum
✔ Maximum Product
✔ Stock Profit
✔ Rain Water
✔ Optimization

Think:

👉 Kadane
👉 Greedy
👉 Two Pointer
👉 Hash Map
""")