# ==========================================================
# Month 7 - Day 3
# Python Interview Basics III
#
# Topics Covered:
# 1. enumerate()
# 2. zip()
# 3. any()
# 4. all()
# 5. sorted() vs sort()
# 6. Custom Sorting using key
# ==========================================================

print("=" * 60)
print("1. enumerate()")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango", "Orange"]

for index, fruit in enumerate(fruits):
    print(index, "->", fruit)

print("\nStarting index from 1")

for index, fruit in enumerate(fruits, start=1):
    print(index, "->", fruit)


print("\n" + "=" * 60)
print("2. zip()")
print("=" * 60)

names = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]

students = list(zip(names, marks))

print("Zipped List:")
print(students)

print("\nIterating using zip()")

for name, mark in zip(names, marks):
    print(f"{name} scored {mark}")


print("\n" + "=" * 60)
print("3. any()")
print("=" * 60)

numbers = [0, 0, 5, 0]

print("Numbers:", numbers)
print("Any non-zero?", any(numbers))

values = [False, False, False]
print("Values:", values)
print("Any True?", any(values))


print("\n" + "=" * 60)
print("4. all()")
print("=" * 60)

numbers = [2, 4, 6, 8]

print("Numbers:", numbers)
print("All positive?", all(n > 0 for n in numbers))
print("All even?", all(n % 2 == 0 for n in numbers))

numbers = [2, 4, 7, 8]
print("\nNumbers:", numbers)
print("All even?", all(n % 2 == 0 for n in numbers))


print("\n" + "=" * 60)
print("5. sorted() vs sort()")
print("=" * 60)

numbers = [5, 1, 9, 3, 7]

print("Original:", numbers)

sorted_numbers = sorted(numbers)

print("sorted() returns:", sorted_numbers)
print("Original remains:", numbers)

numbers.sort()

print("\nAfter sort():", numbers)


print("\n" + "=" * 60)
print("6. Custom Sorting using key")
print("=" * 60)

students = [
    ("John", 85),
    ("Alice", 92),
    ("Bob", 78),
    ("David", 88)
]

print("Original List")
print(students)

print("\nSort by Marks")

by_marks = sorted(students, key=lambda x: x[1])
print(by_marks)

print("\nSort by Name")

by_name = sorted(students, key=lambda x: x[0])
print(by_name)

print("\nSort by Marks (Descending)")

desc = sorted(students, key=lambda x: x[1], reverse=True)
print(desc)


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ enumerate()
- Returns both index and value.
- Useful when looping with positions.

Syntax:
enumerate(iterable, start=0)

--------------------------------------------------

✔ zip()
- Combines multiple iterables element by element.

Syntax:
zip(list1, list2)

--------------------------------------------------

✔ any()
- Returns True if at least one element is True.

Examples:
any([0,0,5]) → True
any([0,0,0]) → False

--------------------------------------------------

✔ all()
- Returns True only if every element is True.

Examples:
all([2,4,6]) → True
all([2,4,7]) → False

--------------------------------------------------

✔ sorted()
- Returns a NEW sorted list.
- Original list remains unchanged.

✔ sort()
- Sorts the ORIGINAL list.
- Returns None.

--------------------------------------------------

✔ Custom Sorting using key

Examples:
sorted(list, key=lambda x: x[1])
sorted(list, key=len)
sorted(list, reverse=True)

--------------------------------------------------
Interview Tip:
sorted() works with lists, tuples, strings,
sets, dictionaries, etc.
sort() works ONLY with lists.
""")