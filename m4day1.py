# 🔹 BASE CLASS
class Person:
    def __init__(self, name):
        self.name = name
        print("Person Constructor Called")

    def show(self):
        print("Name:", self.name)


# 🔹 SINGLE INHERITANCE
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)   # Constructor chaining
        self.roll = roll
        print("Student Constructor Called")

    def show(self):
        print("Student Name:", self.name)
        print("Roll No:", self.roll)


# 🔹 MULTI-LEVEL INHERITANCE
class CollegeStudent(Student):
    def __init__(self, name, roll, college):
        super().__init__(name, roll)
        self.college = college
        print("CollegeStudent Constructor Called")

    def show(self):
        super().show()
        print("College:", self.college)


# 🔹 HIERARCHICAL INHERITANCE
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print("Teacher Constructor Called")

    def show(self):
        print("Teacher Name:", self.name)
        print("Subject:", self.subject)


# 🔹 MAIN PROGRAM

print("\n--- Single Inheritance ---")
s = Student("Vikyat", 101)
s.show()

print("\n--- Multi-Level Inheritance ---")
cs = CollegeStudent("Rahul", 102, "PS College")
cs.show()

print("\n--- Hierarchical Inheritance ---")
t = Teacher("Anil Sir", "Math")
t.show()