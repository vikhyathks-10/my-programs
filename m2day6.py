# 6️⃣ Number System Converter Using Functions
def decimal_to_binary(n):
    return bin(n)[2:]

print("Binary:", decimal_to_binary(10))


# 7️⃣ Temperature Converter Using Functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print("Temperature in Fahrenheit:", celsius_to_fahrenheit(30))


# 8️⃣ Area Calculator Using Menu
def area_calculator():
    print("\nArea Menu")
    print("1.Circle  2.Rectangle")
    ch = int(input("Enter choice: "))

    if ch == 1:
        r = float(input("Enter radius: "))
        print("Area of circle:", 3.14 * r * r)
    elif ch == 2:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        print("Area of rectangle:", l * b)
    else:
        print("Invalid choice")

area_calculator()


# 9️⃣ Banking Menu (Deposit / Withdraw)
bank_balance = 3000

def banking():
    global bank_balance
    print("\nBank Menu")
    print("1.Deposit  2.Withdraw")
    ch = int(input("Enter choice: "))

    if ch == 1:
        amt = int(input("Enter amount: "))
        bank_balance += amt
    elif ch == 2:
        amt = int(input("Enter amount: "))
        if amt <= bank_balance:
            bank_balance -= amt
        else:
            print("Insufficient balance")
    print("Balance:", bank_balance)

banking()


# 🔟 Login System Using Functions
def login():
    user = "admin"
    pwd = "python123"

    u = input("\nEnter username: ")
    p = input("Enter password: ")

    if u == user and p == pwd:
        print("Login successful")
    else:
        print("Login failed")

login()
