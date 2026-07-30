# ==========================================================
# Month 7 - Day 30
# Mock Coding Interview
#
# Programs:
# 1. Reverse Words
# 2. Group Anagrams
# 3. Valid Parentheses
# 4. Product Except Self
# 5. Top K Frequent Elements
# 6. Happy Number
# 7. Climbing Stairs
# ==========================================================

from collections import defaultdict, Counter
import heapq


# ==========================================================
# 1. REVERSE WORDS
# ==========================================================

print("=" * 60)
print("1. REVERSE WORDS")
print("=" * 60)


def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])


sentence = "Python makes coding interesting"

print("Original :", sentence)
print("Reversed :", reverse_words(sentence))

# Time Complexity: O(n)
# Space Complexity: O(n)


# ==========================================================
# 2. GROUP ANAGRAMS
# ==========================================================

print("\n" + "=" * 60)
print("2. GROUP ANAGRAMS")
print("=" * 60)


def group_anagrams(words):

    groups = defaultdict(list)

    for word in words:

        key = "".join(sorted(word))

        groups[key].append(word)

    return list(groups.values())


words = [
    "eat",
    "tea",
    "tan",
    "ate",
    "nat",
    "bat"
]

result = group_anagrams(words)

print("Words:", words)

print("Grouped Anagrams:")

for group in result:
    print(group)

# Time Complexity:
# O(n * k log k)
#
# n = number of words
# k = average word length


# ==========================================================
# 3. VALID PARENTHESES
# ==========================================================

print("\n" + "=" * 60)
print("3. VALID PARENTHESES")
print("=" * 60)


def valid_parentheses(expression):

    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in expression:

        if char in "([{":
            stack.append(char)

        elif char in pairs:

            if not stack:
                return False

            if stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0


expressions = [
    "{[()]}",
    "([{}])",
    "(]",
    "([)]"
]

for expression in expressions:

    print(
        expression,
        "->",
        valid_parentheses(expression)
    )

# Time Complexity: O(n)
# Space Complexity: O(n)


# ==========================================================
# 4. PRODUCT EXCEPT SELF
# ==========================================================

print("\n" + "=" * 60)
print("4. PRODUCT EXCEPT SELF")
print("=" * 60)


def product_except_self(numbers):

    n = len(numbers)

    result = [1] * n

    # Prefix Product

    prefix = 1

    for i in range(n):

        result[i] = prefix

        prefix *= numbers[i]

    # Suffix Product

    suffix = 1

    for i in range(n - 1, -1, -1):

        result[i] *= suffix

        suffix *= numbers[i]

    return result


numbers = [1, 2, 3, 4]

result = product_except_self(numbers)

print("Numbers :", numbers)
print("Result  :", result)

# Expected:
#
# [24, 12, 8, 6]
#
# Time Complexity: O(n)
# Extra Space: O(1)
# Output array is not counted.


# ==========================================================
# 5. TOP K FREQUENT ELEMENTS
# ==========================================================

print("\n" + "=" * 60)
print("5. TOP K FREQUENT ELEMENTS")
print("=" * 60)


def top_k_frequent(numbers, k):

    frequency = Counter(numbers)

    # lambda is used instead of frequency.get
    # to avoid Pylance type-checking errors.

    result = heapq.nlargest(
        k,
        frequency.keys(),
        key=lambda x: frequency[x]
    )

    return result


numbers = [
    1, 1, 1,
    2, 2,
    3,
    4, 4, 4, 4
]

k = 2

result = top_k_frequent(numbers, k)

print("Numbers   :", numbers)
print("Frequency :", dict(Counter(numbers)))
print("K         :", k)
print("Top K     :", result)

# Frequency:
#
# 1 -> 3
# 2 -> 2
# 3 -> 1
# 4 -> 4
#
# Top 2:
#
# [4, 1]
#
# Time Complexity:
# O(n + m log k)
#
# n = total elements
# m = unique elements


# ==========================================================
# 6. HAPPY NUMBER
# ==========================================================

print("\n" + "=" * 60)
print("6. HAPPY NUMBER")
print("=" * 60)


def is_happy(number):

    seen = set()

    while number != 1:

        if number in seen:
            return False

        seen.add(number)

        total = 0

        while number > 0:

            digit = number % 10

            total += digit * digit

            number //= 10

        number = total

    return True


numbers_to_check = [
    19,
    2,
    7
]

for number in numbers_to_check:

    print(
        number,
        "->",
        is_happy(number)
    )

# Example for 19:
#
# 19
# ↓
# 1² + 9²
# ↓
# 82
# ↓
# 8² + 2²
# ↓
# 68
# ↓
# 6² + 8²
# ↓
# 100
# ↓
# 1
#
# Therefore:
# 19 is a Happy Number.


# ==========================================================
# 7. CLIMBING STAIRS
# ==========================================================

print("\n" + "=" * 60)
print("7. CLIMBING STAIRS")
print("=" * 60)


def climb_stairs(n):

    if n <= 0:
        return 0

    if n <= 2:
        return n

    previous = 1
    current = 2

    for _ in range(3, n + 1):

        previous, current = (
            current,
            previous + current
        )

    return current


stairs = 5

ways = climb_stairs(stairs)

print("Number of Stairs :", stairs)
print("Ways to Climb    :", ways)

# Number of ways:
#
# n = 1 -> 1
# n = 2 -> 2
# n = 3 -> 3
# n = 4 -> 5
# n = 5 -> 8
#
# Time Complexity: O(n)
# Space Complexity: O(1)


# ==========================================================
# INTERVIEW SUMMARY
# ==========================================================

print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
1. REVERSE WORDS

Pattern:
String Manipulation

Tools:

split()
join()
slicing

Time:
O(n)


------------------------------------------------------------

2. GROUP ANAGRAMS

Pattern:

Hash Map
+
Sorting

Idea:

eat -> aet
tea -> aet
ate -> aet

Same sorted form
means they are anagrams.


------------------------------------------------------------

3. VALID PARENTHESES

Pattern:

Stack

Opening Bracket
-> Push

Closing Bracket
-> Match and Pop

Time:
O(n)


------------------------------------------------------------

4. PRODUCT EXCEPT SELF

Pattern:

Prefix Product
+
Suffix Product

Example:

[1, 2, 3, 4]

Result:

[24, 12, 8, 6]

Time:
O(n)


------------------------------------------------------------

5. TOP K FREQUENT ELEMENTS

Pattern:

Frequency Map
+
Heap

Tools:

Counter
heapq

Example:

[1,1,1,2,2,3,4,4,4,4]

Frequency:

1 -> 3
2 -> 2
3 -> 1
4 -> 4

Top 2:

[4, 1]


------------------------------------------------------------

6. HAPPY NUMBER

Pattern:

Hash Set
+
Cycle Detection

Store previously seen numbers.

If a number repeats,
there is a cycle.


------------------------------------------------------------

7. CLIMBING STAIRS

Pattern:

Dynamic Programming

Formula:

ways(n) =
ways(n - 1) + ways(n - 2)

Similar to Fibonacci.

Time:
O(n)

Space:
O(1)


------------------------------------------------------------

MOCK INTERVIEW STRATEGY

1. Understand the problem

2. Identify input and output

3. Think of brute-force solution

4. Identify coding pattern

5. Optimize the solution

6. Write clean code

7. Dry-run the solution

8. Test edge cases

9. Explain time complexity

10. Explain space complexity


------------------------------------------------------------

PATTERNS PRACTICED

Reverse Words
-> String Manipulation

Group Anagrams
-> Hash Map + Sorting

Valid Parentheses
-> Stack

Product Except Self
-> Prefix + Suffix

Top K Frequent
-> Counter + Heap

Happy Number
-> Hash Set

Climbing Stairs
-> Dynamic Programming
""")


# ==========================================================
# DAY 30 COMPLETED
# ==========================================================

print("\n" + "=" * 60)
print("DAY 30 COMPLETED")
print("=" * 60)

print("""
Problems Completed:

1. Reverse Words
2. Group Anagrams
3. Valid Parentheses
4. Product Except Self
5. Top K Frequent Elements
6. Happy Number
7. Climbing Stairs

Interview Patterns:

✔ String Manipulation
✔ Hash Map
✔ Sorting
✔ Stack
✔ Prefix / Suffix
✔ Heap
✔ Hash Set
✔ Dynamic Programming
""")