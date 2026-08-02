class BankAccount:
    bank = "State Bank of India"

    def __init__(self, holder, account_number, balance):
        self.holder = holder
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount:.2f} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")

    def get_balance(self):
        return self.__balance

    def show_balance(self):
        print(f"Current Balance: ₹{self.__balance:.2f}")

    def account_details(self):
        print("\n========== Account Details ==========")
        print("Bank           :", BankAccount.bank)
        print("Holder         :", self.holder)
        print("Account Number :", self.account_number)
        self.show_balance()


class SavingsAccount(BankAccount):
    def __init__(self, holder, account_number, balance):
        super().__init__(holder, account_number, balance)

    def add_interest(self):
        interest_rate = 0.04  # 4%
        interest = self.get_balance() * interest_rate

        print(f"\nAdding 4% Interest (₹{interest:.2f})...")
        self.deposit(interest)

    # Method Overriding
    def account_details(self):
        print("\n===== Savings Account Details =====")
        super().account_details()


# ---------------- MAIN PROGRAM ----------------

account = SavingsAccount(
    "Rahul",
    "SBI123456789",
    10000
)

account.account_details()

print("\nDepositing Money...")
account.deposit(3000)

print("\nWithdrawing Money...")
account.withdraw(2000)

account.add_interest()

print("\nFinal Account Details")
account.account_details()