# 1️⃣ Factorial of a Number
num = int(input("Enter a number for factorial: "))
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print("Factorial:", fact)


# 2️⃣ Reverse a Number
n = int(input("\nEnter a number to reverse: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reversed number:", rev)


# 3️⃣ Sum of Digits
n = int(input("\nEnter a number to find sum of digits: "))
sum_digits = 0

while n > 0:
    sum_digits += n % 10
    n //= 10

print("Sum of digits:", sum_digits)


# 4️⃣ Palindrome Number
n = int(input("\nEnter a number to check palindrome: "))
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10

if temp == rev:
    print("Palindrome number")
else:
    print("Not a palindrome")


# 5️⃣ Count Digits
n = int(input("\nEnter a number to count digits: "))
count = 0

while n > 0:
    count += 1
    n //= 10

print("Number of digits:", count)
