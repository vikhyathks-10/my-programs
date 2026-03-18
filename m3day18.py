# -------- Custom Exception --------
class InvalidAmountError(Exception):
    pass


# -------- Main Program --------
balance = 10000
correct_username = "admin"
correct_password = "1234"
attempts = 3

while True:

    print("\n------ MINI PROJECT SYSTEM ------")
    print("1 ATM System")
    print("2 Bank Withdrawal")
    print("3 Student Marks Validator")
    print("4 Login System")
    print("5 Password Strength Checker")
    print("6 Custom Exception Demo")
    print("7 Exit")

    choice = input("Enter choice: ")

    # 1 ATM System
    if choice == "1":
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount > balance:
                raise ValueError("Insufficient balance!")

            balance -= amount
            print("Withdrawn:", amount)
            print("Remaining Balance:", balance)

        except ValueError as e:
            print("Error:", e)

    # 2 Bank Withdrawal
    elif choice == "2":
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                raise InvalidAmountError("Amount must be greater than zero!")

            if amount > balance:
                raise ValueError("Insufficient funds!")

            balance -= amount
            print("Withdrawal successful. Balance:", balance)

        except InvalidAmountError as e:
            print("Custom Error:", e)

        except ValueError as e:
            print("Error:", e)

    # 3 Student Marks Validator
    elif choice == "3":
        try:
            marks = int(input("Enter marks: "))

            if marks < 0 or marks > 100:
                raise ValueError("Marks must be between 0 and 100")

            print("Valid marks:", marks)

        except ValueError as e:
            print("Error:", e)

    # 4 Login System
    elif choice == "4":
        count = 0

        while count < attempts:
            user = input("Enter username: ")
            pwd = input("Enter password: ")

            if user == correct_username and pwd == correct_password:
                print("Login successful")
                break
            else:
                count += 1
                print("Invalid credentials. Attempts left:", attempts - count)

        if count == attempts:
            print("Account locked!")

    # 5 Password Strength Checker
    elif choice == "5":
        password = input("Enter password: ")

        try:
            if len(password) < 6:
                raise ValueError("Password too short!")

            if not any(c.isdigit() for c in password):
                raise ValueError("Password must contain a number!")

            if not any(c.isupper() for c in password):
                raise ValueError("Password must contain an uppercase letter!")

            print("Strong password")

        except ValueError as e:
            print("Weak Password:", e)

    # 6 Custom Exception Demo
    elif choice == "6":
        try:
            num = int(input("Enter positive number: "))

            if num < 0:
                raise InvalidAmountError("Negative value not allowed!")

            print("Valid number:", num)

        except InvalidAmountError as e:
            print("Custom Exception:", e)

    # Exit
    elif choice == "7":
        break

    else:
        print("Invalid choice")