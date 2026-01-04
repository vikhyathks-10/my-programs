# DAY 4 – Operators

# 1. Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 2. Positive or Negative
num2 = int(input("\nEnter a number: "))
if num2 > 0:
    print("Positive number")
elif num2 < 0:
    print("Negative number")
else:
    print("Zero")

# 3. Greater of two numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Greater number:", a)
elif b > a:
    print("Greater number:", b)
else:
    print("Both numbers are equal")

# 4. Greater of three numbers
x = int(input("\nEnter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x >= y and x >= z:
    print("Greatest number:", x)
elif y >= x and y >= z:
    print("Greatest number:", y)
else:
    print("Greatest number:", z)

# 5. Swap two numbers
p = int(input("\nEnter first number to swap: "))
q = int(input("Enter second number to swap: "))

print("Before swap:", p, q)

p, q = q, p   # Python swap
print("After swap:", p, q)
