# ==========================================================
# Month 7 - Day 9
# Prefix Sum Pattern
#
# Topics Covered:
# 1. Prefix Sum Array
# 2. Range Sum Query
# 3. Running Sum
# 4. Pivot Index
# 5. Subarray Sum Equals K
# 6. Equilibrium Index
# ==========================================================

print("=" * 60)
print("1. PREFIX SUM ARRAY")
print("=" * 60)

arr = [2, 4, 6, 8, 10]

prefix = [0] * len(arr)
prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

print("Original Array :", arr)
print("Prefix Sum     :", prefix)


print("\n" + "=" * 60)
print("2. RANGE SUM QUERY")
print("=" * 60)

arr = [5, 2, 7, 3, 6, 1]

prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)

left = 1
right = 4

range_sum = prefix[right + 1] - prefix[left]

print("Array :", arr)
print(f"Range Sum ({left} to {right}) =", range_sum)


print("\n" + "=" * 60)
print("3. RUNNING SUM")
print("=" * 60)

nums = [1, 2, 3, 4]

running = []

current = 0

for num in nums:
    current += num
    running.append(current)

print("Original :", nums)
print("Running Sum :", running)


print("\n" + "=" * 60)
print("4. PIVOT INDEX")
print("=" * 60)

nums = [1, 7, 3, 6, 5, 6]

total = sum(nums)
left_sum = 0
pivot = -1

for i in range(len(nums)):
    if left_sum == total - left_sum - nums[i]:
        pivot = i
        break
    left_sum += nums[i]

print("Array :", nums)
print("Pivot Index :", pivot)


print("\n" + "=" * 60)
print("5. SUBARRAY SUM EQUALS K")
print("=" * 60)

nums = [1, 1, 1]
k = 2

count = 0
prefix_sum = 0
hashmap = {0: 1}

for num in nums:
    prefix_sum += num

    if prefix_sum - k in hashmap:
        count += hashmap[prefix_sum - k]

    hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

print("Array :", nums)
print("Target :", k)
print("Subarrays :", count)


print("\n" + "=" * 60)
print("6. EQUILIBRIUM INDEX")
print("=" * 60)

arr = [-7, 1, 5, 2, -4, 3, 0]

total = sum(arr)
left_sum = 0
index = -1

for i in range(len(arr)):

    if left_sum == total - left_sum - arr[i]:
        index = i
        break

    left_sum += arr[i]

print("Array :", arr)
print("Equilibrium Index :", index)


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ Prefix Sum

Stores cumulative sums.

Example:

Array:
[2,4,6,8]

Prefix:
[2,6,12,20]

--------------------------------------------

✔ Range Sum Query

Formula:

prefix[right+1] - prefix[left]

Time:
O(1)

--------------------------------------------

✔ Running Sum

Continuously adds previous values.

--------------------------------------------

✔ Pivot Index

Left Sum == Right Sum

--------------------------------------------

✔ Equilibrium Index

Same concept as Pivot Index.

--------------------------------------------

✔ Subarray Sum Equals K

Uses:

Prefix Sum + Hash Map

Time:
O(n)

Space:
O(n)

--------------------------------------------

Interview Tip

Whenever you hear:

• Continuous Sum
• Range Sum
• Subarray Sum
• Prefix

Think:

👉 Prefix Sum

For fast queries:

Use

Prefix + Hash Map

instead of nested loops.
""")