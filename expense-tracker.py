expenses = []
while True:
    print("\n1. Add Expense\n2. Show Expenses\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        cost = float(input("Enter cost: ₹"))
        expenses.append((item, cost))
        print("Expense added.")
    elif choice == "2":
        total = sum(cost for item, cost in expenses)
        print("\n--- Expense List ---")
        for item, cost in expenses:
            print(f"{item}: ₹{cost:.2f}")
        print(f"Total Spent: ₹{total:.2f}")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
