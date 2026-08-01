class LibraryBook:

    library = "City Central Library"

    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def issue(self):
        if self.available:
            self.available = False
            print(f"{self.title} issued successfully.")
        else:
            print("Book already issued.")

    def return_book(self):
        self.available = True
        print(f"{self.title} returned successfully.")

    def display(self):
        print("\nBook ID :", self.book_id)
        print("Title :", self.title)
        print("Author :", self.author)
        print("Available :", self.available)


book1 = LibraryBook(101, "Python Programming", "Guido")
book2 = LibraryBook(102, "Machine Learning", "Andrew Ng")

book1.display()

book1.issue()

book1.display()

book1.return_book()

book1.display()