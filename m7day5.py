# ==========================================================
# Month 7 - Day 5
# Interview Coding Warm-up
#
# Topics Covered:
# 1. Reverse String (3 Ways)
# 2. Reverse Number
# 3. Palindrome Check
# 4. Anagram Check
# 5. Character Frequency Counter
# 6. First Non-Repeated Character
# ==========================================================

from collections import Counter

print("=" * 60)
print("1. REVERSE STRING (3 WAYS)")
print("=" * 60)

text = "Python"

# Method 1: Slicing
print("Method 1:", text[::-1])

# Method 2: reversed()
print("Method 2:", "".join(reversed(text)))

# Method 3: Loop
reverse = ""
for ch in text:
    reverse = ch + reverse
print("Method 3:", reverse)


print("\n" + "=" * 60)
print("2. REVERSE NUMBER")
print("=" * 60)

num = 12345
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Original Number :", num)
print("Reversed Number :", reverse)


print("\n" + "=" * 60)
print("3. PALINDROME CHECK")
print("=" * 60)

word = "madam"

if word == word[::-1]:
    print(word, "is a Palindrome")
else:
    print(word, "is Not a Palindrome")


print("\n" + "=" * 60)
print("4. ANAGRAM CHECK")
print("=" * 60)

str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print(str1, "and", str2, "are Anagrams")
else:
    print("Not Anagrams")


print("\n" + "=" * 60)
print("5. CHARACTER FREQUENCY COUNTER")
print("=" * 60)

sentence = "programming"

frequency = Counter(sentence)

print("Character Frequency:")

for char, count in frequency.items():
    print(char, ":", count)


print("\n" + "=" * 60)
print("6. FIRST NON-REPEATED CHARACTER")
print("=" * 60)

text = "swiss"

freq = Counter(text)

for ch in text:
    if freq[ch] == 1:
        print("First Non-Repeated Character:", ch)
        break


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ Reverse String
Methods:
1. Slicing
2. reversed()
3. Loop

----------------------------------------

✔ Reverse Number

Repeatedly:
digit = n % 10
reverse = reverse * 10 + digit

----------------------------------------

✔ Palindrome

A palindrome reads the same
forward and backward.

Examples:
madam
racecar
level

----------------------------------------

✔ Anagram

Two strings are anagrams if
their characters are the same
after sorting.

Example:
listen
silent

----------------------------------------

✔ Character Frequency

collections.Counter()

returns occurrences of every character.

----------------------------------------

✔ First Non-Repeated Character

Count frequency first,
then scan from left to right.

----------------------------------------

Interview Tip:
These six problems are among the
most frequently asked Python coding
questions in interviews.
""")