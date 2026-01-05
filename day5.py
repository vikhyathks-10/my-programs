# 1️⃣ Check Pass or Fail
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")


# 2️⃣ Check Voting Eligibility
age = int(input("\nEnter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 3️⃣ Check Number is Zero or Not
num = int(input("\nEnter a number: "))
if num == 0:
    print("Number is Zero")
else:
    print("Number is Not Zero")


# 4️⃣ Check Character is Vowel
ch = input("\nEnter a character: ").lower()
if ch in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Not a vowel")


# 5️⃣ Check Number is Multiple of 5
n = int(input("\nEnter a number: "))
if n % 5 == 0:
    print("Multiple of 5")
else:
    print("Not a multiple of 5")
