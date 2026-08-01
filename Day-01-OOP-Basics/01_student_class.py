class Student:
    college = "PES University"

    def __init__(self, name, usn, branch):
        self.name = name
        self.usn = usn
        self.branch = branch

    def display(self):
        print("Name :", self.name)
        print("USN :", self.usn)
        print("Branch :", self.branch)
        print("College :", Student.college)


s1 = Student("Rahul", "PES1UG22CS001", "CSE")
s2 = Student("Priya", "PES1UG22CS002", "CSE")

s1.display()
print()
s2.display()