# 1️⃣ Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print("Largest number is:", a)
    else:
        print("Largest number is:", c)
else:
    if b > c:
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)


# 2️⃣ Smallest of Three Numbers
x = int(input("\nEnter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x < y:
    if x < z:
        print("Smallest number is:", x)
    else:
        print("Smallest number is:", z)
else:
    if y < z:
        print("Smallest number is:", y)
    else:
        print("Smallest number is:", z)


# 3️⃣ Triangle Validity Check
a = int(input("\nEnter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a > 0 and b > 0 and c > 0:
    if a + b + c == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")
else:
    print("Angles must be greater than zero")


# 4️⃣ Scholarship Eligibility
marks = int(input("\nEnter marks: "))
income = int(input("Enter family income: "))

if marks >= 80:
    if income <= 300000:
        print("Eligible for Scholarship")
    else:
        print("Not eligible due to income")
else:
    print("Not eligible due to marks")


# 5️⃣ Exam Result System
marks = int(input("\nEnter exam marks: "))

if marks >= 40:
    if marks >= 75:
        print("Pass with Distinction")
    else:
        print("Pass")
else:
    print("Fail")
