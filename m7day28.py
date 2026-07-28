# ==========================================================
# Month 7 - Day 28
# Code Reading & Complexity Analysis
#
# Programs:
# 1. O(1) - Constant Time
# 2. O(n) - Linear Time
# 3. O(n²) - Quadratic Time
# 4. O(log n) - Binary Search
# 5. O(n log n) - Sorting
# 6. Optimize Search using Set
# 7. Time & Space Complexity Comparison
# ==========================================================


# ==========================================================
# 1. O(1) - CONSTANT TIME
# ==========================================================

print("=" * 50)
print("1. O(1) - CONSTANT TIME")
print("=" * 50)

numbers = [10, 20, 30, 40, 50]

first = numbers[0]

print("List:", numbers)
print("First Element:", first)

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")


# ==========================================================
# 2. O(n) - LINEAR TIME
# ==========================================================

print("\n" + "=" * 50)
print("2. O(n) - LINEAR TIME")
print("=" * 50)

numbers = [5, 10, 15, 20, 25]

total = 0

for number in numbers:
    total += number

print("Numbers:", numbers)
print("Sum:", total)

print("Time Complexity: O(n)")
print("Space Complexity: O(1)")


# ==========================================================
# 3. O(n²) - QUADRATIC TIME
# ==========================================================

print("\n" + "=" * 50)
print("3. O(n²) - QUADRATIC TIME")
print("=" * 50)

numbers = [1, 2, 3, 4]

print("Pairs:")

for i in numbers:
    for j in numbers:
        print(i, j)

print("Time Complexity: O(n²)")
print("Space Complexity: O(1)")


# ==========================================================
# 4. O(log n) - BINARY SEARCH
# ==========================================================

print("\n" + "=" * 50)
print("4. O(log n) - BINARY SEARCH")
print("=" * 50)


def binary_search(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:

        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


numbers = [10, 20, 30, 40, 50, 60, 70]

target = 50

index = binary_search(numbers, target)

print("Numbers:", numbers)
print("Target :", target)
print("Index  :", index)

print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")


# ==========================================================
# 5. O(n log n) - SORTING
# ==========================================================

print("\n" + "=" * 50)
print("5. O(n log n) - SORTING")
print("=" * 50)

numbers = [40, 10, 50, 20, 30]

sorted_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted  :", sorted_numbers)

print("Typical Time Complexity: O(n log n)")
print("Space Complexity: depends on sorting implementation")


# ==========================================================
# 6. OPTIMIZE SEARCH USING SET
# ==========================================================

print("\n" + "=" * 50)
print("6. OPTIMIZE SEARCH USING SET")
print("=" * 50)

numbers = [10, 20, 30, 40, 50]

target = 40


# Linear Search

found = False

for number in numbers:

    if number == target:
        found = True
        break

print("Linear Search:", found)
print("Search Time: O(n)")


# Set Search

number_set = set(numbers)

found = target in number_set

print("\nSet Search:", found)
print("Average Lookup Time: O(1)")

# Important:
# Creating the set itself takes O(n).


# ==========================================================
# 7. TIME & SPACE COMPLEXITY COMPARISON
# ==========================================================

print("\n" + "=" * 50)
print("7. COMPLEXITY COMPARISON")
print("=" * 50)

print("""
O(1)
Constant Time

Example:
arr[0]


O(log n)
Logarithmic Time

Example:
Binary Search


O(n)
Linear Time

Example:
Single Loop


O(n log n)
Linearithmic Time

Example:
Efficient Sorting


O(n²)
Quadratic Time

Example:
Nested Loops
""")


# ==========================================================
# CODE READING CHALLENGE 1
# ==========================================================

print("\n" + "=" * 50)
print("CODE READING CHALLENGE 1")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]

result = 0

for number in numbers:

    if number % 2 == 0:
        result += number

print("Output:", result)

# Dry Run:
#
# 1 -> Odd  -> Ignore
# 2 -> Even -> result = 2
# 3 -> Odd  -> Ignore
# 4 -> Even -> result = 6
# 5 -> Odd  -> Ignore
#
# Output = 6
#
# Time Complexity = O(n)


# ==========================================================
# CODE READING CHALLENGE 2
# ==========================================================

print("\n" + "=" * 50)
print("CODE READING CHALLENGE 2")
print("=" * 50)

count = 0

for i in range(3):

    for j in range(3):

        count += 1

print("Output:", count)

# Outer loop = 3 times
# Inner loop = 3 times
#
# 3 * 3 = 9
#
# Output = 9
#
# General Complexity = O(n²)


# ==========================================================
# CODE READING CHALLENGE 3
# ==========================================================

print("\n" + "=" * 50)
print("CODE READING CHALLENGE 3")
print("=" * 50)

number = 32

steps = 0

while number > 1:

    number //= 2

    steps += 1

print("Steps:", steps)

# Dry Run:
#
# 32 -> 16
# 16 -> 8
# 8  -> 4
# 4  -> 2
# 2  -> 1
#
# Steps = 5
#
# Complexity = O(log n)


# ==========================================================
# INTERVIEW SUMMARY
# ==========================================================

print("\n" + "=" * 50)
print("INTERVIEW SUMMARY")
print("=" * 50)

print("""
TIME COMPLEXITY

Measures how execution time
grows as input size increases.


--------------------------------------------

O(1)

Constant Time

Example:

numbers[0]


--------------------------------------------

O(log n)

Logarithmic Time

Example:

Binary Search


--------------------------------------------

O(n)

Linear Time

Example:

for x in numbers:
    print(x)


--------------------------------------------

O(n log n)

Example:

Sorting


--------------------------------------------

O(n²)

Quadratic Time

Example:

for i in numbers:
    for j in numbers:
        print(i, j)


--------------------------------------------

COMPLEXITY ORDER

Fastest

O(1)

↓

O(log n)

↓

O(n)

↓

O(n log n)

↓

O(n²)

Slowest


--------------------------------------------

SPACE COMPLEXITY

Measures additional memory
used by an algorithm.

Example:

total = 0

uses:

O(1) extra space


Creating:

copy = numbers[:]

uses:

O(n) extra space


--------------------------------------------

INTERVIEW CODE READING STEPS

1. Read the input

2. Identify loops

3. Dry-run variables

4. Predict output

5. Check edge cases

6. Determine time complexity

7. Determine space complexity

8. Look for optimization


--------------------------------------------

IMPORTANT PATTERNS

Direct Access
→ O(1)

Binary Search
→ O(log n)

Single Loop
→ O(n)

Sorting
→ O(n log n)

Nested Loop
→ Often O(n²)

Dictionary / Set Lookup
→ O(1) average
""")


# ==========================================================
# DAY 28 COMPLETED
# ==========================================================

print("\n" + "=" * 50)
print("DAY 28 COMPLETED")
print("=" * 50)

print("""
Programs Practiced:

1. Constant Time - O(1)
2. Linear Time - O(n)
3. Quadratic Time - O(n²)
4. Binary Search - O(log n)
5. Sorting - O(n log n)
6. Set Search Optimization
7. Complexity Comparison

Code Reading:

✔ Predict Output
✔ Dry Run
✔ Identify Loops
✔ Time Complexity
✔ Space Complexity
✔ Optimization
""")