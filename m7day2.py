# ==========================================================
# Month 7 - Day 2
# Python Interview Basics II
#
# Topics Covered:
# 1. *args
# 2. **kwargs
# 3. Lambda Functions
# 4. map()
# 5. filter()
# 6. reduce()
# ==========================================================

from functools import reduce

print("=" * 60)
print("1. *args")
print("=" * 60)

def add_numbers(*args):
    print("Arguments received:", args)
    print("Sum =", sum(args))

add_numbers(10, 20, 30)
add_numbers(5, 10, 15, 20, 25)


print("\n" + "=" * 60)
print("2. **kwargs")
print("=" * 60)

def student_details(**kwargs):
    print("Student Information")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

student_details(
    Name="Vikhyath",
    Age=20,
    Branch="CSE",
    College="PES University"
)


print("\n" + "=" * 60)
print("3. Lambda Functions")
print("=" * 60)

square = lambda x: x ** 2
cube = lambda x: x ** 3
maximum = lambda a, b: a if a > b else b

print("Square of 6 =", square(6))
print("Cube of 4 =", cube(4))
print("Maximum =", maximum(25, 18))


print("\n" + "=" * 60)
print("4. map()")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
cubes = list(map(lambda x: x ** 3, numbers))

print("Original List :", numbers)
print("Squares       :", squares)
print("Cubes         :", cubes)


print("\n" + "=" * 60)
print("5. filter()")
print("=" * 60)

numbers = [3, 8, 11, 20, 15, 24, 30]

even = list(filter(lambda x: x % 2 == 0, numbers))
odd = list(filter(lambda x: x % 2 != 0, numbers))
greater_than_10 = list(filter(lambda x: x > 10, numbers))

print("Original List     :", numbers)
print("Even Numbers      :", even)
print("Odd Numbers       :", odd)
print("Greater than 10   :", greater_than_10)


print("\n" + "=" * 60)
print("6. reduce()")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

sum_all = reduce(lambda x, y: x + y, numbers)
product_all = reduce(lambda x, y: x * y, numbers)
maximum = reduce(lambda x, y: x if x > y else y, numbers)

print("Numbers :", numbers)
print("Sum     :", sum_all)
print("Product :", product_all)
print("Maximum :", maximum)


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ *args
- Accepts any number of positional arguments.
- Stored as a tuple.

Example:
def fun(*args):
    pass

✔ **kwargs
- Accepts any number of keyword arguments.
- Stored as a dictionary.

Example:
def fun(**kwargs):
    pass

✔ Lambda Function
- Anonymous (unnamed) function.
- Best for short one-line operations.

Syntax:
lambda arguments: expression

✔ map()
- Applies a function to every element.
- Returns a map object.

Syntax:
map(function, iterable)

✔ filter()
- Keeps elements that satisfy a condition.
- Returns a filter object.

Syntax:
filter(function, iterable)

✔ reduce()
- Combines all elements into one value.
- Requires:
from functools import reduce

Syntax:
reduce(function, iterable)

------------------------------------------------------------
Function      Purpose

map()         Transform every element
filter()      Select matching elements
reduce()      Reduce to a single value
------------------------------------------------------------
""")