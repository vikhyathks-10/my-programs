# 1️⃣ Odd or Even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 2️⃣ Largest of Two Numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest number is:", a)
elif b > a:
    print("Largest number is:", b)
else:
    print("Both numbers are equal")


# 3️⃣ Leap Year Check
year = int(input("\nEnter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")


# 4️⃣ Password Correct or Not
password = input("\nEnter password: ")
if password == "python123":
    print("Password is correct")
else:
    print("Incorrect password")


# 5️⃣ Temperature Hot or Cold
temp = float(input("\nEnter temperature in °C: "))
if temp >= 30:
    print("Hot weather")
else:
    print("Cold weather")