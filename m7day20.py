# ==========================================================
# Month 7 - Day 20
# Object-Oriented Programming (OOP)
#
# Topics Covered:
# 1. Class & Object
# 2. Constructor (__init__)
# 3. Inheritance
# 4. Method Overriding
# 5. Polymorphism
# 6. Encapsulation
# ==========================================================

print("=" * 60)
print("1. CLASS & OBJECT")
print("=" * 60)

class Student:

    def display(self):
        print("Welcome to Python OOP!")

student = Student()
student.display()


print("\n" + "=" * 60)
print("2. CONSTRUCTOR (__init__)")
print("=" * 60)

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        print("Name   :", self.name)
        print("Salary :", self.salary)

emp = Employee("Vikhyath", 50000)
emp.details()


print("\n" + "=" * 60)
print("3. INHERITANCE")
print("=" * 60)

class Animal:

    def sound(self):
        print("Animals make sounds.")

class Dog(Animal):

    def bark(self):
        print("Dog barks.")

dog = Dog()

dog.sound()
dog.bark()


print("\n" + "=" * 60)
print("4. METHOD OVERRIDING")
print("=" * 60)

class Bird:

    def fly(self):
        print("Bird can fly.")

class Penguin(Bird):

    def fly(self):
        print("Penguin cannot fly.")

bird = Bird()
penguin = Penguin()

bird.fly()
penguin.fly()


print("\n" + "=" * 60)
print("5. POLYMORPHISM")
print("=" * 60)

class Circle:

    def area(self):
        return 3.14 * 5 * 5

class Rectangle:

    def area(self):
        return 10 * 4

shapes = [Circle(), Rectangle()]

for shape in shapes:
    print("Area:", shape.area())


print("\n" + "=" * 60)
print("6. ENCAPSULATION")
print("=" * 60)

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance!")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)

account.deposit(500)
account.withdraw(300)

print("Current Balance:", account.get_balance())


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ Object-Oriented Programming (OOP)

OOP organizes programs into
objects that contain both
data and methods.

--------------------------------------------------

✔ Class

Blueprint for creating objects.

Example

class Student:
    pass

--------------------------------------------------

✔ Object

Instance of a class.

Example

student = Student()

--------------------------------------------------

✔ Constructor

__init__()

Automatically called when
an object is created.

--------------------------------------------------

✔ Inheritance

Allows one class to inherit
properties and methods
from another.

Types

• Single
• Multiple
• Multilevel
• Hierarchical
• Hybrid

--------------------------------------------------

✔ Method Overriding

Child class provides its own
implementation of a parent method.

--------------------------------------------------

✔ Polymorphism

Same method name,
different implementations.

Example

shape.area()

Circle
Rectangle

--------------------------------------------------

✔ Encapsulation

Restricts direct access
to data.

Private Variable

__balance

Access using methods.

--------------------------------------------------

Interview Tip

The Four Pillars of OOP

✔ Encapsulation
✔ Abstraction
✔ Inheritance
✔ Polymorphism

These are among the most
frequently asked Python
interview topics.
""")