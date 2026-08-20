# ============================================================
# MONTH 8 - DAY 20
# DATA ANALYSIS WITH PYTHON
#
# Programs 101-105
#
# Concepts:
# Lists, Dictionaries, Statistics, Sorting
#
# How to run:
# python data_analysis.py
# ============================================================

from statistics import mean, median, mode, StatisticsError


# ============================================================
# SAMPLE STUDENT DATA
# ============================================================

students = {
    "Rahul": 85,
    "Priya": 92,
    "Arjun": 76,
    "Sneha": 88,
    "Vikhyath": 95,
    "Kiran": 72,
    "Ananya": 90,
    "Rohan": 81,
    "Meera": 95,
    "Aditya": 68
}


# ============================================================
# HELPER FUNCTION
# Get marks as a list
# ============================================================

def get_marks():
    return list(students.values())


# ============================================================
# PROGRAM 101
# STUDENT MARKS STATISTICS
# ============================================================

def student_marks_statistics():

    marks = get_marks()

    print("\n" + "-" * 50)
    print("          STUDENT MARKS STATISTICS")
    print("-" * 50)

    print(f"Number of students : {len(marks)}")
    print(f"Total marks        : {sum(marks)}")
    print(f"Average marks      : {mean(marks):.2f}")
    print(f"Highest mark       : {max(marks)}")
    print(f"Lowest mark        : {min(marks)}")

    sorted_marks = sorted(marks, reverse=True)

    print("\nMarks in descending order:")

    print(sorted_marks)


# ============================================================
# PROGRAM 102
# MEAN, MEDIAN AND MODE
# ============================================================

def mean_median_mode():

    marks = get_marks()

    print("\n" + "-" * 50)
    print("          MEAN, MEDIAN AND MODE")
    print("-" * 50)

    average = mean(marks)
    middle_value = median(marks)

    try:
        most_common = mode(marks)

        print(f"Mean   : {average:.2f}")
        print(f"Median : {middle_value:.2f}")
        print(f"Mode   : {most_common}")

    except StatisticsError:

        print(f"Mean   : {average:.2f}")
        print(f"Median : {middle_value:.2f}")
        print("Mode   : No unique mode")


# ============================================================
# PROGRAM 103
# HIGHEST / LOWEST VALUE ANALYSIS
# ============================================================

def highest_lowest_analysis():

    marks = get_marks()

    highest_mark = max(marks)
    lowest_mark = min(marks)

    highest_students = [
        name
        for name, mark in students.items()
        if mark == highest_mark
    ]

    lowest_students = [
        name
        for name, mark in students.items()
        if mark == lowest_mark
    ]

    print("\n" + "-" * 50)
    print("          HIGHEST / LOWEST ANALYSIS")
    print("-" * 50)

    print(f"Highest mark : {highest_mark}")

    print(
        "Student(s) with highest mark:"
    )

    for name in highest_students:
        print(f"  {name}")

    print(f"\nLowest mark : {lowest_mark}")

    print(
        "Student(s) with lowest mark:"
    )

    for name in lowest_students:
        print(f"  {name}")


# ============================================================
# PROGRAM 104
# GRADE DISTRIBUTION
# ============================================================

def get_grade(mark):

    if mark >= 90:
        return "A+"

    elif mark >= 80:
        return "A"

    elif mark >= 70:
        return "B"

    elif mark >= 60:
        return "C"

    elif mark >= 50:
        return "D"

    else:
        return "F"


def grade_distribution():

    grade_counts = {
        "A+": 0,
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    print("\n" + "-" * 50)
    print("             GRADE DISTRIBUTION")
    print("-" * 50)

    for name, mark in students.items():

        grade = get_grade(mark)

        grade_counts[grade] += 1

        print(
            f"{name:<12} "
            f"{mark:>3} "
            f"-> Grade {grade}"
        )

    print("\nGrade Summary:")

    for grade, count in grade_counts.items():

        print(
            f"Grade {grade}: "
            f"{count} student(s)"
        )


# ============================================================
# PROGRAM 105
# CLASS PERFORMANCE ANALYZER
# ============================================================

def class_performance_analyzer():

    marks = get_marks()

    average = mean(marks)

    passed_students = [
        name
        for name, mark in students.items()
        if mark >= 50
    ]

    failed_students = [
        name
        for name, mark in students.items()
        if mark < 50
    ]

    above_average = [
        name
        for name, mark in students.items()
        if mark > average
    ]

    below_average = [
        name
        for name, mark in students.items()
        if mark < average
    ]

    pass_percentage = (
        len(passed_students) /
        len(students)
    ) * 100

    print("\n" + "-" * 50)
    print("          CLASS PERFORMANCE ANALYZER")
    print("-" * 50)

    print(f"Total students   : {len(students)}")
    print(f"Class average     : {average:.2f}")
    print(
        f"Highest mark      : {max(marks)}"
    )
    print(
        f"Lowest mark       : {min(marks)}"
    )

    print(
        f"\nPassed students   : "
        f"{len(passed_students)}"
    )

    print(
        f"Failed students   : "
        f"{len(failed_students)}"
    )

    print(
        f"Pass percentage   : "
        f"{pass_percentage:.2f}%"
    )

    print("\nStudents above class average:")

    if above_average:

        for name in above_average:
            print(
                f"  {name} -> "
                f"{students[name]}"
            )

    else:

        print("  None")

    print("\nStudents below class average:")

    if below_average:

        for name in below_average:
            print(
                f"  {name} -> "
                f"{students[name]}"
            )

    else:

        print("  None")


# ============================================================
# DISPLAY ALL STUDENTS
# ============================================================

def display_students():

    print("\n" + "-" * 50)
    print("              STUDENT DATA")
    print("-" * 50)

    for name, mark in students.items():

        print(
            f"{name:<12} : {mark}"
        )


# ============================================================
# MENU
# ============================================================

def display_menu():

    print("\n" + "=" * 55)
    print("          DATA ANALYSIS WITH PYTHON")
    print("=" * 55)

    print("1. Student Marks Statistics")
    print("2. Mean, Median and Mode")
    print("3. Highest / Lowest Analysis")
    print("4. Grade Distribution")
    print("5. Class Performance Analyzer")
    print("6. Display Student Data")
    print("7. Run All Analyses")
    print("8. Exit")

    print("=" * 55)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("\nWelcome to Data Analysis with Python!")

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        # ----------------------------------------------------
        # PROGRAM 101
        # ----------------------------------------------------

        if choice == "1":

            student_marks_statistics()

        # ----------------------------------------------------
        # PROGRAM 102
        # ----------------------------------------------------

        elif choice == "2":

            mean_median_mode()

        # ----------------------------------------------------
        # PROGRAM 103
        # ----------------------------------------------------

        elif choice == "3":

            highest_lowest_analysis()

        # ----------------------------------------------------
        # PROGRAM 104
        # ----------------------------------------------------

        elif choice == "4":

            grade_distribution()

        # ----------------------------------------------------
        # PROGRAM 105
        # ----------------------------------------------------

        elif choice == "5":

            class_performance_analyzer()

        # ----------------------------------------------------
        # DISPLAY DATA
        # ----------------------------------------------------

        elif choice == "6":

            display_students()

        # ----------------------------------------------------
        # RUN ALL
        # ----------------------------------------------------

        elif choice == "7":

            print(
                "\nRunning all data analyses..."
            )

            display_students()

            student_marks_statistics()

            mean_median_mode()

            highest_lowest_analysis()

            grade_distribution()

            class_performance_analyzer()

        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        elif choice == "8":

            print(
                "\nThank you for using "
                "Data Analysis with Python!"
            )

            break

        # ----------------------------------------------------
        # INVALID INPUT
        # ----------------------------------------------------

        else:

            print(
                "\nInvalid choice."
                " Please enter a number from 1 to 8."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()