"""Common Python Coding Interview Questions and Solutions
1. Reverse a string without using slicing
s = "hello"
rev = ""
for char in s:
    rev = char + rev
print("Reversed:", rev)

2. Factorial of a number

Using loop:

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)


Using recursion:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print("Factorial:", factorial(5))

3. Check if a number is prime
n = 29
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

4. Fibonacci sequence up to n terms
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b

5. Find largest and smallest number in a list
nums = [5, 8, 2, 9, 1, 7]
print("Largest:", max(nums))
print("Smallest:", min(nums))

6. Count vowels in a string
s = "Programming"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowel count:", count)

7. Check palindrome string
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

8. Sum of digits of a number
n = 12345
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Sum of digits:", total)

9. Find second largest element in a list
nums = [10, 20, 4, 45, 99]
unique_nums = list(set(nums))   # remove duplicates
unique_nums.sort()
print("Second largest:", unique_nums[-2])

10. Remove duplicates from a list
nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))
print("Without duplicates:", unique)

"""