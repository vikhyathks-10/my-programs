# ==========================================================
# Month 7 - Day 18
# Python Regular Expressions (re)
#
# Topics Covered:
# 1. re.search()
# 2. re.findall()
# 3. re.sub()
# 4. Email Validation
# 5. Phone Number Extraction
# 6. Password Validation
# ==========================================================

import re

print("=" * 60)
print("1. re.search()")
print("=" * 60)

text = "Welcome to Python Programming"

pattern = "Python"

match = re.search(pattern, text)

if match:
    print("Pattern Found!")
    print("Matched Word :", match.group())
    print("Start Index  :", match.start())
    print("End Index    :", match.end())
else:
    print("Pattern Not Found")


print("\n" + "=" * 60)
print("2. re.findall()")
print("=" * 60)

sentence = "Python Java C++ Python JavaScript Python"

words = re.findall("Python", sentence)

print("Occurrences:", words)
print("Total Count:", len(words))


print("\n" + "=" * 60)
print("3. re.sub()")
print("=" * 60)

text = "I love Java. Java is powerful."

updated = re.sub("Java", "Python", text)

print("Original :", text)
print("Updated  :", updated)


print("\n" + "=" * 60)
print("4. EMAIL VALIDATION")
print("=" * 60)

email = "student123@gmail.com"

pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

if re.match(pattern, email):
    print(email, "is a Valid Email")
else:
    print(email, "is NOT a Valid Email")


print("\n" + "=" * 60)
print("5. PHONE NUMBER EXTRACTION")
print("=" * 60)

text = """
Contact Numbers:
9876543210
9123456789
8888888888
"""

numbers = re.findall(r'\d{10}', text)

print("Phone Numbers Found:")

for number in numbers:
    print(number)


print("\n" + "=" * 60)
print("6. PASSWORD VALIDATION")
print("=" * 60)

password = "Python@123"

pattern = (
    r'^(?=.*[A-Z])'
    r'(?=.*[a-z])'
    r'(?=.*\d)'
    r'(?=.*[@$!%*?&])'
    r'[A-Za-z\d@$!%*?&]{8,}$'
)

if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ re Module

Used for

• Pattern Matching
• Validation
• Searching
• Text Processing

Import

import re

--------------------------------------------------

✔ re.search()

Returns first occurrence.

Example

re.search("Python", text)

Useful Methods

group()
start()
end()

--------------------------------------------------

✔ re.findall()

Returns ALL matches
as a list.

Example

re.findall(r'\\d+', text)

--------------------------------------------------

✔ re.sub()

Replace matching text.

Example

re.sub("Java","Python",text)

--------------------------------------------------

✔ Email Validation

Pattern

^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$

--------------------------------------------------

✔ Phone Number

\\d{10}

Exactly 10 digits.

--------------------------------------------------

✔ Password Validation

Checks

✔ Uppercase
✔ Lowercase
✔ Digit
✔ Special Character
✔ Minimum Length

--------------------------------------------------

Interview Tip

Whenever you hear

✔ Validation
✔ Pattern Matching
✔ Parsing
✔ Log Analysis

Think:

👉 Regular Expressions (re)

Most Asked Functions

✔ search()
✔ match()
✔ fullmatch()
✔ findall()
✔ finditer()
✔ sub()
✔ split()
""")