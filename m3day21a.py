# -------- 1. Simple Class --------
class Hello:
    def display(self):
        print("Hello, this is a simple class")


obj1 = Hello()
obj1.display()


# -------- 2. Class with Attributes --------
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Vikyat", 19)
s1.show()


# -------- 3. Class with Methods --------
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()
print("Addition:", calc.add(5, 3))
print("Multiplication:", calc.multiply(5, 3))


# -------- 4. Object Counter --------
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1


c1 = Counter()
c2 = Counter()
c3 = Counter()

print("Total objects created:", Counter.count)


# -------- 5. Class Variable vs Instance Variable --------
class Example:
    class_var = "I am class variable"

    def __init__(self, name):
        self.name = name   # instance variable


e1 = Example("Vikyat")
e2 = Example("Python")

print("Class Variable:", Example.class_var)
print("Instance Variable e1:", e1.name)
print("Instance Variable e2:", e2.name)