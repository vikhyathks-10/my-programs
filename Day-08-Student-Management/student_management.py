import sqlite3


# ==============================
# DATABASE CONNECTION
# ==============================

conn = sqlite3.connect("students.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    branch TEXT NOT NULL,
    marks REAL NOT NULL,
    attendance REAL NOT NULL
)
""")

conn.commit()


# ==============================
# STUDENT MANAGEMENT CLASS
# ==============================

class StudentManagement:

    # --------------------------
    # ADD STUDENT
    # --------------------------

    def add_student(self):

        try:
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            branch = input("Enter Branch: ")
            marks = float(input("Enter Marks: "))
            attendance = float(input("Enter Attendance (%): "))

            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                return

            if attendance < 0 or attendance > 100:
                print("Attendance must be between 0 and 100.")
                return

            cursor.execute("""
                INSERT INTO students
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                student_id,
                name,
                age,
                branch,
                marks,
                attendance
            ))

            conn.commit()

            print("\nStudent Added Successfully!")

        except ValueError:
            print("Please enter valid numerical values.")

        except sqlite3.IntegrityError:
            print("Student ID already exists.")


    # --------------------------
    # VIEW ALL STUDENTS
    # --------------------------

    def view_students(self):

        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        if not students:
            print("\nNo Students Found.")
            return

        print("\n================ STUDENT RECORDS ================")

        print(
            f"{'ID':<8}"
            f"{'Name':<20}"
            f"{'Age':<8}"
            f"{'Branch':<12}"
            f"{'Marks':<10}"
            f"{'Attendance':<12}"
        )

        print("-" * 70)

        for student in students:

            print(
                f"{student[0]:<8}"
                f"{student[1]:<20}"
                f"{student[2]:<8}"
                f"{student[3]:<12}"
                f"{student[4]:<10.2f}"
                f"{student[5]:<12.2f}"
            )


    # --------------------------
    # SEARCH STUDENT
    # --------------------------

    def search_student(self):

        student_id = input("Enter Student ID: ")

        cursor.execute(
            "SELECT * FROM students WHERE student_id=?",
            (student_id,)
        )

        student = cursor.fetchone()

        if student:

            print("\nStudent Found!")

            print("ID         :", student[0])
            print("Name       :", student[1])
            print("Age        :", student[2])
            print("Branch     :", student[3])
            print("Marks      :", student[4])
            print("Attendance :", student[5])
            print("Grade      :", self.calculate_grade(student[4]))

        else:
            print("Student Not Found.")


    # --------------------------
    # UPDATE STUDENT
    # --------------------------

    def update_student(self):

        try:
            student_id = int(input("Enter Student ID: "))

            cursor.execute(
                "SELECT * FROM students WHERE student_id=?",
                (student_id,)
            )

            student = cursor.fetchone()

            if not student:
                print("Student Not Found.")
                return

            print("\n1. Update Name")
            print("2. Update Age")
            print("3. Update Branch")
            print("4. Update Marks")
            print("5. Update Attendance")

            choice = input("Enter Choice: ")

            if choice == "1":

                name = input("Enter New Name: ")

                cursor.execute(
                    "UPDATE students SET name=? WHERE student_id=?",
                    (name, student_id)
                )

            elif choice == "2":

                age = int(input("Enter New Age: "))

                cursor.execute(
                    "UPDATE students SET age=? WHERE student_id=?",
                    (age, student_id)
                )

            elif choice == "3":

                branch = input("Enter New Branch: ")

                cursor.execute(
                    "UPDATE students SET branch=? WHERE student_id=?",
                    (branch, student_id)
                )

            elif choice == "4":

                marks = float(input("Enter New Marks: "))

                if marks < 0 or marks > 100:
                    print("Marks must be between 0 and 100.")
                    return

                cursor.execute(
                    "UPDATE students SET marks=? WHERE student_id=?",
                    (marks, student_id)
                )

            elif choice == "5":

                attendance = float(
                    input("Enter New Attendance (%): ")
                )

                if attendance < 0 or attendance > 100:
                    print("Attendance must be between 0 and 100.")
                    return

                cursor.execute(
                    "UPDATE students SET attendance=? WHERE student_id=?",
                    (attendance, student_id)
                )

            else:

                print("Invalid Choice.")
                return

            conn.commit()

            print("Student Updated Successfully!")

        except ValueError:

            print("Please enter valid values.")


    # --------------------------
    # DELETE STUDENT
    # --------------------------

    def delete_student(self):

        try:
            student_id = int(input("Enter Student ID: "))

            cursor.execute(
                "SELECT name FROM students WHERE student_id=?",
                (student_id,)
            )

            student = cursor.fetchone()

            if not student:

                print("Student Not Found.")
                return

            confirm = input(
                f"Delete {student[0]}? (y/n): "
            ).lower()

            if confirm == "y":

                cursor.execute(
                    "DELETE FROM students WHERE student_id=?",
                    (student_id,)
                )

                conn.commit()

                print("Student Deleted Successfully!")

            else:

                print("Deletion Cancelled.")

        except ValueError:

            print("Invalid Student ID.")


    # --------------------------
    # CALCULATE GRADE
    # --------------------------

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


    # --------------------------
    # STUDENT PERFORMANCE
    # --------------------------

    def performance(self):

        try:
            student_id = int(input("Enter Student ID: "))

            cursor.execute(
                "SELECT * FROM students WHERE student_id=?",
                (student_id,)
            )

            student = cursor.fetchone()

            if not student:

                print("Student Not Found.")
                return

            marks = student[4]
            attendance = student[5]

            grade = self.calculate_grade(marks)

            print("\n========== PERFORMANCE ==========")

            print("Student       :", student[1])
            print("Marks         :", marks)
            print("Grade         :", grade)
            print("Attendance    :", f"{attendance}%")

            if attendance >= 75:
                print("Attendance    : Eligible")
            else:
                print("Attendance    : Shortage")

            if marks >= 50 and attendance >= 75:
                print("Result        : PASS")
            else:
                print("Result        : NEEDS IMPROVEMENT")

        except ValueError:

            print("Invalid Student ID.")


# ==============================
# MAIN PROGRAM
# ==============================

manager = StudentManagement()


while True:

    print("\n")
    print("=" * 45)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Performance")
    print("7. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        manager.add_student()

    elif choice == "2":

        manager.view_students()

    elif choice == "3":

        manager.search_student()

    elif choice == "4":

        manager.update_student()

    elif choice == "5":

        manager.delete_student()

    elif choice == "6":

        manager.performance()

    elif choice == "7":

        print("\nThank you for using Student Management System!")
        break

    else:

        print("\nInvalid Choice. Please try again.")


conn.close()