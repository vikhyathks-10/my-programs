# ==========================================================
# Month 7 - Day 27
# Python Debugging Challenges
#
# Programs:
# 1. Division Error Handling
# 2. List Index Error
# 3. Dictionary Key Error
# 4. Type Conversion Error
# 5. Find Largest Number
# 6. Average with Empty List
# 7. Second Largest Number
# ==========================================================


# ==========================================================
# 1. DIVISION ERROR HANDLING
# ==========================================================

print("=" * 50)
print("1. DIVISION ERROR HANDLING")
print("=" * 50)


def divide(a, b):

    if b == 0:
        return "Cannot divide by zero"

    return a / b


print("10 / 2 =", divide(10, 2))
print("10 / 0 =", divide(10, 0))


# ==========================================================
# 2. LIST INDEX ERROR
# ==========================================================

print("\n" + "=" * 50)
print("2. LIST INDEX ERROR")
print("=" * 50)

numbers = [10, 20, 30, 40]

print("List:", numbers)

print("Elements:")

for i in range(len(numbers)):
    print(numbers[i])


# ==========================================================
# 3. DICTIONARY KEY ERROR
# ==========================================================

print("\n" + "=" * 50)
print("3. DICTIONARY KEY ERROR")
print("=" * 50)

student = {
    "name": "Arjun",
    "branch": "CSE",
    "cgpa": 9.1
}

print("Name   :", student.get("name"))
print("Branch :", student.get("branch"))
print("CGPA   :", student.get("cgpa"))

# Key does not exist, so default value is returned

print(
    "Age    :",
    student.get("age", "Not Available")
)


# ==========================================================
# 4. TYPE CONVERSION ERROR
# ==========================================================

print("\n" + "=" * 50)
print("4. TYPE CONVERSION ERROR")
print("=" * 50)

age = "20"

print("Age stored as string:", age)

age = int(age)

future_age = age + 5

print("Current Age :", age)
print("Age After 5 Years :", future_age)


# ==========================================================
# 5. FIND LARGEST NUMBER
# ==========================================================

print("\n" + "=" * 50)
print("5. FIND LARGEST NUMBER")
print("=" * 50)

numbers = [5, 12, 7, 25, 10, 18]

largest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

print("Numbers :", numbers)
print("Largest :", largest)


# ==========================================================
# 6. AVERAGE WITH EMPTY LIST
# ==========================================================

print("\n" + "=" * 50)
print("6. AVERAGE WITH EMPTY LIST")
print("=" * 50)


def find_average(numbers):

    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


marks = [80, 90, 75, 85]

empty_marks = []

print("Marks:", marks)

print(
    "Average:",
    find_average(marks)
)

print(
    "Empty List Average:",
    find_average(empty_marks)
)


# ==========================================================
# 7. SECOND LARGEST NUMBER
# ==========================================================

print("\n" + "=" * 50)
print("7. SECOND LARGEST NUMBER")
print("=" * 50)


def second_largest(numbers):

    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return "Second largest does not exist"

    unique_numbers.sort(reverse=True)

    return unique_numbers[1]


numbers = [10, 30, 20, 50, 40, 50]

print("Numbers :", numbers)

print(
    "Second Largest :",
    second_largest(numbers)
)


# ==========================================================
# DEBUGGING EXAMPLES
# ==========================================================

print("\n" + "=" * 50)
print("COMMON DEBUGGING ERRORS")
print("=" * 50)

print("""
1. ZeroDivisionError

Wrong:
10 / 0

Fix:
Check denominator before division.


2. IndexError

Wrong:
numbers[len(numbers)]

Fix:
Use indexes from 0 to len(numbers)-1.


3. KeyError

Wrong:
student["age"]

when age does not exist.

Fix:
student.get("age")


4. TypeError

Wrong:
"20" + 5

Fix:
int("20") + 5


5. Logical Error

Wrong:
if number < largest

when finding maximum.

Fix:
if number > largest


6. Empty Input

Wrong:
sum(numbers) / len(numbers)

when numbers = []

Fix:
Check if list is empty first.


7. Duplicate Values

When finding second largest,
remove duplicates first.
""")


# ==========================================================
# INTERVIEW SUMMARY
# ==========================================================

print("\n" + "=" * 50)
print("INTERVIEW SUMMARY")
print("=" * 50)

print("""
Three Main Types of Errors:

1. Syntax Error
2. Runtime Error
3. Logical Error


Common Runtime Errors:

ValueError
TypeError
IndexError
KeyError
ZeroDivisionError
FileNotFoundError


Debugging Steps:

1. Read the error message
2. Check the error line
3. Understand the expected output
4. Find the bug
5. Fix the code
6. Run again
7. Test edge cases


Important Edge Cases:

Empty List
Single Element
Zero
Negative Numbers
Duplicate Values
Large Inputs
""")


print("\n" + "=" * 50)
print("DAY 27 COMPLETED")
print("=" * 50)

print("""
Programs Completed:

1. Division Error Handling
2. List Index Error
3. Dictionary Key Error
4. Type Conversion Error
5. Find Largest Number
6. Average with Empty List
7. Second Largest Number
""")