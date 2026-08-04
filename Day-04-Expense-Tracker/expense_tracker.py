import csv
import os

FILENAME = "expenses.csv"


class ExpenseTracker:

    def __init__(self):
        if not os.path.exists(FILENAME):
            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Category", "Description", "Amount"])

    def add_expense(self):
        date = input("Enter Date (DD-MM-YYYY): ")
        category = input("Enter Category: ")
        description = input("Enter Description: ")
        amount = float(input("Enter Amount: "))

        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])

        print("\nExpense Added Successfully!")

    def view_expenses(self):

        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            print("\n===== ALL EXPENSES =====\n")

            for row in reader:
                print("{:<15}{:<15}{:<25}{:<10}".format(*row))

    def search_category(self):

        category = input("Enter Category: ")

        found = False

        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            print()

            for row in reader:

                if len(row) > 1 and row[1].lower() == category.lower():
                    print(row)
                    found = True

        if not found:
            print("No Expenses Found.")

    def delete_expense(self):

        description = input("Enter Description to Delete: ")

        rows = []

        deleted = False

        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:

                if row[2] == description:
                    deleted = True
                    continue

                rows.append(row)

        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        if deleted:
            print("Expense Deleted Successfully.")
        else:
            print("Expense Not Found.")

    def monthly_summary(self):

        total = 0

        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            next(reader)

            for row in reader:
                total += float(row[3])

        print(f"\nTotal Monthly Expense : ₹{total:.2f}")

    def category_summary(self):

        summary = {}

        with open(FILENAME, "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:

                category = row[1]
                amount = float(row[3])

                summary[category] = summary.get(category, 0) + amount

        print("\n===== CATEGORY SUMMARY =====")

        for category, amount in summary.items():
            print(category, ":", amount)


tracker = ExpenseTracker()

while True:

    print("\n========= EXPENSE TRACKER =========")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Category")
    print("4. Delete Expense")
    print("5. Monthly Summary")
    print("6. Category Summary")
    print("7. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":
        tracker.add_expense()

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.search_category()

    elif choice == "4":
        tracker.delete_expense()

    elif choice == "5":
        tracker.monthly_summary()

    elif choice == "6":
        tracker.category_summary()

    elif choice == "7":
        print("\nThank You!")
        break

    else:
        print("Invalid Choice.")