A = float(input("Enter first number: "))
B = float(input("Enter second number: "))
C = float(input("Enter third number: "))

if A >= B and A >= C:
    largest = A
elif B >= A and B >= C:
    largest = B
else:
    largest = C

print(f"The largest number is: {largest}")
