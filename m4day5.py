# 🔹 ABSTRACTION - ALL IN ONE PROGRAM

from abc import ABC, abstractmethod


# 🔹 ABSTRACT CLASS (Interface-like structure)
class Bank(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


# 🔹 ANOTHER ABSTRACT CLASS (Multiple Abstract Classes)
class Loan(ABC):

    @abstractmethod
    def apply_loan(self, amount):
        pass


# 🔹 CHILD CLASS IMPLEMENTING MULTIPLE ABSTRACT CLASSES
class Customer(Bank, Loan):

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


    # 🔹 Implementing abstract methods
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")


    def apply_loan(self, amount):
        print(f"Loan of {amount} applied successfully")


    def show_balance(self):
        print(f"{self.name}'s Balance:", self.balance)



# 🔹 MAIN PROGRAM

print("\n--- Abstraction Example (Bank System) ---")

cust = Customer("Vikyat", 5000)

cust.deposit(2000)
cust.withdraw(3000)
cust.apply_loan(10000)
cust.show_balance()