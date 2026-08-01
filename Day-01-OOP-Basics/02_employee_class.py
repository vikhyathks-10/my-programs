class Employee:

    company = "Google"

    def __init__(self, name, empid, salary):
        self.name = name
        self.empid = empid
        self.salary = salary

    def display(self):
        print("Employee Name :", self.name)
        print("Employee ID :", self.empid)
        print("Salary :", self.salary)
        print("Company :", Employee.company)


e1 = Employee("John", 101, 80000)
e2 = Employee("Alice", 102, 95000)

e1.display()
print()
e2.display()