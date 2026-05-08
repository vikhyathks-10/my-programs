# 🔹 DAY 8 - REGEX BASICS

import re


# 🔹 Sample Text

text = "Python 3 is powerful. My number is 987654 and score is 95."


# 🔹 1. Match Simple Word

print("\n--- Match Simple Word ---")

match = re.match(r"Python", text)

if match:
    print("Matched:", match.group())
else:
    print("No Match")


# 🔹 2. Search Numbers

print("\n--- Search Numbers ---")

numbers = re.search(r"\d+", text)

if numbers:
    print("First Number Found:", numbers.group())


# 🔹 3. Find Vowels

print("\n--- Find Vowels ---")

vowels = re.findall(r"[aeiouAEIOU]", text)

print(vowels)


# 🔹 4. Extract Digits

print("\n--- Extract Digits ---")

digits = re.findall(r"\d", text)

print(digits)


# 🔹 5. Count Matches

print("\n--- Count Matches ---")

count = len(re.findall(r"\d+", text))

print("Total Number Groups:", count)