# ==========================================================
# Month 7 - Day 15
# Python itertools Module
#
# Topics Covered:
# 1. combinations()
# 2. permutations()
# 3. product()
# 4. accumulate()
# 5. groupby()
# 6. cycle()
# ==========================================================

from itertools import combinations, permutations, product
from itertools import accumulate, groupby, cycle
import operator

print("=" * 60)
print("1. COMBINATIONS")
print("=" * 60)

numbers = [1, 2, 3, 4]

print("Choose 2 Elements:")

for item in combinations(numbers, 2):
    print(item)

print("Total Combinations:",
      len(list(combinations(numbers, 2))))


print("\n" + "=" * 60)
print("2. PERMUTATIONS")
print("=" * 60)

letters = ['A', 'B', 'C']

print("Permutations:")

for item in permutations(letters):
    print(item)

print("Total Permutations:",
      len(list(permutations(letters))))


print("\n" + "=" * 60)
print("3. PRODUCT")
print("=" * 60)

colors = ["Red", "Blue"]
sizes = ["S", "M", "L"]

cartesian = list(product(colors, sizes))

print("Cartesian Product:")

for item in cartesian:
    print(item)


print("\n" + "=" * 60)
print("4. ACCUMULATE")
print("=" * 60)

nums = [1, 2, 3, 4, 5]

print("Numbers:", nums)

print("Running Sum:")
print(list(accumulate(nums)))

print("Running Product:")
print(list(accumulate(nums, operator.mul)))


print("\n" + "=" * 60)
print("5. GROUPBY")
print("=" * 60)

students = [
    ("CSE", "Alice"),
    ("CSE", "Bob"),
    ("ECE", "Charlie"),
    ("ECE", "David"),
    ("EEE", "Eva")
]

students.sort(key=lambda x: x[0])

for department, group in groupby(students, key=lambda x: x[0]):
    print(department)

    for student in group:
        print("   ", student)


print("\n" + "=" * 60)
print("6. CYCLE")
print("=" * 60)

traffic = cycle(["Red", "Yellow", "Green"])

print("Traffic Signal Simulation:")

for i in range(10):
    print(next(traffic))


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ itertools

Provides fast and memory-efficient
iterator tools.

Import

from itertools import *

------------------------------------------------

✔ combinations(iterable, r)

Order does NOT matter.

Example

ABC

AB
AC
BC

Formula

nCr

------------------------------------------------

✔ permutations(iterable)

Order matters.

ABC

AB
BA
AC
CA

Formula

nPr

------------------------------------------------

✔ product()

Cartesian Product

Useful for

Nested loops

Example

product([1,2],[3,4])

(1,3)
(1,4)
(2,3)
(2,4)

------------------------------------------------

✔ accumulate()

Running calculations

Default

Running Sum

Can also perform

Multiplication
Maximum
Minimum

------------------------------------------------

✔ groupby()

Groups consecutive
similar elements.

Usually sort before using.

------------------------------------------------

✔ cycle()

Creates an infinite iterator.

Useful for

Round Robin
Scheduling
Traffic Signals
Repeated Patterns

------------------------------------------------

Interview Tip

Most Useful itertools

✔ combinations
✔ permutations
✔ product
✔ accumulate
✔ groupby
✔ cycle

These appear frequently in
Python interviews and coding contests.
""")