# 1️⃣ Simple Function
def simple_function():
    print("Hello! This is a simple function.")

simple_function()


# 2️⃣ Add Function
def add(a, b):
    return a + b

result = add(10, 20)
print("\nAddition result:", result)


# 3️⃣ Even / Odd Function
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("\nEnter a number: "))
print("The number is:", even_odd(num))


# 4️⃣ Factorial Function
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input("\nEnter a number for factorial: "))
print("Factorial:", factorial(n))


# 5️⃣ Prime Check Function
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

p = int(input("\nEnter a number to check prime: "))
if is_prime(p):
    print("Prime number")
else:
    print("Not a prime number")
