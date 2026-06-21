# 🔹 DAY 21 - BANK MANAGEMENT SYSTEM

import csv
import os


class BankManagementSystem:

    ACCOUNTS_FILE = "accounts.csv"
    TRANSACTIONS_FILE = "transactions.csv"

    # =====================================
    # 🔹 Load Accounts
    # =====================================

    def load_accounts(self):

        accounts = []

        if os.path.exists(self.ACCOUNTS_FILE):

            with open(
                self.ACCOUNTS_FILE,
                "r",
                newline=""
            ) as file:

                reader = csv.reader(file)

                accounts = list(reader)

        return accounts

    # =====================================
    # 🔹 Save Accounts
    # =====================================

    def save_accounts(self, accounts):

        with open(
            self.ACCOUNTS_FILE,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerows(accounts)

    # =====================================
    # 🔹 Record Transaction
    # =====================================

    def record_transaction(
        self,
        account_number,
        transaction_type,
        amount
    ):

        with open(
            self.TRANSACTIONS_FILE,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                account_number,
                transaction_type,
                amount
            ])

    # =====================================
    # 🔹 Create Account
    # =====================================

    def create_account(self):

        account_number = input(
            "Enter Account Number: "
        )

        name = input(
            "Enter Account Holder Name: "
        )

        balance = input(
            "Enter Initial Balance: "
        )

        accounts = self.load_accounts()

        accounts.append([
            account_number,
            name,
            balance
        ])

        self.save_accounts(accounts)

        print("✅ Account Created")

    # =====================================
    # 🔹 Deposit
    # =====================================

    def deposit(self):

        account_number = input(
            "Enter Account Number: "
        )

        amount = float(
            input("Enter Amount: ")
        )

        accounts = self.load_accounts()

        found = False

        for account in accounts:

            if account[0] == account_number:

                balance = float(account[2])

                balance += amount

                account[2] = str(balance)

                self.record_transaction(
                    account_number,
                    "Deposit",
                    amount
                )

                found = True

                break

        if found:

            self.save_accounts(accounts)

            print("✅ Deposit Successful")

        else:

            print("❌ Account Not Found")

    # =====================================
    # 🔹 Withdraw
    # =====================================

    def withdraw(self):

        account_number = input(
            "Enter Account Number: "
        )

        amount = float(
            input("Enter Amount: ")
        )

        accounts = self.load_accounts()

        found = False

        for account in accounts:

            if account[0] == account_number:

                balance = float(account[2])

                if amount > balance:

                    print(
                        "❌ Insufficient Balance"
                    )

                    return

                balance -= amount

                account[2] = str(balance)

                self.record_transaction(
                    account_number,
                    "Withdraw",
                    amount
                )

                found = True

                break

        if found:

            self.save_accounts(accounts)

            print("✅ Withdrawal Successful")

        else:

            print("❌ Account Not Found")

    # =====================================
    # 🔹 Balance Enquiry
    # =====================================

    def balance_enquiry(self):

        account_number = input(
            "Enter Account Number: "
        )

        accounts = self.load_accounts()

        found = False

        for account in accounts:

            if account[0] == account_number:

                print(
                    f"💰 Current Balance: ₹{account[2]}"
                )

                found = True

                break

        if not found:

            print("❌ Account Not Found")

    # =====================================
    # 🔹 Transaction History
    # =====================================

    def transaction_history(self):

        account_number = input(
            "Enter Account Number: "
        )

        if not os.path.exists(
            self.TRANSACTIONS_FILE
        ):

            print("No Transactions Found")

            return

        found = False

        print("\n===== TRANSACTION HISTORY =====")

        with open(
            self.TRANSACTIONS_FILE,
            "r"
        ) as file:

            reader = csv.reader(file)

            for row in reader:

                if row[0] == account_number:

                    print(
                        f"{row[1]} : ₹{row[2]}"
                    )

                    found = True

        if not found:

            print("No Transactions Found")


# =====================================
# 🔹 MAIN PROGRAM
# =====================================

bank = BankManagementSystem()

while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")

    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Balance Enquiry")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        bank.create_account()

    elif choice == "2":

        bank.deposit()

    elif choice == "3":

        bank.withdraw()

    elif choice == "4":

        bank.balance_enquiry()

    elif choice == "5":

        bank.transaction_history()

    elif choice == "6":

        print("Goodbye 👋")

        break

    else:

        print("❌ Invalid Choice")