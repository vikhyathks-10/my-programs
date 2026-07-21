# ==========================================================
# Month 7 - Day 21
# Advanced Object-Oriented Programming (OOP)
#
# Topics Covered:
# 1. Abstraction (ABC)
# 2. Abstract Methods
# 3. Static Methods
# 4. Class Methods
# 5. Operator Overloading
# 6. Magic (Dunder) Methods
# ==========================================================

from abc import ABC, abstractmethod

print("=" * 60)
print("1. ABSTRACTION (ABC)")
print("=" * 60)

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Starts with Key.")

car = Car()
car.start()


print("\n" + "=" * 60)
print("2. ABSTRACT METHODS")
print("=" * 60)

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)

print("Area of Circle:", circle.area())


print("\n" + "=" * 60)
print("3. STATIC METHODS")
print("=" * 60)

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

print("Addition:", Calculator.add(10, 20))


print("\n" + "=" * 60)
print("4. CLASS METHODS")
print("=" * 60)

class Student:

    college = "PES University"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

student1 = Student("Vikhyath")

print("Before Change:", Student.college)

Student.change_college("IIT Bangalore")

print("After Change :", Student.college)


print("\n" + "=" * 60)
print("5. OPERATOR OVERLOADING")
print("=" * 60)

class Book:

    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

book1 = Book(250)
book2 = Book(300)

print("Total Pages:", book1 + book2)


print("\n" + "=" * 60)
print("6. MAGIC (DUNDER) METHODS")
print("=" * 60)

class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person(Name = {self.name})"

    def __len__(self):
        return len(self.name)

person = Person("Vikhyath")

print(person)
print("Length of Name:", len(person))


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ Abstraction

Hides implementation details
and shows only essential features.

Module

abc

Import

from abc import ABC, abstractmethod

--------------------------------------------------

✔ Abstract Class

Cannot be instantiated directly.

Contains one or more
abstract methods.

--------------------------------------------------

✔ Abstract Method

Defined using

@abstractmethod

Must be implemented
by child classes.

--------------------------------------------------

✔ Static Method

Decorator

@staticmethod

• Does NOT access instance variables.
• Does NOT access class variables.
• Utility/helper methods.

Call using

Class.method()

--------------------------------------------------

✔ Class Method

Decorator

@classmethod

First parameter

cls

Used to modify
class variables.

--------------------------------------------------

✔ Operator Overloading

Customize operators.

Examples

__add__()

__sub__()

__mul__()

__truediv__()

--------------------------------------------------

✔ Magic (Dunder) Methods

Special methods automatically
called by Python.

Common Ones

__init__()

__str__()

__repr__()

__len__()

__add__()

__eq__()

--------------------------------------------------

Interview Tip

Difference

Instance Method
→ Uses self

Class Method
→ Uses cls

Static Method
→ Uses neither self nor cls

--------------------------------------------------

Most Asked OOP Interview Topics

✔ Abstraction
✔ Inheritance
✔ Polymorphism
✔ Encapsulation
✔ Magic Methods
✔ Operator Overloading
✔ Static vs Class Methods
""")