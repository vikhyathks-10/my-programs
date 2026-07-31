# ==========================================================
# Month 7 - Day 31
# FINAL PYTHON MASTERY CHALLENGE
#
# Programs:
# 1. String Analysis
# 2. Remove Duplicates from List
# 3. Frequency Counter
# 4. Exception Handling Calculator
# 5. OOP - Student Class
# 6. File Handling
# 7. Binary Search
# 8. Two Sum using Hash Map
# ==========================================================


# ==========================================================
# 1. STRING ANALYSIS
# ==========================================================

print("=" * 60)
print("1. STRING ANALYSIS")
print("=" * 60)


def analyze_string(text):

    vowels = 0
    consonants = 0
    digits = 0
    spaces = 0

    for char in text:

        if char.lower() in "aeiou":
            vowels += 1

        elif char.isalpha():
            consonants += 1

        elif char.isdigit():
            digits += 1

        elif char.isspace():
            spaces += 1

    return vowels, consonants, digits, spaces


text = "Python Mastery 2026"

vowels, consonants, digits, spaces = analyze_string(text)

print("Text       :", text)
print("Vowels     :", vowels)
print("Consonants :", consonants)
print("Digits     :", digits)
print("Spaces     :", spaces)

# Time: O(n)


# ==========================================================
# 2. REMOVE DUPLICATES FROM LIST
# ==========================================================

print("\n" + "=" * 60)
print("2. REMOVE DUPLICATES")
print("=" * 60)


def remove_duplicates(numbers):

    seen = set()
    result = []

    for number in numbers:

        if number not in seen:

            seen.add(number)

            result.append(number)

    return result


numbers = [
    10, 20, 10,
    30, 20, 40,
    50, 40
]

print("Original :", numbers)

print(
    "Unique   :",
    remove_duplicates(numbers)
)

# Time: O(n) average
# Space: O(n)


# ==========================================================
# 3. FREQUENCY COUNTER
# ==========================================================

print("\n" + "=" * 60)
print("3. FREQUENCY COUNTER")
print("=" * 60)


def count_frequency(items):

    frequency = {}

    for item in items:

        frequency[item] = (
            frequency.get(item, 0) + 1
        )

    return frequency


numbers = [
    1, 2, 2,
    3, 3, 3,
    4, 4
]

frequency = count_frequency(numbers)

print("Numbers:", numbers)

print("Frequency:")

for number, count in frequency.items():

    print(
        number,
        "->",
        count
    )

# Time: O(n)
# Space: O(n)


# ==========================================================
# 4. EXCEPTION HANDLING CALCULATOR
# ==========================================================

print("\n" + "=" * 60)
print("4. EXCEPTION HANDLING")
print("=" * 60)


def calculator(a, b, operation):

    try:

        if operation == "+":

            return a + b

        elif operation == "-":

            return a - b

        elif operation == "*":

            return a * b

        elif operation == "/":

            return a / b

        else:

            return "Invalid Operation"

    except ZeroDivisionError:

        return "Cannot divide by zero"


print(
    "10 + 5 =",
    calculator(10, 5, "+")
)

print(
    "10 - 5 =",
    calculator(10, 5, "-")
)

print(
    "10 * 5 =",
    calculator(10, 5, "*")
)

print(
    "10 / 5 =",
    calculator(10, 5, "/")
)

print(
    "10 / 0 =",
    calculator(10, 0, "/")
)


# ==========================================================
# 5. OOP - STUDENT CLASS
# ==========================================================

print("\n" + "=" * 60)
print("5. OOP - STUDENT CLASS")
print("=" * 60)


class Student:

    def __init__(
        self,
        name,
        branch,
        marks
    ):

        self.name = name
        self.branch = branch
        self.marks = marks

    def average(self):

        if not self.marks:
            return 0

        return sum(self.marks) / len(self.marks)

    def display(self):

        print("Name    :", self.name)
        print("Branch  :", self.branch)
        print(
            "Average :",
            round(self.average(), 2)
        )


student1 = Student(
    "Arjun",
    "CSE",
    [85, 90, 88, 92, 95]
)

student1.display()


# ==========================================================
# 6. FILE HANDLING
# ==========================================================

print("\n" + "=" * 60)
print("6. FILE HANDLING")
print("=" * 60)

filename = "month7_summary.txt"

try:

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "Month 7 - Python Mastery\n"
        )

        file.write(
            "Day 31 - Final Challenge\n"
        )

        file.write(
            "Status - Completed\n"
        )

    print(
        filename,
        "created successfully!"
    )

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

    print("\nFile Content:")

    print(content)

except OSError as error:

    print(
        "File Error:",
        error
    )


# ==========================================================
# 7. BINARY SEARCH
# ==========================================================

print("\n" + "=" * 60)
print("7. BINARY SEARCH")
print("=" * 60)


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
    40, 50, 60,
    70, 80
]

target = 60

index = binary_search(
    numbers,
    target
)

print("Numbers:", numbers)
print("Target :", target)

if index != -1:

    print(
        "Found at index:",
        index
    )

else:

    print("Target not found")

# Time: O(log n)
# Space: O(1)


# ==========================================================
# 8. TWO SUM USING HASH MAP
# ==========================================================

print("\n" + "=" * 60)
print("8. TWO SUM")
print("=" * 60)


def two_sum(numbers, target):

    seen = {}

    for index, number in enumerate(numbers):

        required = target - number

        if required in seen:

            return [
                seen[required],
                index
            ]

        seen[number] = index

    return []


numbers = [
    2, 7, 11, 15
]

target = 9

result = two_sum(
    numbers,
    target
)

print("Numbers:", numbers)
print("Target :", target)

if result:

    print(
        "Indexes:",
        result
    )

    print(
        "Values :",
        numbers[result[0]],
        "+",
        numbers[result[1]],
        "=",
        target
    )

else:

    print("Pair not found")

# Time: O(n)
# Space: O(n)


# ==========================================================
# FINAL COMPLEXITY REVISION
# ==========================================================

print("\n" + "=" * 60)
print("COMPLEXITY REVISION")
print("=" * 60)

print("""
O(1)
-> Direct access

O(log n)
-> Binary Search

O(n)
-> Single traversal

O(n log n)
-> Efficient sorting

O(n²)
-> Typical nested traversal
""")


# ==========================================================
# FINAL INTERVIEW REVISION
# ==========================================================

print("\n" + "=" * 60)
print("PYTHON INTERVIEW REVISION")
print("=" * 60)

print("""
Python Fundamentals

✔ Variables
✔ Data Types
✔ Operators
✔ Conditions
✔ Loops


Collections

✔ List
✔ Tuple
✔ Set
✔ Dictionary


Functions

✔ Functions
✔ Lambda
✔ *args
✔ **kwargs
✔ Scope


Advanced Python

✔ Decorators
✔ Generators
✔ Iterators
✔ Closures
✔ Type Hints


OOP

✔ Class
✔ Object
✔ Constructor
✔ Encapsulation
✔ Inheritance
✔ Polymorphism
✔ Abstraction


Error Handling

✔ try
✔ except
✔ else
✔ finally
✔ raise


File & Data Processing

✔ TXT
✔ CSV
✔ JSON
✔ Excel
✔ SQLite


Important Libraries

✔ collections
✔ itertools
✔ functools
✔ heapq
✔ bisect
✔ math
✔ datetime


Coding Patterns

✔ Hash Map
✔ Two Pointers
✔ Sliding Window
✔ Prefix Sum
✔ Stack
✔ Queue
✔ Binary Search
✔ Recursion
✔ Dynamic Programming


Complexity

✔ O(1)
✔ O(log n)
✔ O(n)
✔ O(n log n)
✔ O(n²)


Interview Skills

✔ Problem Solving
✔ Code Reading
✔ Debugging
✔ Optimization
✔ Edge Cases
✔ Dry Running
""")


# ==========================================================
# MONTH 7 COMPLETED
# ==========================================================

print("\n" + "=" * 60)
print("MONTH 7 - PYTHON MASTERY COMPLETED!")
print("=" * 60)

print("""
Day 31 Final Challenges:

1. String Analysis
2. Remove Duplicates
3. Frequency Counter
4. Exception Handling Calculator
5. OOP Student Class
6. File Handling
7. Binary Search
8. Two Sum

Month 7 Focus:

✔ Python Interview Preparation
✔ Advanced Problem Solving
✔ Built-in Libraries
✔ Code Optimization
✔ Debugging
✔ Code Reading
✔ Coding Patterns
✔ Mock Interviews
✔ Complexity Analysis
✔ Python Revision

MONTH 7 COMPLETE!
""")