# 🔹 DAY 27 - LIBRARY MANAGEMENT SYSTEM

from datetime import datetime


class Library:

    def __init__(self):

        self.books = {
            "Python": 5,
            "Java": 3,
            "C++": 2
        }

        self.issued_books = {}

    # 🔹 Add Books
    def add_book(self):

        book = input("Enter Book Name: ")

        quantity = int(input("Enter Quantity: "))

        if book in self.books:
            self.books[book] += quantity
        else:
            self.books[book] = quantity

        print("Books Added Successfully")

    # 🔹 Issue Books
    def issue_book(self):

        book = input("Enter Book Name to Issue: ")

        if book in self.books and self.books[book] > 0:

            user = input("Enter Student Name: ")

            self.books[book] -= 1

            issue_date = datetime.now()

            self.issued_books[user] = {
                "book": book,
                "date": issue_date
            }

            print(f"{book} Issued to {user}")

        else:
            print("Book Not Available")

    # 🔹 Return Books
    def return_book(self):

        user = input("Enter Student Name: ")

        if user in self.issued_books:

            book = self.issued_books[user]["book"]

            issue_date = self.issued_books[user]["date"]

            self.books[book] += 1

            return_date = datetime.now()

            days = (return_date - issue_date).days

            fine = self.calculate_fine(days)

            print(f"{book} Returned Successfully")

            print("Fine Amount: ₹", fine)

            del self.issued_books[user]

        else:
            print("No Book Record Found")

    # 🔹 Search Books
    def search_book(self):

        book = input("Enter Book Name: ")

        if book in self.books:

            print(f"{book} Available Quantity:",
                  self.books[book])

        else:
            print("Book Not Found")

    # 🔹 Fine Calculation
    def calculate_fine(self, days):

        if days > 7:
            return (days - 7) * 10

        return 0

    # 🔹 Display Books
    def display_books(self):

        print("\n--- Available Books ---")

        for book, qty in self.books.items():
            print(book, "->", qty)


# 🔹 MAIN PROGRAM

library = Library()

while True:

    print("\n====== LIBRARY MENU ======")

    print("1. Add Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        library.add_book()

    elif choice == "2":

        library.issue_book()

    elif choice == "3":

        library.return_book()

    elif choice == "4":

        library.search_book()

    elif choice == "5":

        library.display_books()

    elif choice == "6":

        print("Exiting Library System")
        break

    else:
        print("Invalid Choice")