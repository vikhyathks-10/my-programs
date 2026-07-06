# ==========================================================
# Month 7 - Day 6
# Hash Map Problems
#
# Topics Covered:
# 1. Count Character Frequency
# 2. Word Frequency
# 3. Duplicate Detection
# 4. Missing Number
# 5. Majority Element
# 6. Two Sum
# ==========================================================

from collections import Counter

print("=" * 60)
print("1. COUNT CHARACTER FREQUENCY")
print("=" * 60)

text = "programming"

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print("String:", text)
print("Frequency:", frequency)


print("\n" + "=" * 60)
print("2. WORD FREQUENCY")
print("=" * 60)

sentence = "python is easy python is powerful python"

words = sentence.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Sentence:")
print(sentence)

print("\nWord Frequency:")

for word, count in word_count.items():
    print(f"{word} : {count}")


print("\n" + "=" * 60)
print("3. DUPLICATE DETECTION")
print("=" * 60)

numbers = [2, 5, 8, 2, 6, 5, 10, 12]

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Numbers :", numbers)
print("Duplicates :", list(duplicates))


print("\n" + "=" * 60)
print("4. MISSING NUMBER")
print("=" * 60)

numbers = [1, 2, 3, 5, 6]

n = 6

expected = n * (n + 1) // 2
actual = sum(numbers)

print("Numbers :", numbers)
print("Missing Number :", expected - actual)


print("\n" + "=" * 60)
print("5. MAJORITY ELEMENT")
print("=" * 60)

nums = [2, 2, 1, 2, 3, 2, 2]

counter = Counter(nums)

majority = None

for key, value in counter.items():
    if value > len(nums) // 2:
        majority = key
        break

print("Array :", nums)
print("Majority Element :", majority)


print("\n" + "=" * 60)
print("6. TWO SUM")
print("=" * 60)

nums = [2, 7, 11, 15]
target = 9

lookup = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in lookup:
        print("Indices :", lookup[complement], i)
        print("Values :", complement, num)
        break

    lookup[num] = i


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ Hash Map
- Stores key-value pairs.
- Python implementation:
  Dictionary {}

-----------------------------------------

✔ Frequency Counting

dict.get(key,0)

or

collections.Counter

Time Complexity:
O(n)

-----------------------------------------

✔ Duplicate Detection

Use a set.

Time:
O(n)

-----------------------------------------

✔ Missing Number

Formula:

n(n+1)/2

Expected Sum - Actual Sum

Time:
O(n)

-----------------------------------------

✔ Majority Element

Element occurring more than n/2 times.

Can be solved using:

Counter
Dictionary
Boyer-Moore Voting Algorithm (Optimal)

-----------------------------------------

✔ Two Sum

Use a dictionary to store:

Value → Index

Time Complexity:
O(n)

Space Complexity:
O(n)

-----------------------------------------

Interview Tip:

Whenever you hear:

• Frequency
• Duplicate
• Lookup
• Pair Sum

Think:

👉 Hash Map (Dictionary)

Most interview solutions become O(n)
using dictionaries instead of nested loops.
""")