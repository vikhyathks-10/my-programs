# 🔹 DAY 8 - BASIC PROGRAMS


# 🔹 1. Factorial (Recursive)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# 🔹 2. Fibonacci (Recursive)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# 🔹 3. Sum of Digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


# 🔹 4. Reverse Number
def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n = n // 10
    return rev


# 🔹 5. Power Calculation
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


# 🔹 MAIN PROGRAM

print("\n--- Factorial ---")
print("Factorial of 5:", factorial(5))

print("\n--- Fibonacci ---")
n = 6
print(f"Fibonacci series up to {n}:")
for i in range(n):
    print(fibonacci(i), end=" ")

print("\n\n--- Sum of Digits ---")
print("Sum of digits of 1234:", sum_of_digits(1234))

print("\n--- Reverse Number ---")
print("Reverse of 1234:", reverse_number(1234))

print("\n--- Power Calculation ---")
print("2^5 =", power(2, 5))