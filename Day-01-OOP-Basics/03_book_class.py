class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def details(self):
        print("Title :", self.title)
        print("Author :", self.author)
        print("Price :", self.price)


b1 = Book("Python Programming", "Guido", 699)
b2 = Book("Data Structures", "Mark", 850)

b1.details()
print()
b2.details()