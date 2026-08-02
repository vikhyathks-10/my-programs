class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, usn):
        super().__init__(name)
        self.usn = usn

    def details(self):
        self.display()
        print("USN:", self.usn)


s = Student("Rahul", "PES1UG22CS001")
s.details()