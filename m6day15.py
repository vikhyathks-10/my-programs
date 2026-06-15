# 🔹 DAY 15 - EXPENSE TRACKER

import csv
import os


class ExpenseTracker:

    FILE_NAME = "expenses.csv"

    # ==========================================
    # 🔹 Add Expense
    # ==========================================

    def add_expense(self):

        date = input("Enter Date (DD-MM-YYYY): ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))

        with open(self.FILE_NAME,
                  "a",
                  newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                date,
                category,
                amount
            ])

        print("✅ Expense Added Successfully")


    # ==========================================
    # 🔹 View Expenses
    # ==========================================

    def view_expenses(self):

        if not os.path.exists(self.FILE_NAME):

            print("No Expenses Found")
            return

        print("\nDate\t\tCategory\tAmount")

        with open(self.FILE_NAME,
                  "r") as file:

            reader = csv.reader(file)

            for row in reader:

                print(
                    f"{row[0]}\t{row[1]}\t\t₹{row[2]}"
                )


    # ==========================================
    # 🔹 Delete Expense
    # ==========================================

    def delete_expense(self):

        if not os.path.exists(self.FILE_NAME):

            print("No Expenses Found")
            return

        expenses = []

        with open(self.FILE_NAME,
                  "r") as file:

            reader = csv.reader(file)

            expenses = list(reader)

        for i, expense in enumerate(expenses):

            print(
                i + 1,
                expense
            )

        choice = int(
            input(
                "Enter Expense Number To Delete: "
            )
        )

        if 1 <= choice <= len(expenses):

            expenses.pop(choice - 1)

            with open(
                self.FILE_NAME,
                "w",
                newline=""
            ) as file:

                writer = csv.writer(file)

                writer.writerows(expenses)

            print("✅ Expense Deleted")

        else:

            print("Invalid Choice")


    # ==========================================
    # 🔹 Monthly Summary
    # ==========================================

    def monthly_summary(self):

        if not os.path.exists(self.FILE_NAME):

            print("No Expenses Found")
            return

        total = 0

        with open(self.FILE_NAME,
                  "r") as file:

            reader = csv.reader(file)

            for row in reader:

                total += float(row[2])

        print(
            f"\n💰 Total Monthly Expense: ₹{total}"
        )


    # ==========================================
    # 🔹 Category Wise Report
    # ==========================================

    def category_report(self):

        if not os.path.exists(self.FILE_NAME):

            print("No Expenses Found")
            return

        report = {}

        with open(self.FILE_NAME,
                  "r") as file:

            reader = csv.reader(file)

            for row in reader:

                category = row[1]

                amount = float(row[2])

                report[category] = (
                    report.get(category, 0)
                    + amount
                )

        print("\n📊 Category Report")

        for category, amount in report.items():

            print(
                category,
                "→ ₹",
                amount
            )


# ==========================================
# 🔹 MAIN PROGRAM
# ==========================================

tracker = ExpenseTracker()

while True:

    print("\n===== EXPENSE TRACKER =====")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Monthly Summary")
    print("5. Category Wise Report")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        tracker.add_expense()

    elif choice == "2":

        tracker.view_expenses()

    elif choice == "3":

        tracker.delete_expense()

    elif choice == "4":

        tracker.monthly_summary()

    elif choice == "5":

        tracker.category_report()

    elif choice == "6":

        print("Goodbye 👋")
        break

    else:

        print("Invalid Choice")