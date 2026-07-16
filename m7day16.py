# ==========================================================
# Month 7 - Day 16
# functools & heapq
#
# Topics Covered:
# 1. lru_cache
# 2. partial
# 3. reduce()
# 4. Min Heap
# 5. Max Heap
# 6. Top K Largest Elements
# ==========================================================

from functools import lru_cache, partial, reduce
import heapq
import operator

print("=" * 60)
print("1. lru_cache")
print("=" * 60)

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

num = 10

print(f"Fibonacci({num}) =", fibonacci(num))

print("Cache Info:")
print(fibonacci.cache_info())


print("\n" + "=" * 60)
print("2. partial()")
print("=" * 60)

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print("Square of 5 :", square(5))
print("Cube of 4   :", cube(4))


print("\n" + "=" * 60)
print("3. reduce()")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

sum_result = reduce(operator.add, numbers)
product_result = reduce(operator.mul, numbers)

print("Numbers :", numbers)
print("Sum     :", sum_result)
print("Product :", product_result)


print("\n" + "=" * 60)
print("4. MIN HEAP")
print("=" * 60)

numbers = [10, 4, 15, 20, 8]

heapq.heapify(numbers)

print("Heap :", numbers)

print("Smallest Element :", heapq.heappop(numbers))

print("Heap After Pop :", numbers)


print("\n" + "=" * 60)
print("5. MAX HEAP")
print("=" * 60)

numbers = [10, 4, 15, 20, 8]

max_heap = [-num for num in numbers]

heapq.heapify(max_heap)

largest = -heapq.heappop(max_heap)

print("Original :", numbers)
print("Largest Element :", largest)


print("\n" + "=" * 60)
print("6. TOP K LARGEST ELEMENTS")
print("=" * 60)

nums = [12, 5, 8, 20, 17, 3, 25, 10]

k = 3

top_k = heapq.nlargest(k, nums)

print("Array :", nums)
print(f"Top {k} Largest :", top_k)


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ functools

Useful Functions

• lru_cache
• partial
• reduce

--------------------------------------------------

✔ lru_cache

Caches function results.

Useful for:

• Dynamic Programming
• Recursion
• Memoization

Syntax

@lru_cache(maxsize=None)

--------------------------------------------------

✔ partial

Creates a new function
by fixing some arguments.

Example

square = partial(power, exponent=2)

--------------------------------------------------

✔ reduce()

Combines all elements
into a single value.

Requires

from functools import reduce

--------------------------------------------------

✔ heapq

Python implements

Min Heap

Important Functions

heapify()

heappush()

heappop()

nlargest()

nsmallest()

--------------------------------------------------

✔ Max Heap

Python has no built-in
Max Heap.

Use:

Negative values

--------------------------------------------------

✔ Top K Elements

heapq.nlargest(k, iterable)

Time

O(n log k)

--------------------------------------------------

Interview Tip

Whenever you hear:

✔ Top K
✔ Highest
✔ Lowest
✔ Priority Queue

Think:

👉 Heap

Whenever you hear:

✔ Memoization

Think:

👉 lru_cache
""")