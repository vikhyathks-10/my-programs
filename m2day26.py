# =====================================
# 1️⃣ Student Marks System
# =====================================
students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Marks:", students)


# =====================================
# 2️⃣ Find Topper Student
# =====================================
topper = None
max_marks = -1

for name in students:
    if students[name] > max_marks:
        max_marks = students[name]
        topper = name

print("Topper:", topper, "with marks:", max_marks)


# =====================================
# 3️⃣ Average Marks Calculation
# =====================================
total = 0

for marks in students.values():
    total += marks

average = total / len(students)
print("Average Marks:", average)


# =====================================
# 4️⃣ Nested Dictionary Creation
# =====================================
nested_students = {}

n2 = int(input("\nEnter number of students for nested dictionary: "))

for i in range(n2):
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    nested_students[name] = {
        "Age": age,
        "Marks": marks
    }

print("Nested Dictionary:", nested_students)


# =====================================
# 5️⃣ Employee Management System
# =====================================
employees = {}

m = int(input("\nEnter number of employees: "))

for i in range(m):
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    salary = int(input("Enter salary: "))

    employees[emp_id] = {
        "Name": name,
        "Salary": salary
    }

print("\nEmployee Records:", employees)

# Search employee
search_id = input("Enter employee ID to search: ")

if search_id in employees:
    print("Employee Details:", employees[search_id])
else:
    print("Employee not found")