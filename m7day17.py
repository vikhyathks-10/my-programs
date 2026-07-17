# ==========================================================
# Month 7 - Day 17
# Python bisect & math Module
#
# Topics Covered:
# 1. Binary Insert (bisect.insort)
# 2. Search Position (bisect_left & bisect_right)
# 3. Greatest Common Divisor (GCD)
# 4. Least Common Multiple (LCM)
# 5. Prime Number Optimization
# 6. Fast Power (Binary Exponentiation)
# ==========================================================

import bisect
import math

print("=" * 60)
print("1. BINARY INSERT (bisect.insort)")
print("=" * 60)

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

bisect.insort(numbers, 35)

print("After Inserting 35:", numbers)


print("\n" + "=" * 60)
print("2. SEARCH POSITION")
print("=" * 60)

numbers = [10, 20, 30, 40, 50]

left = bisect.bisect_left(numbers, 30)
right = bisect.bisect_right(numbers, 30)

print("Array:", numbers)
print("bisect_left(30) :", left)
print("bisect_right(30):", right)

position = bisect.bisect_left(numbers, 25)

print("Insertion Position for 25:", position)


print("\n" + "=" * 60)
print("3. GREATEST COMMON DIVISOR (GCD)")
print("=" * 60)

a = 48
b = 18

gcd = math.gcd(a, b)

print(f"GCD({a}, {b}) =", gcd)


print("\n" + "=" * 60)
print("4. LEAST COMMON MULTIPLE (LCM)")
print("=" * 60)

a = 12
b = 18

lcm = math.lcm(a, b)

print(f"LCM({a}, {b}) =", lcm)


print("\n" + "=" * 60)
print("5. PRIME NUMBER OPTIMIZATION")
print("=" * 60)

number = 97

is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a Prime Number")
else:
    print(number, "is NOT a Prime Number")


print("\n" + "=" * 60)
print("6. FAST POWER (Binary Exponentiation)")
print("=" * 60)

base = 2
exponent = 10

result = 1

b = base
e = exponent

while e > 0:

    if e % 2 == 1:
        result *= b

    b *= b
    e //= 2

print(f"{base}^{exponent} =", result)


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ bisect Module

Used for Binary Search operations
on sorted lists.

Import

import bisect

--------------------------------------------------

✔ bisect_left()

Returns the leftmost insertion index.

Example

[10,20,30,40]

bisect_left(30)

returns

2

--------------------------------------------------

✔ bisect_right()

Returns the rightmost insertion index.

Useful for duplicate values.

--------------------------------------------------

✔ insort()

Inserts while maintaining
sorted order.

Time

O(n)

--------------------------------------------------

✔ math.gcd()

Greatest Common Divisor

Time

O(log n)

--------------------------------------------------

✔ math.lcm()

Least Common Multiple

Formula

LCM(a,b)

--------------------------------------------------

✔ Prime Optimization

Instead of checking till n,

check till

√n

Time

O(√n)

--------------------------------------------------

✔ Binary Exponentiation

Repeated squaring.

Time

O(log n)

Instead of

O(n)

--------------------------------------------------

Interview Tip

Whenever you hear:

✔ Sorted Array
✔ Insertion Position

Think:

👉 bisect

Whenever you hear:

✔ Large Powers

Think:

👉 Binary Exponentiation

Whenever you hear:

✔ Factors

Think:

👉 GCD / LCM
""")