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


# 🔹 SECOND ABSTRACT CLASS (Multiple Abstract Classes)
class Loan(ABC):

    @abstractmethod
    def apply_loan(self, amount):
        pass


# 🔹 CHILD CLASS IMPLEMENTING BOTH ABSTRACT CLASSES
class Customer(Bank, Loan):

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


    # 🔹 Implement abstract methods
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def apply_loan(self, amount):
        print("Loan Applied:", amount)


    # 🔹 Extra method
    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)



# 🔹 MAIN PROGRAM

print("\n--- Bank System (Abstraction) ---")

c = Customer("Vikyat", 5000)

c.deposit(1000)
c.withdraw(2000)
c.apply_loan(10000)
c.display()


# 🔹 MANDATORY POINT (Cannot create object of abstract class)
# b = Bank()   ❌ ERROR