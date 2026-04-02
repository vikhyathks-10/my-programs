# 🔹 MULTIPLE INHERITANCE + MRO + super() + REAL LIFE EXAMPLE


# Parent Class 1
class Engine:
    def start(self):
        print("Engine starts")

    def show(self):
        print("This is Engine class")


# Parent Class 2
class MusicSystem:
    def play_music(self):
        print("Music is playing")

    def show(self):
        print("This is MusicSystem class")


# 🔹 CHILD CLASS (Multiple Inheritance)
class Car(Engine, MusicSystem):
    def __init__(self, name):
        self.name = name

    def show(self):
        # Method overriding + super()
        print("Car Name:", self.name)
        super().show()   # Calls based on MRO


# 🔹 REAL-LIFE BASE CLASS
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


# Derived Class 1
class Bike(Vehicle):
    def display(self):
        print("Bike Brand:", self.brand)


# Derived Class 2
class SportsCar(Vehicle):
    def display(self):
        print("Sports Car Brand:", self.brand)


# 🔹 MAIN PROGRAM

print("\n--- Multiple Inheritance ---")
c = Car("BMW")
c.start()          # from Engine
c.play_music()     # from MusicSystem
c.show()           # overridden

print("\n--- MRO (Method Resolution Order) ---")
print(Car.__mro__)   # Shows order of method lookup

print("\n--- Base vs Derived Method Call ---")
v = Vehicle("Generic Brand")
v.display()

b = Bike("Yamaha")
b.display()   # overridden

s = SportsCar("Ferrari")
s.display()   # overridden