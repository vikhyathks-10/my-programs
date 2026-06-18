# 🔹 DAY 18 - STUDENT MANAGEMENT SYSTEM

import csv
import os


class StudentManagementSystem:

    FILE_NAME = "students.csv"

    # =====================================
    # 🔹 Load Students
    # =====================================

    def load_students(self):

        students = []

        if os.path.exists(self.FILE_NAME):

            with open(self.FILE_NAME, "r", newline="") as file:

                reader = csv.reader(file)

                students = list(reader)

        return students

    # =====================================
    # 🔹 Save Students
    # =====================================

    def save_students(self, students):

        with open(self.FILE_NAME,
                  "w",
                  newline="") as file:

            writer = csv.writer(file)

            writer.writerows(students)

    # =====================================
    # 🔹 Add Student
    # =====================================

    def add_student(self):

        name = input("Enter Student Name: ")

        marks = float(
            input("Enter Marks: ")
        )

        students = self.load_students()

        students.append(
            [name, str(marks)]
        )

        self.save_students(students)

        print("✅ Student Added")

    # =====================================
    # 🔹 Update Marks
    # =====================================

    def update_marks(self):

        students = self.load_students()

        if not students:

            print("No Students Found")
            return

        name = input(
            "Enter Student Name: "
        )

        found = False

        for student in students:

            if student[0].lower() == name.lower():

                new_marks = float(
                    input(
                        "Enter New Marks: "
                    )
                )

                student[1] = str(new_marks)

                found = True

                break

        if found:

            self.save_students(students)

            print("✅ Marks Updated")

        else:

            print("❌ Student Not Found")

    # =====================================
    # 🔹 Delete Student
    # =====================================

    def delete_student(self):

        students = self.load_students()

        if not students:

            print("No Students Found")
            return

        name = input(
            "Enter Student Name: "
        )

        new_students = []

        found = False

        for student in students:

            if student[0].lower() != name.lower():

                new_students.append(student)

            else:

                found = True

        if found:

            self.save_students(new_students)

            print("✅ Student Deleted")

        else:

            print("❌ Student Not Found")

    # =====================================
    # 🔹 Grade Calculator
    # =====================================

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

    # =====================================
    # 🔹 Generate Report Card
    # =====================================

    def generate_report_card(self):

        students = self.load_students()

        if not students:

            print("No Students Found")
            return

        print("\n===== REPORT CARD =====")

        for student in students:

            name = student[0]

            marks = float(student[1])

            grade = self.calculate_grade(
                marks
            )

            print(
                f"{name} | Marks: {marks} | Grade: {grade}"
            )

    # =====================================
    # 🔹 Rank Students
    # =====================================

    def rank_students(self):

        students = self.load_students()

        if not students:

            print("No Students Found")
            return

        ranked = sorted(
            students,
            key=lambda x: float(x[1]),
            reverse=True
        )

        print("\n===== STUDENT RANKINGS =====")

        for rank, student in enumerate(
            ranked,
            start=1
        ):

            print(
                f"{rank}. {student[0]} "
                f"({student[1]} Marks)"
            )


# =====================================
# 🔹 MAIN PROGRAM
# =====================================

sms = StudentManagementSystem()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Generate Report Card")
    print("5. Rank Students")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        sms.add_student()

    elif choice == "2":

        sms.update_marks()

    elif choice == "3":

        sms.delete_student()

    elif choice == "4":

        sms.generate_report_card()

    elif choice == "5":

        sms.rank_students()

    elif choice == "6":

        print("Goodbye 👋")

        break

    else:

        print("❌ Invalid Choice")