import csv


# ==================================================
# PROGRAM 91
# Read Student CSV
# ==================================================

def read_students(filename):
    students = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

        print("\n--- Student Records ---")

        for student in students:
            print(
                f"Name: {student['Name']}, "
                f"Python: {student['Python']}, "
                f"C++: {student['C++']}, "
                f"DBMS: {student['DBMS']}, "
                f"Maths: {student['Maths']}"
            )

        return students

    except FileNotFoundError:
        print("\nError: students.csv not found.")
        return []

    except KeyError:
        print("\nError: CSV file has incorrect column names.")
        return []

    except Exception as e:
        print(f"\nError reading CSV file: {e}")
        return []


# ==================================================
# HELPER FUNCTION
# Calculate Student Average
# ==================================================

def calculate_student_average(student):
    marks = [
        float(student["Python"]),
        float(student["C++"]),
        float(student["DBMS"]),
        float(student["Maths"])
    ]

    return sum(marks) / len(marks)


# ==================================================
# PROGRAM 92
# Calculate Average Marks
# ==================================================

def calculate_averages(students):

    if not students:
        print("\nNo student records available.")
        return

    print("\n--- Average Marks ---")

    for student in students:

        average = calculate_student_average(student)

        print(
            f"{student['Name']}: "
            f"{average:.2f}"
        )


# ==================================================
# PROGRAM 93
# Find Highest-Scoring Student
# ==================================================

def highest_scoring_student(students):

    if not students:
        print("\nNo student records available.")
        return None

    highest_student = students[0]
    highest_average = calculate_student_average(
        highest_student
    )

    for student in students[1:]:

        average = calculate_student_average(student)

        if average > highest_average:
            highest_average = average
            highest_student = student

    print("\n--- Highest-Scoring Student ---")

    print(
        f"Student: {highest_student['Name']}"
    )

    print(
        f"Average: {highest_average:.2f}"
    )

    return highest_student, highest_average


# ==================================================
# PROGRAM 94
# Filter Students Above a Particular Mark
# ==================================================

def filter_students(students, minimum_mark):

    if not students:
        print("\nNo student records available.")
        return

    print(
        f"\n--- Students With Average "
        f"Above {minimum_mark:.2f} ---"
    )

    found = False

    for student in students:

        average = calculate_student_average(student)

        if average >= minimum_mark:

            print(
                f"{student['Name']} -> "
                f"{average:.2f}"
            )

            found = True

    if not found:
        print(
            f"No students found with an average "
            f"of {minimum_mark:.2f} or above."
        )


# ==================================================
# PROGRAM 95
# Generate Summary CSV
# ==================================================

def generate_summary_csv(students, filename):

    if not students:
        print("\nNo student records available.")
        return

    try:

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            fieldnames = [
                "Name",
                "Average",
                "Grade"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for student in students:

                average = calculate_student_average(student)

                if average >= 90:
                    grade = "A+"

                elif average >= 80:
                    grade = "A"

                elif average >= 70:
                    grade = "B"

                elif average >= 60:
                    grade = "C"

                elif average >= 50:
                    grade = "D"

                else:
                    grade = "F"

                writer.writerow({
                    "Name": student["Name"],
                    "Average": f"{average:.2f}",
                    "Grade": grade
                })

        print(
            f"\nSummary successfully written "
            f"to '{filename}'."
        )

    except Exception as e:
        print(
            f"\nError creating summary CSV: {e}"
        )


# ==================================================
# MENU
# ==================================================

def display_menu():

    print("\n" + "=" * 55)
    print("           STUDENT CSV ANALYZER")
    print("=" * 55)

    print("1. Read Student CSV")
    print("2. Calculate Average Marks")
    print("3. Find Highest-Scoring Student")
    print("4. Filter Students Above a Mark")
    print("5. Generate Summary CSV")
    print("6. Run All Programs")
    print("7. Exit")

    print("=" * 55)


# ==================================================
# MAIN PROGRAM
# ==================================================

def main():

    filename = "students.csv"

    # Load student records once
    students = read_students(filename)

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        # ------------------------------------------
        # Program 91
        # ------------------------------------------

        if choice == "1":

            students = read_students(filename)

        # ------------------------------------------
        # Program 92
        # ------------------------------------------

        elif choice == "2":

            calculate_averages(students)

        # ------------------------------------------
        # Program 93
        # ------------------------------------------

        elif choice == "3":

            highest_scoring_student(students)

        # ------------------------------------------
        # Program 94
        # ------------------------------------------

        elif choice == "4":

            try:

                mark = float(
                    input(
                        "Enter minimum average mark: "
                    )
                )

                if mark < 0 or mark > 100:
                    print(
                        "Please enter a mark between "
                        "0 and 100."
                    )
                else:
                    filter_students(
                        students,
                        mark
                    )

            except ValueError:

                print(
                    "Please enter a valid number."
                )

        # ------------------------------------------
        # Program 95
        # ------------------------------------------

        elif choice == "5":

            generate_summary_csv(
                students,
                "summary.csv"
            )

        # ------------------------------------------
        # Run All Programs
        # ------------------------------------------

        elif choice == "6":

            print("\nRunning all programs...")

            # Program 91
            students = read_students(filename)

            if not students:
                continue

            # Program 92
            calculate_averages(students)

            # Program 93
            highest_scoring_student(students)

            # Program 94
            try:

                mark = float(
                    input(
                        "\nEnter minimum average "
                        "mark for filtering: "
                    )
                )

                if 0 <= mark <= 100:

                    filter_students(
                        students,
                        mark
                    )

                else:

                    print(
                        "Mark must be between "
                        "0 and 100."
                    )

            except ValueError:

                print(
                    "Invalid mark. "
                    "Skipping filter operation."
                )

            # Program 95
            generate_summary_csv(
                students,
                "summary.csv"
            )

        # ------------------------------------------
        # Exit
        # ------------------------------------------

        elif choice == "7":

            print(
                "\nThank you for using "
                "Student CSV Analyzer!"
            )

            break

        # ------------------------------------------
        # Invalid Choice
        # ------------------------------------------

        else:

            print(
                "\nInvalid choice. "
                "Please enter a number from 1 to 7."
            )


# ==================================================
# PROGRAM ENTRY POINT
# ==================================================

if __name__ == "__main__":
    main()