import sqlite3
from datetime import datetime


# ==========================================
# DATABASE CONNECTION
# ==========================================

conn = sqlite3.connect("banking.db")
cursor = conn.cursor()


# ==========================================
# CREATE TABLES
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts(
    account_number INTEGER PRIMARY KEY,
    holder_name TEXT NOT NULL,
    account_type TEXT NOT NULL,
    balance REAL NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number INTEGER NOT NULL,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL,
    transaction_date TEXT NOT NULL
)
""")

conn.commit()


# ==========================================
# BANK ACCOUNT CLASS
# ==========================================

class BankAccount:

    def __init__(
        self,
        account_number,
        holder_name,
        account_type,
        balance
    ):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = balance

    # --------------------------------------
    # CREATE ACCOUNT
    # --------------------------------------

    def create_account(self):

        cursor.execute(
            "SELECT account_number FROM accounts WHERE account_number=?",
            (self.account_number,)
        )

        existing = cursor.fetchone()

        if existing:
            print("\nAccount number already exists.")
            return

        if self.balance < 0:
            print("\nInitial balance cannot be negative.")
            return

        cursor.execute("""
            INSERT INTO accounts
            VALUES (?, ?, ?, ?)
        """, (
            self.account_number,
            self.holder_name,
            self.account_type,
            self.balance
        ))

        conn.commit()

        print("\nAccount Created Successfully!")

        if self.balance > 0:
            self.add_transaction(
                "Initial Deposit",
                self.balance
            )

    # --------------------------------------
    # ADD TRANSACTION
    # --------------------------------------

    def add_transaction(self, transaction_type, amount):

        transaction_date = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        cursor.execute("""
            INSERT INTO transactions
            (account_number, transaction_type, amount, transaction_date)
            VALUES (?, ?, ?, ?)
        """, (
            self.account_number,
            transaction_type,
            amount,
            transaction_date
        ))

        conn.commit()

    # --------------------------------------
    # GET ACCOUNT
    # --------------------------------------

    @staticmethod
    def get_account(account_number):

        cursor.execute("""
            SELECT *
            FROM accounts
            WHERE account_number=?
        """, (account_number,))

        return cursor.fetchone()

    # --------------------------------------
    # DEPOSIT
    # --------------------------------------

    def deposit(self, amount):

        if amount <= 0:
            print("\nDeposit amount must be greater than zero.")
            return

        account = self.get_account(self.account_number)

        if not account:
            print("\nAccount not found.")
            return

        new_balance = account[3] + amount

        cursor.execute("""
            UPDATE accounts
            SET balance=?
            WHERE account_number=?
        """, (
            new_balance,
            self.account_number
        ))

        conn.commit()

        self.add_transaction("Deposit", amount)

        print(
            f"\n₹{amount:.2f} deposited successfully."
        )

        print(
            f"Current Balance: ₹{new_balance:.2f}"
        )

    # --------------------------------------
    # WITHDRAW
    # --------------------------------------

    def withdraw(self, amount):

        if amount <= 0:
            print("\nWithdrawal amount must be greater than zero.")
            return

        account = self.get_account(self.account_number)

        if not account:
            print("\nAccount not found.")
            return

        current_balance = account[3]

        if amount > current_balance:
            print("\nInsufficient balance.")
            return

        new_balance = current_balance - amount

        cursor.execute("""
            UPDATE accounts
            SET balance=?
            WHERE account_number=?
        """, (
            new_balance,
            self.account_number
        ))

        conn.commit()

        self.add_transaction("Withdrawal", amount)

        print(
            f"\n₹{amount:.2f} withdrawn successfully."
        )

        print(
            f"Current Balance: ₹{new_balance:.2f}"
        )

    # --------------------------------------
    # CHECK BALANCE
    # --------------------------------------

    def show_balance(self):

        account = self.get_account(self.account_number)

        if account:

            print("\n========== BALANCE ==========")
            print("Account Number :", account[0])
            print("Holder Name    :", account[1])
            print("Balance        :", f"₹{account[3]:.2f}")

        else:
            print("\nAccount not found.")

    # --------------------------------------
    # ACCOUNT DETAILS
    # --------------------------------------

    def show_details(self):

        account = self.get_account(self.account_number)

        if account:

            print("\n========== ACCOUNT DETAILS ==========")
            print("Account Number :", account[0])
            print("Holder Name    :", account[1])
            print("Account Type   :", account[2])
            print("Balance        :", f"₹{account[3]:.2f}")

        else:
            print("\nAccount not found.")

    # --------------------------------------
    # TRANSACTION HISTORY
    # --------------------------------------

    def transaction_history(self):

        cursor.execute("""
            SELECT transaction_type, amount, transaction_date
            FROM transactions
            WHERE account_number=?
            ORDER BY transaction_id DESC
        """, (self.account_number,))

        transactions = cursor.fetchall()

        if not transactions:
            print("\nNo transactions found.")
            return

        print("\n========== TRANSACTION HISTORY ==========")

        for transaction in transactions:

            print(
                f"Type: {transaction[0]}"
            )

            print(
                f"Amount: ₹{transaction[1]:.2f}"
            )

            print(
                f"Date: {transaction[2]}"
            )

            print("-" * 40)


# ==========================================
# CREATE ACCOUNT FUNCTION
# ==========================================

def create_new_account():

    try:

        account_number = int(
            input("Enter Account Number: ")
        )

        holder_name = input(
            "Enter Account Holder Name: "
        )

        account_type = input(
            "Enter Account Type (Savings/Current): "
        )

        account_type = account_type.title()

        if account_type not in ["Savings", "Current"]:

            print("\nInvalid account type.")
            return

        balance = float(
            input("Enter Initial Deposit: ")
        )

        account = BankAccount(
            account_number,
            holder_name,
            account_type,
            balance
        )

        account.create_account()

    except ValueError:

        print("\nPlease enter valid values.")


# ==========================================
# FIND ACCOUNT
# ==========================================

def get_account_object():

    try:

        account_number = int(
            input("Enter Account Number: ")
        )

        account_data = BankAccount.get_account(
            account_number
        )

        if not account_data:

            print("\nAccount not found.")
            return None

        return BankAccount(
            account_data[0],
            account_data[1],
            account_data[2],
            account_data[3]
        )

    except ValueError:

        print("\nInvalid account number.")
        return None


# ==========================================
# TRANSFER MONEY
# ==========================================

def transfer_money():

    try:

        sender_number = int(
            input("Sender Account Number: ")
        )

        receiver_number = int(
            input("Receiver Account Number: ")
        )

        amount = float(
            input("Transfer Amount: ")
        )

        if amount <= 0:

            print("\nAmount must be greater than zero.")
            return

        sender = BankAccount.get_account(
            sender_number
        )

        receiver = BankAccount.get_account(
            receiver_number
        )

        if not sender:

            print("\nSender account not found.")
            return

        if not receiver:

            print("\nReceiver account not found.")
            return

        if sender_number == receiver_number:

            print("\nSender and receiver cannot be the same.")
            return

        if sender[3] < amount:

            print("\nInsufficient sender balance.")
            return

        sender_balance = sender[3] - amount
        receiver_balance = receiver[3] + amount

        cursor.execute("""
            UPDATE accounts
            SET balance=?
            WHERE account_number=?
        """, (
            sender_balance,
            sender_number
        ))

        cursor.execute("""
            UPDATE accounts
            SET balance=?
            WHERE account_number=?
        """, (
            receiver_balance,
            receiver_number
        ))

        date = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        cursor.execute("""
            INSERT INTO transactions
            (account_number, transaction_type, amount, transaction_date)
            VALUES (?, ?, ?, ?)
        """, (
            sender_number,
            "Transfer Sent",
            amount,
            date
        ))

        cursor.execute("""
            INSERT INTO transactions
            (account_number, transaction_type, amount, transaction_date)
            VALUES (?, ?, ?, ?)
        """, (
            receiver_number,
            "Transfer Received",
            amount,
            date
        ))

        conn.commit()

        print("\nTransfer Successful!")
        print(f"Amount: ₹{amount:.2f}")

    except ValueError:

        print("\nInvalid input.")


# ==========================================
# DELETE ACCOUNT
# ==========================================

def delete_account():

    try:

        account_number = int(
            input("Enter Account Number: ")
        )

        account = BankAccount.get_account(
            account_number
        )

        if not account:

            print("\nAccount not found.")
            return

        print(
            f"\nAccount Holder: {account[1]}"
        )

        confirmation = input(
            "Are you sure? (y/n): "
        ).lower()

        if confirmation == "y":

            cursor.execute("""
                DELETE FROM transactions
                WHERE account_number=?
            """, (account_number,))

            cursor.execute("""
                DELETE FROM accounts
                WHERE account_number=?
            """, (account_number,))

            conn.commit()

            print("\nAccount Deleted Successfully!")

        else:

            print("\nDeletion Cancelled.")


    except ValueError:

        print("\nInvalid account number.")


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n")
    print("=" * 50)
    print("           BANKING MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Create Account")
    print("2. Account Details")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Transfer Money")
    print("7. Transaction History")
    print("8. Delete Account")
    print("9. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        create_new_account()

    elif choice == "2":

        account = get_account_object()

        if account:
            account.show_details()

    elif choice == "3":

        account = get_account_object()

        if account:

            try:
                amount = float(
                    input("Enter Deposit Amount: ")
                )

                account.deposit(amount)

            except ValueError:
                print("\nInvalid amount.")

    elif choice == "4":

        account = get_account_object()

        if account:

            try:
                amount = float(
                    input("Enter Withdrawal Amount: ")
                )

                account.withdraw(amount)

            except ValueError:
                print("\nInvalid amount.")

    elif choice == "5":

        account = get_account_object()

        if account:
            account.show_balance()

    elif choice == "6":

        transfer_money()

    elif choice == "7":

        account = get_account_object()

        if account:
            account.transaction_history()

    elif choice == "8":

        delete_account()

    elif choice == "9":

        print("\nThank you for using the Banking System!")
        break

    else:

        print("\nInvalid Choice. Please try again.")


conn.close()