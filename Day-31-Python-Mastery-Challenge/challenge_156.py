# ============================================================
# DAY 31 - PROGRAM 156
# STUDENT PERFORMANCE ANALYZER
# ============================================================

def calculate_grade(average):
    """Return grade based on average marks."""

    if average >= 90:
        return "A"

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    elif average >= 60:
        return "D"

    elif average >= 40:
        return "E"

    else:
        return "F"


def calculate_total(marks):
    """Calculate total marks."""

    return sum(marks)


def calculate_average(marks):
    """Calculate average marks."""

    if not marks:
        return 0

    return sum(marks) / len(marks)


def add_student(students):
    """Add a student to the student dictionary."""

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    if name in students:
        print("Student already exists.")
        return

    marks = []

    print("\nEnter marks for 5 subjects.")

    for subject_number in range(1, 6):

        while True:

            try:

                mark = float(
                    input(
                        f"Subject {subject_number} marks: "
                    )
                )

                if mark < 0 or mark > 100:

                    print(
                        "Marks must be between 0 and 100."
                    )

                    continue

                marks.append(mark)

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

    students[name] = marks

    print(
        f"\n{name} added successfully."
    )


def display_students(students):
    """Display all student details."""

    if not students:

        print("\nNo student records available.")

        return

    print("\n" + "=" * 75)

    print(
        f"{'Name':<20}"
        f"{'Total':<10}"
        f"{'Average':<12}"
        f"{'Grade':<10}"
        f"{'Status':<10}"
    )

    print("=" * 75)

    for name, marks in students.items():

        total = calculate_total(marks)

        average = calculate_average(marks)

        grade = calculate_grade(average)

        status = (
            "PASS"
            if average >= 40
            else "FAIL"
        )

        print(
            f"{name:<20}"
            f"{total:<10.2f}"
            f"{average:<12.2f}"
            f"{grade:<10}"
            f"{status:<10}"
        )

    print("=" * 75)


def find_highest_student(students):
    """Find student with highest average."""

    if not students:

        return None

    return max(
        students,
        key=lambda name:
        calculate_average(students[name])
    )


def find_lowest_student(students):
    """Find student with lowest average."""

    if not students:

        return None

    return min(
        students,
        key=lambda name:
        calculate_average(students[name])
    )


def class_average(students):
    """Calculate overall class average."""

    if not students:

        return 0

    all_marks = []

    for marks in students.values():

        all_marks.extend(marks)

    return calculate_average(all_marks)


def display_analysis(students):
    """Display overall class analysis."""

    if not students:

        print("\nNo data available.")

        return

    highest = find_highest_student(students)

    lowest = find_lowest_student(students)

    average = class_average(students)

    print("\n" + "=" * 50)
    print("          CLASS PERFORMANCE")
    print("=" * 50)

    print(
        f"Class Average : {average:.2f}"
    )

    print(
        f"Highest       : {highest} "
        f"({calculate_average(students[highest]):.2f})"
    )

    print(
        f"Lowest        : {lowest} "
        f"({calculate_average(students[lowest]):.2f})"
    )

    print("=" * 50)


def main():

    students = {}

    while True:

        print("\n" + "=" * 55)
        print("       STUDENT PERFORMANCE ANALYZER")
        print("=" * 55)

        print("1. Add Student")
        print("2. Display Students")
        print("3. Display Class Analysis")
        print("4. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            add_student(students)

        elif choice == "2":

            display_students(students)

        elif choice == "3":

            display_analysis(students)

        elif choice == "4":

            print("\nProgram completed.")

            break

        else:

            print("\nInvalid choice.")


if __name__ == "__main__":

    main()