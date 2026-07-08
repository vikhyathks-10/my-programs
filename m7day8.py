# ==========================================================
# Month 7 - Day 8
# Two Pointer Pattern
#
# Topics Covered:
# 1. Pair Sum
# 2. Remove Duplicates from Sorted Array
# 3. Move Zeroes
# 4. Reverse Array
# 5. Merge Two Sorted Arrays
# 6. Container With Most Water
# ==========================================================

print("=" * 60)
print("1. PAIR SUM")
print("=" * 60)

arr = [1, 2, 3, 4, 6, 8, 9]
target = 10

left = 0
right = len(arr) - 1

found = False

while left < right:
    current = arr[left] + arr[right]

    if current == target:
        print("Pair Found:", arr[left], arr[right])
        found = True
        break
    elif current < target:
        left += 1
    else:
        right -= 1

if not found:
    print("No Pair Found")


print("\n" + "=" * 60)
print("2. REMOVE DUPLICATES")
print("=" * 60)

nums = [1, 1, 2, 2, 3, 4, 4, 5]

if nums:
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    print("Unique Elements:", nums[:i + 1])
    print("Count:", i + 1)


print("\n" + "=" * 60)
print("3. MOVE ZEROES")
print("=" * 60)

nums = [0, 1, 0, 3, 12]

left = 0

for right in range(len(nums)):
    if nums[right] != 0:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1

print("After Moving Zeroes:", nums)


print("\n" + "=" * 60)
print("4. REVERSE ARRAY")
print("=" * 60)

arr = [10, 20, 30, 40, 50]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed Array:", arr)


print("\n" + "=" * 60)
print("5. MERGE TWO SORTED ARRAYS")
print("=" * 60)

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

i = j = 0
merged = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

merged.extend(a[i:])
merged.extend(b[j:])

print("Merged Array:", merged)


print("\n" + "=" * 60)
print("6. CONTAINER WITH MOST WATER")
print("=" * 60)

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

left = 0
right = len(height) - 1

maximum = 0

while left < right:

    width = right - left
    area = min(height[left], height[right]) * width

    maximum = max(maximum, area)

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print("Maximum Water Area:", maximum)


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ Two Pointer Technique

Uses two indices moving toward each other
or in the same direction.

--------------------------------------------

✔ Common Applications

• Pair Sum
• Remove Duplicates
• Reverse Array
• Move Zeroes
• Merge Arrays
• Container With Most Water

--------------------------------------------

✔ Types

1. Opposite Direction
   left → ← right

Examples:
• Pair Sum
• Reverse Array
• Container With Most Water

--------------------------------------------

2. Same Direction

Examples:
• Remove Duplicates
• Move Zeroes
• Merge Arrays

--------------------------------------------

Time Complexity

Most problems:
O(n)

Space Complexity

Usually:
O(1)

--------------------------------------------

Interview Tip

Whenever the array is:

✔ Sorted
✔ Needs swapping
✔ Searching pairs
✔ Reversing
✔ Merging

Think:

👉 Two Pointers

It usually converts O(n²)
into O(n).
""")