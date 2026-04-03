# 🔹 POLYMORPHISM - ALL IN ONE PROGRAM


# 🔹 FUNCTION POLYMORPHISM
def add(a, b, c=0):   # simulate overloading using default argument
    return a + b + c


# 🔹 METHOD OVERLOADING (SIMULATION)
class Calculator:
    def multiply(self, a, b, c=None):
        if c is None:
            return a * b
        else:
            return a * b * c


# 🔹 METHOD OVERRIDING
class Animal:
    def speak(self):
        print("Animal makes sound")


class Dog(Animal):
    def speak(self):   # overriding
        print("Dog barks")


# 🔹 OPERATOR OVERLOADING
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __eq__(self, other):
        return self.value == other.value

    def display(self):
        print("Value:", self.value)


# 🔹 DUCK TYPING
class Bird:
    def fly(self):
        print("Bird can fly")


class Airplane:
    def fly(self):
        print("Airplane can fly")


def make_it_fly(obj):
    obj.fly()   # no type check (duck typing)


# 🔹 MAIN PROGRAM

print("\n--- Function Polymorphism ---")
print(add(2, 3))
print(add(2, 3, 4))


print("\n--- Method Overloading (Simulated) ---")
calc = Calculator()
print(calc.multiply(2, 3))
print(calc.multiply(2, 3, 4))


print("\n--- Method Overriding ---")
a = Animal()
a.speak()

d = Dog()
d.speak()


print("\n--- Operator Overloading ---")
n1 = Number(10)
n2 = Number(20)

n3 = n1 + n2   # uses __add__
n3.display()

print("Are equal?", n1 == n2)   # uses __eq__


print("\n--- Duck Typing ---")
b = Bird()
p = Airplane()

make_it_fly(b)
make_it_fly(p)