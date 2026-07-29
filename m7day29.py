# ==========================================================
# Month 7 - Day 29
# Python Coding Patterns
#
# Programs:
# 1. Two Pointers
# 2. Sliding Window
# 3. Hash Map
# 4. Prefix Sum
# 5. Stack
# 6. Queue
# 7. Binary Search
# ==========================================================

from collections import deque


# ==========================================================
# 1. TWO POINTERS
# Find two numbers whose sum equals target
# ==========================================================

print("=" * 50)
print("1. TWO POINTERS")
print("=" * 50)

numbers = [1, 2, 4, 6, 8, 10]
target = 12

left = 0
right = len(numbers) - 1

found = False

while left < right:

    current_sum = numbers[left] + numbers[right]

    if current_sum == target:

        print(
            "Pair:",
            numbers[left],
            numbers[right]
        )

        found = True
        break

    elif current_sum < target:
        left += 1

    else:
        right -= 1

if not found:
    print("Pair not found")

print("Time Complexity: O(n)")


# ==========================================================
# 2. SLIDING WINDOW
# Maximum sum of k consecutive elements
# ==========================================================

print("\n" + "=" * 50)
print("2. SLIDING WINDOW")
print("=" * 50)

numbers = [2, 1, 5, 1, 3, 2]

k = 3

window_sum = sum(numbers[:k])

max_sum = window_sum

for i in range(k, len(numbers)):

    window_sum += numbers[i]

    window_sum -= numbers[i - k]

    max_sum = max(
        max_sum,
        window_sum
    )

print("Numbers:", numbers)
print("Window Size:", k)
print("Maximum Sum:", max_sum)

print("Time Complexity: O(n)")


# ==========================================================
# 3. HASH MAP
# Find frequency of each element
# ==========================================================

print("\n" + "=" * 50)
print("3. HASH MAP")
print("=" * 50)

numbers = [
    1, 2, 2, 3,
    3, 3, 4, 4
]

frequency = {}

for number in numbers:

    frequency[number] = (
        frequency.get(number, 0) + 1
    )

print("Numbers:", numbers)

print("Frequency:")

for number, count in frequency.items():

    print(
        number,
        "->",
        count
    )

print("Time Complexity: O(n)")


# ==========================================================
# 4. PREFIX SUM
# Find sum between indexes left and right
# ==========================================================

print("\n" + "=" * 50)
print("4. PREFIX SUM")
print("=" * 50)

numbers = [10, 20, 30, 40, 50]

prefix = [0]

for number in numbers:

    prefix.append(
        prefix[-1] + number
    )

left = 1
right = 3

range_sum = (
    prefix[right + 1]
    - prefix[left]
)

print("Numbers:", numbers)

print("Prefix Sum:", prefix)

print(
    f"Sum from index {left} to {right}:",
    range_sum
)

print("Build Prefix: O(n)")
print("Each Range Query: O(1)")


# ==========================================================
# 5. STACK
# Valid Parentheses
# ==========================================================

print("\n" + "=" * 50)
print("5. STACK - VALID PARENTHESES")
print("=" * 50)

expression = "{[()]}"

stack = []

pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}

valid = True

for char in expression:

    if char in "([{":

        stack.append(char)

    elif char in pairs:

        if (
            not stack
            or stack[-1] != pairs[char]
        ):

            valid = False
            break

        stack.pop()

if stack:
    valid = False

print("Expression:", expression)
print("Valid:", valid)

print("Time Complexity: O(n)")


# ==========================================================
# 6. QUEUE
# FIFO Processing
# ==========================================================

print("\n" + "=" * 50)
print("6. QUEUE")
print("=" * 50)

queue = deque()

queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")

print("Queue:", list(queue))

while queue:

    task = queue.popleft()

    print("Processing:", task)

print("Time Complexity: O(n)")


# ==========================================================
# 7. BINARY SEARCH
# Search in sorted array
# ==========================================================

print("\n" + "=" * 50)
print("7. BINARY SEARCH")
print("=" * 50)


def binary_search(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:

        mid = (
            left + (right - left) // 2
        )

        if numbers[mid] == target:

            return mid

        elif numbers[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return -1


numbers = [
    10, 20, 30,
    40, 50, 60, 70
]

target = 40

result = binary_search(
    numbers,
    target
)

print("Numbers:", numbers)
print("Target :", target)

if result != -1:

    print(
        "Target found at index:",
        result
    )

else:

    print("Target not found")

print("Time Complexity: O(log n)")


# ==========================================================
# INTERVIEW SUMMARY
# ==========================================================

print("\n" + "=" * 50)
print("INTERVIEW SUMMARY")
print("=" * 50)

print("""
1. TWO POINTERS

Use when:

✔ Sorted Array
✔ Pair Problems
✔ Opposite Ends
✔ Removing Duplicates

Example:

Two Sum on Sorted Array

Time:
O(n)


--------------------------------------------

2. SLIDING WINDOW

Use when:

✔ Subarray
✔ Substring
✔ Consecutive Elements
✔ Maximum / Minimum Window

Example:

Maximum sum of k elements

Time:
O(n)


--------------------------------------------

3. HASH MAP

Use when:

✔ Frequency
✔ Duplicate Detection
✔ Fast Lookup
✔ Two Sum

Python:

dictionary

Average Lookup:
O(1)


--------------------------------------------

4. PREFIX SUM

Use when:

✔ Multiple Range Sum Queries
✔ Subarray Sum
✔ Cumulative Values

Build:

O(n)

Query:

O(1)


--------------------------------------------

5. STACK

Remember:

LIFO

Last In
First Out

Use when:

✔ Parentheses
✔ Undo
✔ Expression Evaluation
✔ Next Greater Element


--------------------------------------------

6. QUEUE

Remember:

FIFO

First In
First Out

Use when:

✔ BFS
✔ Scheduling
✔ Waiting Line
✔ Task Processing

Python:

collections.deque


--------------------------------------------

7. BINARY SEARCH

Use when:

✔ Sorted Data
✔ Search Space Can Be Halved

Time:

O(log n)


--------------------------------------------

PATTERN RECOGNITION

Sorted Array + Pair
→ Two Pointers

Consecutive Elements
→ Sliding Window

Frequency / Lookup
→ Hash Map

Range Sum
→ Prefix Sum

Matching / Undo
→ Stack

FIFO / BFS
→ Queue

Sorted Search
→ Binary Search
""")


# ==========================================================
# DAY 29 COMPLETED
# ==========================================================

print("\n" + "=" * 50)
print("DAY 29 COMPLETED")
print("=" * 50)

print("""
Programs Completed:

1. Two Pointers
2. Sliding Window
3. Hash Map
4. Prefix Sum
5. Stack
6. Queue
7. Binary Search

Goal:

Don't just memorize solutions.

Learn to recognize which
pattern fits the problem.
""")