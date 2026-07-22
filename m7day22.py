# ==========================================================
# Month 7 - Day 22
# Advanced Python Features
#
# Topics Covered:
# 1. Decorators
# 2. Generators
# 3. Iterators
# 4. Context Managers
# 5. Closures
# 6. Function Annotations
# ==========================================================

from contextlib import contextmanager

print("=" * 60)
print("1. DECORATORS")
print("=" * 60)

def decorator(func):

    def wrapper():
        print("Before Function Call")
        func()
        print("After Function Call")

    return wrapper


@decorator
def greet():
    print("Hello, Python!")

greet()


print("\n" + "=" * 60)
print("2. GENERATORS")
print("=" * 60)

def fibonacci(n):

    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b

print("First 10 Fibonacci Numbers:")

for num in fibonacci(10):
    print(num, end=" ")

print()


print("\n" + "=" * 60)
print("3. ITERATORS")
print("=" * 60)

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("Iterator Finished!")


print("\n" + "=" * 60)
print("4. CONTEXT MANAGER")
print("=" * 60)

@contextmanager
def message():

    print("Opening Resource")

    try:
        yield

    finally:
        print("Closing Resource")

with message():
    print("Working Inside Context Manager")


print("\n" + "=" * 60)
print("5. CLOSURES")
print("=" * 60)

def multiplier(x):

    def multiply(y):
        return x * y

    return multiply

double = multiplier(2)
triple = multiplier(3)

print("Double of 10:", double(10))
print("Triple of 10:", triple(10))


print("\n" + "=" * 60)
print("6. FUNCTION ANNOTATIONS")
print("=" * 60)

def add(a: int, b: int) -> int:
    return a + b

print("Addition:", add(15, 25))
print("Annotations:", add.__annotations__)


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ Decorators

Used to modify or extend
the behavior of functions
without changing their code.

Syntax

@decorator

--------------------------------------------------

✔ Generators

Functions that use

yield

instead of return.

Advantages

• Memory Efficient
• Lazy Evaluation

--------------------------------------------------

✔ Iterators

Objects that implement

__iter__()
__next__()

Use

iter()

next()

--------------------------------------------------

✔ Context Manager

Handles resource management
automatically.

Example

with open(...)

Can also create custom
context managers using

@contextmanager

--------------------------------------------------

✔ Closures

A nested function that
remembers variables from
its enclosing scope.

Useful for

• Function factories
• Callbacks
• Data hiding

--------------------------------------------------

✔ Function Annotations

Provide type hints.

Example

def add(a: int, b: int) -> int

Annotations improve

✔ Readability
✔ IDE Support
✔ Static Analysis

--------------------------------------------------

Interview Tip

Difference

return
→ Ends function

yield
→ Pauses function and
returns next value on demand.

--------------------------------------------------

Most Asked Questions

✔ Decorators
✔ Generators
✔ yield vs return
✔ Iterators
✔ Context Managers
✔ Closures
✔ Type Hints
""")