# 🔹 DAY 9 PROGRAMS


# 🔹 1. GCD using Recursion (Euclidean Algorithm)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# 🔹 2. Count Digits (Recursion)
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)


# 🔹 3. Palindrome Check
def is_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return original == rev


# 🔹 4. Product of Array (Recursion)
def product_array(arr, n):
    if n == 0:
        return 1
    return arr[n-1] * product_array(arr, n-1)


# 🔹 5. Sum of Array (Recursion)
def sum_array(arr, n):
    if n == 0:
        return 0
    return arr[n-1] + sum_array(arr, n-1)


# 🔹 MAIN PROGRAM

print("\n--- GCD ---")
print("GCD of 48 and 18:", gcd(48, 18))


print("\n--- Count Digits ---")
print("Digits in 12345:", count_digits(12345))


print("\n--- Palindrome Check ---")
num = 121
if is_palindrome(num):
    print(num, "is Palindrome")
else:
    print(num, "is Not Palindrome")


print("\n--- Product of Array ---")
arr = [1, 2, 3, 4]
print("Product:", product_array(arr, len(arr)))


print("\n--- Sum of Array ---")
print("Sum:", sum_array(arr, len(arr)))