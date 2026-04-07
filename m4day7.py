# 🔹 ALL MINI PROJECTS IN ONE PROGRAM

# ---------------- ATM ----------------
class ATM:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin

    def check_balance(self, pin):
        if pin == self.__pin:
            print("Balance:", self.__balance)
        else:
            print("Wrong PIN")

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Wrong PIN")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)


# ---------------- SHOPPING CART ----------------
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def total(self):
        total = sum(p.price for p in self.items)
        print("Total Price:", total)


# ---------------- QUIZ ----------------
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, q):
        self.questions.append(q)

    def start(self):
        score = 0
        for q in self.questions:
            ans = input(q.question + " ")
            if ans.lower() == q.answer.lower():
                score += 1
        print("Score:", score)


# ---------------- CONTACT MANAGER ----------------
class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def view_contacts(self):
        for name, phone in self.contacts.items():
            print(name, ":", phone)


# ---------------- FILE MANAGER ----------------
class FileManager:
    def write_file(self, filename, data):
        with open(filename, "w") as f:
            f.write(data)

    def read_file(self, filename):
        with open(filename, "r") as f:
            print(f.read())


# ---------------- MAIN MENU ----------------

atm = ATM(5000, 1234)
cart = Cart()
quiz = Quiz()
cm = ContactManager()
fm = FileManager()

# Preload quiz
quiz.add_question(Question("Python is interpreted? (yes/no)", "yes"))
quiz.add_question(Question("2+2=?", "4"))

while True:
    print("\n====== MAIN MENU ======")
    print("1. ATM")
    print("2. Shopping Cart")
    print("3. Quiz")
    print("4. Contact Manager")
    print("5. File Manager")
    print("0. Exit")

    choice = input("Enter choice: ")

    # ATM
    if choice == "1":
        pin = int(input("Enter PIN: "))
        print("1. Check Balance  2. Deposit  3. Withdraw")
        opt = input("Enter option: ")
        if opt == "1":
            atm.check_balance(pin)
        elif opt == "2":
            amt = int(input("Amount: "))
            atm.deposit(amt)
        elif opt == "3":
            amt = int(input("Amount: "))
            atm.withdraw(amt, pin)

    # Shopping Cart
    elif choice == "2":
        name = input("Enter product name: ")
        price = int(input("Enter price: "))
        cart.add_item(Product(name, price))
        cart.total()

    # Quiz
    elif choice == "3":
        quiz.start()

    # Contact Manager
    elif choice == "4":
        name = input("Name: ")
        phone = input("Phone: ")
        cm.add_contact(name, phone)
        cm.view_contacts()

    # File Manager
    elif choice == "5":
        filename = input("File name: ")
        data = input("Enter data: ")
        fm.write_file(filename, data)
        fm.read_file(filename)

    elif choice == "0":
        print("Exiting...")
        break

    else:
        print("Invalid choice")