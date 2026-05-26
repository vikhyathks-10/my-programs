# 🔹 DAY 26 - ATM MINI PROJECT


class ATM:

    def __init__(self):

        self.username = "vikyat"
        self.password = "1234"

        self.balance = 1000

        self.transactions = []

    # 🔹 User Login
    def login(self):

        print("\n--- ATM LOGIN ---")

        user = input("Enter Username: ")
        pwd = input("Enter Password: ")

        if user == self.username and pwd == self.password:

            print("Login Successful")
            return True

        else:
            print("Invalid Credentials")
            return False

    # 🔹 Deposit Function
    def deposit(self):

        amount = float(input("Enter Deposit Amount: "))

        if amount > 0:

            self.balance += amount

            self.transactions.append(
                f"Deposited ₹{amount}"
            )

            print("Amount Deposited Successfully")

        else:
            print("Invalid Amount")

    # 🔹 Withdraw Function
    def withdraw(self):

        amount = float(input("Enter Withdraw Amount: "))

        if amount <= self.balance:

            self.balance -= amount

            self.transactions.append(
                f"Withdrawn ₹{amount}"
            )

            print("Withdrawal Successful")

        else:
            print("Insufficient Balance")

    # 🔹 Balance Check
    def check_balance(self):

        print(f"Current Balance: ₹{self.balance}")

    # 🔹 Transaction History
    def show_transactions(self):

        print("\n--- Transaction History ---")

        if not self.transactions:
            print("No Transactions Found")

        else:

            for transaction in self.transactions:
                print(transaction)


# 🔹 MAIN PROGRAM

atm = ATM()

if atm.login():

    while True:

        print("\n====== ATM MENU ======")

        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            atm.deposit()

        elif choice == "2":

            atm.withdraw()

        elif choice == "3":

            atm.check_balance()

        elif choice == "4":

            atm.show_transactions()

        elif choice == "5":

            print("Thank You for Using ATM")
            break

        else:
            print("Invalid Choice")