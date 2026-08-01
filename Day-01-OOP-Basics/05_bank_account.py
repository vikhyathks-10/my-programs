class BankAccount:

    bank = "State Bank of India"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited :", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn :", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Holder :", self.holder)
        print("Balance :", self.balance)
        print("Bank :", BankAccount.bank)


acc = BankAccount("Rahul", 10000)

acc.deposit(3000)
acc.withdraw(2000)
acc.display()