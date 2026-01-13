# 1️⃣ Stop loop at 5
print("Stop loop at 5:")
for i in range(1, 11):
    if i == 5:
        break
    print(i)


# 2️⃣ Skip number 3
print("\nSkip number 3:")
for i in range(1, 11):
    if i == 3:
        continue
    print(i)


# 3️⃣ Find first multiple of 7
print("\nFirst multiple of 7:")
for i in range(1, 101):
    if i % 7 == 0:
        print(i)
        break


# 4️⃣ Print until user enters 0
print("\nEnter numbers (0 to stop):")
while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break
    print("You entered:", n)


# 5️⃣ Password Retry System
correct_password = "python123"

while True:
    pwd = input("\nEnter password: ")
    if pwd == correct_password:
        print("Access Granted")
        break
    else:
        print("Wrong password, try again")

