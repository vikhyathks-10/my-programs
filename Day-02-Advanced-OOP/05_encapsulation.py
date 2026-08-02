class Circle:
    def area(self):
        print("Area of Circle = πr²")


class Square:
    def area(self):
        print("Area of Square = side²")


class Rectangle:
    def area(self):
        print("Area of Rectangle = length × breadth")


shapes = [Circle(), Square(), Rectangle()]

for shape in shapes:
    shape.area()