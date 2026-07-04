# ==========================================================
# Month 7 - Day 4
# Python Internals
#
# Topics Covered:
# 1. Deep Copy vs Shallow Copy
# 2. Memory Address Demonstration
# 3. String Interning
# 4. Immutable String Demo
# 5. Reference Counting Demo
# 6. Object Identity Practice
# ==========================================================

import copy
import sys

print("=" * 60)
print("1. DEEP COPY vs SHALLOW COPY")
print("=" * 60)

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 100

print("Original :", original)
print("Shallow  :", shallow)
print("Deep     :", deep)

print("\nObservation:")
print("Shallow copy shares nested objects.")
print("Deep copy creates completely independent objects.")


print("\n" + "=" * 60)
print("2. MEMORY ADDRESS DEMONSTRATION")
print("=" * 60)

a = [10, 20, 30]
b = a
c = a.copy()

print("id(a) =", id(a))
print("id(b) =", id(b))
print("id(c) =", id(c))

print("\na is b :", a is b)
print("a is c :", a is c)


print("\n" + "=" * 60)
print("3. STRING INTERNING")
print("=" * 60)

s1 = "Python"
s2 = "Python"

print("s1 =", s1)
print("s2 =", s2)

print("id(s1) =", id(s1))
print("id(s2) =", id(s2))

print("s1 is s2 :", s1 is s2)

# Runtime-created string
s3 = "".join(["Py", "thon"])

print("\nRuntime String:", s3)
print("s1 == s3 :", s1 == s3)
print("s1 is s3 :", s1 is s3)


print("\n" + "=" * 60)
print("4. IMMUTABLE STRING DEMO")
print("=" * 60)

text = "Hello"

print("Before Modification")
print(text)
print(id(text))

text += " World"

print("\nAfter Modification")
print(text)
print(id(text))

print("\nObservation:")
print("A new string object is created.")


print("\n" + "=" * 60)
print("5. REFERENCE COUNTING")
print("=" * 60)

x = []

print("Reference Count Initially:")
print(sys.getrefcount(x))

y = x
print("\nAfter assigning y = x")
print(sys.getrefcount(x))

z = x
print("\nAfter assigning z = x")
print(sys.getrefcount(x))

del y
print("\nAfter deleting y")
print(sys.getrefcount(x))


print("\n" + "=" * 60)
print("6. OBJECT IDENTITY PRACTICE")
print("=" * 60)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2 :", list1 == list2)
print("list1 is list2 :", list1 is list2)

print()

print("list1 == list3 :", list1 == list3)
print("list1 is list3 :", list1 is list3)

print()

print("Memory Addresses")
print(id(list1))
print(id(list2))
print(id(list3))


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ Shallow Copy
- Copies only the outer object.
- Nested objects are shared.

copy.copy()

--------------------------------------------

✔ Deep Copy
- Copies everything recursively.
- Completely independent copy.

copy.deepcopy()

--------------------------------------------

✔ id(object)
Returns the memory address (identity)
of an object.

--------------------------------------------

✔ String Interning
- Python stores identical immutable
  strings efficiently.
- Sometimes two identical strings
  point to the same memory.

--------------------------------------------

✔ Strings are Immutable
Operations like:

text += "abc"

create a NEW object.

--------------------------------------------

✔ Reference Counting

sys.getrefcount(obj)

Returns the number of references
to an object.

Python automatically frees memory
when reference count becomes zero.

--------------------------------------------

✔ ==

Compares values.

✔ is

Compares object identity (memory address).

--------------------------------------------

Interview Tip:
Use

==

when comparing values.

Use

is

when checking if two variables
refer to the exact same object.
""")