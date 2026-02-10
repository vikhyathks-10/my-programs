# 1️⃣ Function with Default Argument
def greet(name="User"):
    print("Hello", name)

greet()
greet("Vikyt")


# 2️⃣ Function to Calculate Bill with Default Tax
def calculate_bill(amount, tax=5):
    return amount + (amount * tax / 100)

print("Total Bill:", calculate_bill(1000))
print("Total Bill with custom tax:", calculate_bill(1000, 10))


# 3️⃣ Calculator Using Functions (Menu-Driven)
def calculator():
    print("\nCalculator Menu")
    print("1.Add  2.Sub  3.Mul  4.Div")
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
            print("Division not allowed")
    else:
        print("Invalid choice")

calculator()


# 4️⃣ Student Marks System Using Functions
def student_result(name, m1, m2, m3):
    total = m1 + m2 + m3
    avg = total / 3
    print("\nStudent:", name)
    print("Total:", total)
    print("Average:", avg)

student_result("Rahul", 70, 80, 75)


# 5️⃣ ATM Simulation Using Functions
balance = 5000

def atm():
    global balance
    print("\nATM Menu")
    print("1.Check Balance  2.Deposit  3.Withdraw")
    ch = int(input("Enter choice: "))

    if ch == 1:
        print("Balance:", balance)
    elif ch == 2:
        amt = int(input("Enter deposit amount: "))
        balance += amt
        print("Updated Balance:", balance)
    elif ch == 3:
        amt = int(input("Enter withdraw amount: "))
        if amt <= balance:
            balance -= amt
            print("Updated Balance:", balance)
        else:
            print("Insufficient balance")
    else:
        print("Invalid choice")

atm()
