# 1️⃣ Function that returns sum of two numbers
def add(a, b):
    return a + b

print("Sum:", add(10, 20))


# 2️⃣ Function that returns factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("Factorial:", factorial(5))


# 3️⃣ Function that returns Fibonacci series
def fibonacci(n):
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print("Fibonacci Series:", fibonacci(7))


# 4️⃣ Function to check prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is Prime:", is_prime(11))


# 5️⃣ Function to return reverse of number
def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev

print("Reversed Number:", reverse_number(1234))
