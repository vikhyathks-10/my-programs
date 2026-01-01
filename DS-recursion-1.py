# 1. Factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 2. Nth Fibonacci number using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 3. Reverse a string using recursion
def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]

# 4. Sum of digits using recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

# 5. Check if a number is palindrome using recursion
def is_palindrome(num, rev=0, temp=None):
    if temp is None:
        temp = num
    if num == 0:
        return rev == temp
    return is_palindrome(num // 10, rev * 10 + num % 10, temp)

# 6. Power(x, n) using recursion
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

# Test the functions
n = int(input("Enter a number: "))
print("Factorial:", factorial(n))
print("Fibonacci:", fibonacci(n))
print("Reverse string:", reverse_string(input("Enter a string: ")))
print("Sum of digits:", sum_of_digits(n))
print("Is Palindrome:", is_palindrome(n))
print("Power:", power(2, n))
