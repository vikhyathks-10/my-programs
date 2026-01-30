# ===============================
# 1️⃣ ATM Simulation
# ===============================
balance = 10000
print("ATM Simulation")
print("1. Check Balance\n2. Deposit\n3. Withdraw")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Current Balance:", balance)

elif choice == 2:
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print("Updated Balance:", balance)

elif choice == 3:
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance -= amount
        print("Updated Balance:", balance)
    else:
        print("Insufficient balance")

else:
    print("Invalid choice")


# ===============================
# 2️⃣ Simple Login System
# ===============================
print("\nSimple Login System")
username = "admin"
password = "python123"

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login successful")
else:
    print("Login failed")


# ===============================
# 3️⃣ Number Guessing Game
# ===============================
print("\nNumber Guessing Game")
secret = 7

while True:
    guess = int(input("Guess the number (1–10): "))
    if guess == secret:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong guess, try again")


# ===============================
# 4️⃣ Student Report Card
# ===============================
print("\nStudent Report Card")
name = input("Enter student name: ")
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

total = m1 + m2 + m3
average = total / 3

print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 75:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")


# ===============================
# 5️⃣ Menu-Driven Calculator
# ===============================
print("\nMenu-Driven Calculator")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

ch = int(input("Enter choice: "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if ch == 1:
    print("Result:", a + b)
elif ch == 2:
    print("Result:", a - b)
elif ch == 3:
    print("Result:", a * b)
elif ch == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid choice")
