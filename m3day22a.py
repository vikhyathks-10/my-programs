# -------- 1. Student Class --------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Vikyat", 85)
s1.display()


# -------- 2. Rectangle Class --------
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


r = Rectangle(5, 3)
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())


# -------- 3. Circle Class --------
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


c = Circle(4)
print("Circle Area:", c.area())
print("Circle Circumference:", c.circumference())


# -------- 4. Employee Class --------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


e = Employee("Rahul", 50000)
e.display()


# -------- 5. Book Class --------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)


b = Book("Python Basics", "Guido")
b.display()