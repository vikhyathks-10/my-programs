# 🔹 ENCAPSULATION - ALL IN ONE PROGRAM


class BankAccount:

    # 🔹 Constructor
    def __init__(self, name, balance, pin):
        self.name = name              # Public
        self._account_type = "Savings"  # Protected
        self.__balance = balance      # Private
        self.__pin = pin              # Private


    # 🔹 Getter (Access Private Data)
    def get_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Incorrect PIN"


    # 🔹 Setter (Modify Private Data)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount Deposited Successfully")
        else:
            print("Invalid Amount")


    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Incorrect PIN")
        elif amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print("Withdrawal Successful")


    # 🔹 Property Decorator (Clean Getter)
    @property
    def account_info(self):
        return f"Name: {self.name}, Type: {self._account_type}"


    # 🔹 Secure Method (Data Hiding)
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("PIN changed successfully")
        else:
            print("Wrong old PIN")



# 🔹 MAIN PROGRAM

acc = BankAccount("Vikyat", 5000, 1234)

print("\n--- Public Access ---")
print(acc.name)

print("\n--- Protected Access (Not Recommended but Possible) ---")
print(acc._account_type)

print("\n--- Private Access (Not Directly Allowed) ---")
# print(acc.__balance)  ❌ ERROR


print("\n--- Getter Method ---")
print("Balance:", acc.get_balance(1234))


print("\n--- Setter Methods ---")
acc.deposit(1000)
acc.withdraw(2000, 1234)

print("Balance after transactions:", acc.get_balance(1234))


print("\n--- Property Decorator ---")
print(acc.account_info)


print("\n--- Secure Data Modification ---")
acc.change_pin(1234, 5678)
print("Balance with new PIN:", acc.get_balance(5678))