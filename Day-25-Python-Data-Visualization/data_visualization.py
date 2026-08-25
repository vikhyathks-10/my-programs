# ============================================================
# MONTH 8 - DAY 25
# PYTHON DATA VISUALIZATION
#
# Programs 126-130
#
# Concepts:
# matplotlib, charts, CSV, lists, dictionaries,
# statistics and data interpretation
#
# How to run:
# python data_visualization.py
# ============================================================

import csv
import os
import statistics
import matplotlib.pyplot as plt


# ============================================================
# CONFIGURATION
# ============================================================

CSV_FILE = "dashboard_data.csv"


# ============================================================
# PROGRAM 126
# BAR CHART GENERATOR
# ============================================================

def bar_chart_generator():

    print("\n" + "=" * 60)
    print("             PROGRAM 126 - BAR CHART")
    print("=" * 60)

    categories = input(
        "\nEnter categories separated by commas: "
    ).split(",")

    values_input = input(
        "Enter values separated by commas: "
    ).split(",")

    categories = [
        category.strip()
        for category in categories
    ]

    try:

        values = [
            float(value.strip())
            for value in values_input
        ]

    except ValueError:

        print(
            "\nError: Please enter only numbers."
        )

        return

    if len(categories) != len(values):

        print(
            "\nError: Number of categories and "
            "values must be the same."
        )

        return

    if not categories:

        print(
            "\nNo data entered."
        )

        return

    plt.figure(
        figsize=(8, 5)
    )

    plt.bar(
        categories,
        values
    )

    plt.title(
        "Bar Chart"
    )

    plt.xlabel(
        "Categories"
    )

    plt.ylabel(
        "Values"
    )

    plt.xticks(
        rotation=30
    )

    plt.tight_layout()

    plt.show()


# ============================================================
# PROGRAM 127
# STUDENT MARKS VISUALIZATION
# ============================================================

def student_marks_visualization():

    print("\n" + "=" * 60)
    print("          PROGRAM 127 - STUDENT MARKS")
    print("=" * 60)

    names = input(
        "\nEnter student names separated by commas: "
    ).split(",")

    marks_input = input(
        "Enter marks separated by commas: "
    ).split(",")

    names = [
        name.strip()
        for name in names
    ]

    try:

        marks = [
            float(mark.strip())
            for mark in marks_input
        ]

    except ValueError:

        print(
            "\nError: Marks must be numbers."
        )

        return

    if len(names) != len(marks):

        print(
            "\nError: Number of students and "
            "marks must be the same."
        )

        return

    if not names:

        print(
            "\nNo student data entered."
        )

        return

    plt.figure(
        figsize=(9, 5)
    )

    plt.bar(
        names,
        marks
    )

    plt.title(
        "Student Marks"
    )

    plt.xlabel(
        "Students"
    )

    plt.ylabel(
        "Marks"
    )

    plt.ylim(
        0,
        100
    )

    plt.xticks(
        rotation=30
    )

    plt.tight_layout()

    plt.show()


# ============================================================
# PROGRAM 128
# MONTHLY EXPENSE GRAPH
# ============================================================

def monthly_expense_graph():

    print("\n" + "=" * 60)
    print("          PROGRAM 128 - MONTHLY EXPENSE")
    print("=" * 60)

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    expenses = []

    print(
        "\nEnter your expenses for each month:"
    )

    for month in months:

        while True:

            try:

                expense = float(
                    input(
                        f"{month}: ₹"
                    )
                )

                if expense < 0:

                    print(
                        "Expense cannot be negative."
                    )

                    continue

                expenses.append(
                    expense
                )

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

    plt.figure(
        figsize=(10, 5)
    )

    plt.plot(
        months,
        expenses,
        marker="o"
    )

    plt.title(
        "Monthly Expense Trend"
    )

    plt.xlabel(
        "Month"
    )

    plt.ylabel(
        "Expense (₹)"
    )

    plt.xticks(
        rotation=45
    )

    plt.grid(
        True
    )

    plt.tight_layout()

    plt.show()

    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    total = sum(
        expenses
    )

    average = statistics.mean(
        expenses
    )

    highest = max(
        expenses
    )

    highest_month = months[
        expenses.index(highest)
    ]

    print("\nExpense Summary")

    print(
        f"Total Expense   : ₹{total:,.2f}"
    )

    print(
        f"Average Expense : ₹{average:,.2f}"
    )

    print(
        f"Highest Expense : ₹{highest:,.2f}"
    )

    print(
        f"Highest Month   : {highest_month}"
    )


# ============================================================
# PROGRAM 129
# WEATHER DATA VISUALIZATION
# ============================================================

def weather_data_visualization():

    print("\n" + "=" * 60)
    print("         PROGRAM 129 - WEATHER DATA")
    print("=" * 60)

    days_input = input(
        "\nEnter days separated by commas: "
    ).split(",")

    temperatures_input = input(
        "Enter temperatures separated by commas: "
    ).split(",")

    days = [
        day.strip()
        for day in days_input
    ]

    try:

        temperatures = [
            float(temp.strip())
            for temp in temperatures_input
        ]

    except ValueError:

        print(
            "\nError: Temperatures must be numbers."
        )

        return

    if len(days) != len(temperatures):

        print(
            "\nError: Number of days and "
            "temperatures must be the same."
        )

        return

    if not days:

        print(
            "\nNo weather data entered."
        )

        return

    plt.figure(
        figsize=(9, 5)
    )

    plt.plot(
        days,
        temperatures,
        marker="o"
    )

    plt.title(
        "Temperature Changes"
    )

    plt.xlabel(
        "Day"
    )

    plt.ylabel(
        "Temperature (°C)"
    )

    plt.grid(
        True
    )

    plt.tight_layout()

    plt.show()

    # --------------------------------------------------------
    # Temperature statistics
    # --------------------------------------------------------

    highest = max(
        temperatures
    )

    lowest = min(
        temperatures
    )

    average = statistics.mean(
        temperatures
    )

    highest_day = days[
        temperatures.index(highest)
    ]

    lowest_day = days[
        temperatures.index(lowest)
    ]

    print("\nWeather Summary")

    print(
        f"Average Temperature : "
        f"{average:.2f} °C"
    )

    print(
        f"Highest Temperature : "
        f"{highest:.2f} °C"
    )

    print(
        f"Highest Day         : "
        f"{highest_day}"
    )

    print(
        f"Lowest Temperature  : "
        f"{lowest:.2f} °C"
    )

    print(
        f"Lowest Day          : "
        f"{lowest_day}"
    )


# ============================================================
# CREATE SAMPLE CSV
# ============================================================

def create_sample_csv():

    if os.path.exists(CSV_FILE):

        return

    data = [
        {
            "category": "Food",
            "value": 4500
        },
        {
            "category": "Transport",
            "value": 2200
        },
        {
            "category": "Shopping",
            "value": 3500
        },
        {
            "category": "Entertainment",
            "value": 1800
        },
        {
            "category": "Education",
            "value": 5000
        }
    ]

    try:

        with open(
            CSV_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "category",
                    "value"
                ]
            )

            writer.writeheader()

            writer.writerows(
                data
            )

        print(
            f"\n'{CSV_FILE}' created successfully."
        )

    except Exception as e:

        print(
            f"\nError creating CSV: {e}"
        )


# ============================================================
# READ CSV DATA
# ============================================================

def read_csv_data():

    try:

        with open(
            CSV_FILE,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(
                file
            )

            data = list(
                reader
            )

        return data

    except FileNotFoundError:

        print(
            f"\n'{CSV_FILE}' not found."
        )

        return []

    except Exception as e:

        print(
            f"\nError reading CSV: {e}"
        )

        return []


# ============================================================
# PROGRAM 130
# MINI DATA DASHBOARD
# ============================================================

def mini_data_dashboard():

    print("\n" + "=" * 60)
    print("             PROGRAM 130 - DASHBOARD")
    print("=" * 60)

    data = read_csv_data()

    if not data:

        print(
            "\nNo CSV data available."
        )

        return

    categories = []

    values = []

    for row in data:

        category = row.get(
            "category",
            ""
        ).strip()

        value_text = row.get(
            "value",
            "0"
        ).strip()

        if not category:

            continue

        try:

            value = float(
                value_text
            )

        except ValueError:

            continue

        categories.append(
            category
        )

        values.append(
            value
        )

    if not values:

        print(
            "\nNo valid numerical data found."
        )

        return

    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    total = sum(
        values
    )

    average = statistics.mean(
        values
    )

    highest = max(
        values
    )

    lowest = min(
        values
    )

    highest_category = categories[
        values.index(highest)
    ]

    lowest_category = categories[
        values.index(lowest)
    ]

    # --------------------------------------------------------
    # Display Summary
    # --------------------------------------------------------

    print("\n" + "-" * 60)
    print("                 DATA SUMMARY")
    print("-" * 60)

    print(
        f"Number of Records : "
        f"{len(values)}"
    )

    print(
        f"Total Value       : "
        f"{total:,.2f}"
    )

    print(
        f"Average Value     : "
        f"{average:,.2f}"
    )

    print(
        f"Highest Value     : "
        f"{highest:,.2f}"
    )

    print(
        f"Highest Category  : "
        f"{highest_category}"
    )

    print(
        f"Lowest Value      : "
        f"{lowest:,.2f}"
    )

    print(
        f"Lowest Category   : "
        f"{lowest_category}"
    )

    print("-" * 60)

    # ========================================================
    # CHART 1 - BAR CHART
    # ========================================================

    plt.figure(
        figsize=(8, 5)
    )

    plt.bar(
        categories,
        values
    )

    plt.title(
        "Category Values"
    )

    plt.xlabel(
        "Category"
    )

    plt.ylabel(
        "Value"
    )

    plt.xticks(
        rotation=30
    )

    plt.tight_layout()

    plt.show()

    # ========================================================
    # CHART 2 - LINE CHART
    # ========================================================

    plt.figure(
        figsize=(8, 5)
    )

    plt.plot(
        categories,
        values,
        marker="o"
    )

    plt.title(
        "Value Trend"
    )

    plt.xlabel(
        "Category"
    )

    plt.ylabel(
        "Value"
    )

    plt.xticks(
        rotation=30
    )

    plt.grid(
        True
    )

    plt.tight_layout()

    plt.show()

    # ========================================================
    # CHART 3 - PIE CHART
    # ========================================================

    plt.figure(
        figsize=(7, 7)
    )

    plt.pie(
        values,
        labels=categories,
        autopct="%1.1f%%"
    )

    plt.title(
        "Value Distribution"
    )

    plt.tight_layout()

    plt.show()


# ============================================================
# RUN ALL PROGRAMS
# ============================================================

def run_all_programs():

    print(
        "\nRunning Programs 126-130..."
    )

    # --------------------------------------------------------
    # Program 126
    # --------------------------------------------------------

    print(
        "\nProgram 126:"
    )

    categories = [
        "Python",
        "C",
        "C++",
        "Java"
    ]

    values = [
        85,
        70,
        75,
        80
    ]

    plt.figure(
        figsize=(8, 5)
    )

    plt.bar(
        categories,
        values
    )

    plt.title(
        "Programming Language Interest"
    )

    plt.xlabel(
        "Language"
    )

    plt.ylabel(
        "Score"
    )

    plt.tight_layout()

    plt.show()

    # --------------------------------------------------------
    # Program 127
    # --------------------------------------------------------

    print(
        "\nProgram 127:"
    )

    students = [
        "Rahul",
        "Priya",
        "Arjun",
        "Sneha",
        "Kiran"
    ]

    marks = [
        78,
        88,
        72,
        91,
        84
    ]

    plt.figure(
        figsize=(8, 5)
    )

    plt.bar(
        students,
        marks
    )

    plt.title(
        "Student Marks"
    )

    plt.xlabel(
        "Student"
    )

    plt.ylabel(
        "Marks"
    )

    plt.ylim(
        0,
        100
    )

    plt.tight_layout()

    plt.show()

    # --------------------------------------------------------
    # Program 128
    # --------------------------------------------------------

    print(
        "\nProgram 128:"
    )

    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ]

    expenses = [
        4500,
        5200,
        4800,
        6100,
        5700,
        6500
    ]

    plt.figure(
        figsize=(8, 5)
    )

    plt.plot(
        months,
        expenses,
        marker="o"
    )

    plt.title(
        "Monthly Expenses"
    )

    plt.xlabel(
        "Month"
    )

    plt.ylabel(
        "Expense (₹)"
    )

    plt.grid(
        True
    )

    plt.tight_layout()

    plt.show()

    # --------------------------------------------------------
    # Program 129
    # --------------------------------------------------------

    print(
        "\nProgram 129:"
    )

    days = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ]

    temperatures = [
        25,
        27,
        26,
        29,
        30,
        28,
        27
    ]

    plt.figure(
        figsize=(8, 5)
    )

    plt.plot(
        days,
        temperatures,
        marker="o"
    )

    plt.title(
        "Weekly Temperature"
    )

    plt.xlabel(
        "Day"
    )

    plt.ylabel(
        "Temperature (°C)"
    )

    plt.grid(
        True
    )

    plt.tight_layout()

    plt.show()

    # --------------------------------------------------------
    # Program 130
    # --------------------------------------------------------

    print(
        "\nProgram 130:"
    )

    mini_data_dashboard()


# ============================================================
# MENU
# ============================================================

def display_menu():

    print("\n" + "=" * 65)
    print("             PYTHON DATA VISUALIZATION")
    print("=" * 65)

    print("1. Bar Chart Generator")
    print("2. Student Marks Visualization")
    print("3. Monthly Expense Graph")
    print("4. Weather Data Visualization")
    print("5. Mini Data Dashboard")
    print("6. Run All Programs")
    print("7. Exit")

    print("=" * 65)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    create_sample_csv()

    print(
        "\nWelcome to Python Data Visualization!"
    )

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        # ----------------------------------------------------
        # Program 126
        # ----------------------------------------------------

        if choice == "1":

            bar_chart_generator()

        # ----------------------------------------------------
        # Program 127
        # ----------------------------------------------------

        elif choice == "2":

            student_marks_visualization()

        # ----------------------------------------------------
        # Program 128
        # ----------------------------------------------------

        elif choice == "3":

            monthly_expense_graph()

        # ----------------------------------------------------
        # Program 129
        # ----------------------------------------------------

        elif choice == "4":

            weather_data_visualization()

        # ----------------------------------------------------
        # Program 130
        # ----------------------------------------------------

        elif choice == "5":

            mini_data_dashboard()

        # ----------------------------------------------------
        # Run all
        # ----------------------------------------------------

        elif choice == "6":

            run_all_programs()

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        elif choice == "7":

            print(
                "\nThank you for using "
                "Python Data Visualization!"
            )

            break

        else:

            print(
                "\nInvalid choice."
                " Please enter a number from 1 to 7."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()