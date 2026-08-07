import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    category TEXT,
    status TEXT
)
""")

conn.commit()


class Library:

    def add_book(self):

        book_id = int(input("Book ID: "))
        title = input("Title: ")
        author = input("Author: ")
        category = input("Category: ")

        cursor.execute(
            "INSERT INTO books VALUES(?,?,?,?,?)",
            (book_id, title, author, category, "Available")
        )

        conn.commit()

        print("Book Added Successfully!")

    def view_books(self):

        cursor.execute("SELECT * FROM books")

        books = cursor.fetchall()

        print("\n========== BOOKS ==========\n")

        for book in books:
            print(book)

    def search_book(self):

        keyword = input("Enter Book Title: ")

        cursor.execute(
            "SELECT * FROM books WHERE title LIKE ?",
            ('%' + keyword + '%',)
        )

        books = cursor.fetchall()

        if books:
            for book in books:
                print(book)
        else:
            print("Book Not Found.")

    def issue_book(self):

        book_id = int(input("Enter Book ID: "))

        cursor.execute(
            "SELECT status FROM books WHERE book_id=?",
            (book_id,)
        )

        result = cursor.fetchone()

        if result:

            if result[0] == "Available":

                cursor.execute(
                    "UPDATE books SET status='Issued' WHERE book_id=?",
                    (book_id,)
                )

                conn.commit()

                print("Book Issued Successfully!")

            else:
                print("Book Already Issued.")

        else:
            print("Book Not Found.")

    def return_book(self):

        book_id = int(input("Enter Book ID: "))

        cursor.execute(
            "SELECT status FROM books WHERE book_id=?",
            (book_id,)
        )

        result = cursor.fetchone()

        if result:

            if result[0] == "Issued":

                cursor.execute(
                    "UPDATE books SET status='Available' WHERE book_id=?",
                    (book_id,)
                )

                conn.commit()

                print("Book Returned Successfully!")

            else:
                print("Book is Already Available.")

        else:
            print("Book Not Found.")

    def delete_book(self):

        book_id = int(input("Enter Book ID: "))

        cursor.execute(
            "DELETE FROM books WHERE book_id=?",
            (book_id,)
        )

        conn.commit()

        print("Book Deleted Successfully!")

    def available_books(self):

        cursor.execute(
            "SELECT COUNT(*) FROM books WHERE status='Available'"
        )

        count = cursor.fetchone()[0]

        print(f"\nAvailable Books : {count}")


library = Library()

while True:

    print("\n========== LIBRARY MANAGEMENT ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Count Available Books")
    print("8. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.delete_book()

    elif choice == "7":
        library.available_books()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")

conn.close()