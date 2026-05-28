# 🔹 DAY 28 - STUDENT RESULT SYSTEM


class StudentSystem:

    def __init__(self):

        self.students = []

    # 🔹 Add Student Data
    def add_student(self):

        print("\n--- Add Student ---")

        name = input("Enter Student Name: ")

        marks = float(input("Enter Marks (out of 100): "))

        grade = self.calculate_grade(marks)

        student = {
            "name": name,
            "marks": marks,
            "grade": grade
        }

        self.students.append(student)

        print("Student Added Successfully")

    # 🔹 Calculate Grade
    def calculate_grade(self, marks):

        if marks >= 90:
            return "A+"

        elif marks >= 80:
            return "A"

        elif marks >= 70:
            return "B"

        elif marks >= 60:
            return "C"

        elif marks >= 50:
            return "D"

        else:
            return "F"

    # 🔹 Rank Students
    def rank_students(self):

        print("\n--- Student Rankings ---")

        ranked = sorted(
            self.students,
            key=lambda x: x["marks"],
            reverse=True
        )

        for i, student in enumerate(ranked, start=1):

            print(
                f"{i}. {student['name']} "
                f"- {student['marks']} "
                f"({student['grade']})"
            )

    # 🔹 Result Statistics
    def result_statistics(self):

        print("\n--- Result Statistics ---")

        if not self.students:
            print("No Student Data")
            return

        marks_list = [s["marks"] for s in self.students]

        highest = max(marks_list)
        lowest = min(marks_list)
        average = sum(marks_list) / len(marks_list)

        print("Highest Marks:", highest)
        print("Lowest Marks:", lowest)
        print("Average Marks:", round(average, 2))

    # 🔹 Generate Report Card
    def generate_report_card(self):

        print("\n--- Report Cards ---")

        if not self.students:
            print("No Student Data")
            return

        for student in self.students:

            print("\n====================")

            print("Name :", student["name"])

            print("Marks:", student["marks"])

            print("Grade:", student["grade"])

            print("====================")


# 🔹 MAIN PROGRAM

system = StudentSystem()

while True:

    print("\n====== STUDENT RESULT MENU ======")

    print("1. Add Student Data")
    print("2. Rank Students")
    print("3. Result Statistics")
    print("4. Generate Report Card")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        system.add_student()

    elif choice == "2":

        system.rank_students()

    elif choice == "3":

        system.result_statistics()

    elif choice == "4":

        system.generate_report_card()

    elif choice == "5":

        print("Exiting Student Result System")
        break

    else:
        print("Invalid Choice")