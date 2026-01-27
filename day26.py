# 1️⃣ Factorial using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number for factorial: "))
print("Factorial:", factorial(num))


# 2️⃣ Sum of First n Numbers using Recursion
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)

n = int(input("\nEnter n for sum of numbers: "))
print("Sum of first", n, "numbers:", sum_n(n))


# 3️⃣ Fibonacci using Recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("\nEnter number of Fibonacci terms: "))
print("Fibonacci series:")
for i in range(terms):
    print(fibonacci(i), end=" ")
print()


# 4️⃣ Power Calculation using Recursion
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

base = int(input("\nEnter base: "))
exp = int(input("Enter exponent: "))
print("Result:", power(base, exp))


# 5️⃣ Reverse String using Recursion
def reverse_string(s):
    if s == "":
        return s
    else:
        return reverse_string(s[1:]) + s[0]

text = input("\nEnter a string to reverse: ")
print("Reversed string:", reverse_string(text))
