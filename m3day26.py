import os

accounts_file = "accounts.txt"
transactions_file = "transactions.txt"


# -------- Helper: Find Account --------
def find_account(username):
    if not os.path.exists(accounts_file):
        return None

    with open(accounts_file, "r") as f:
        for line in f:
            user, balance = line.strip().split(",")
            if user == username:
                return int(balance)
    return None


# -------- Helper: Update Balance --------
def update_balance(username, new_balance):
    records = []

    with open(accounts_file, "r") as f:
        for line in f:
            user, balance = line.strip().split(",")
            if user == username:
                records.append(f"{user},{new_balance}\n")
            else:
                records.append(line)

    with open(accounts_file, "w") as f:
        f.writelines(records)


# -------- Main Program --------
while True:

    print("\n------ BANK SYSTEM ------")
    print("1 Create Account")
    print("2 Deposit")
    print("3 Withdraw")
    print("4 Check Balance")
    print("5 Transaction History")
    print("6 Exit")

    choice = input("Enter choice: ")

    # 1 Create Account
    if choice == "1":
        username = input("Enter username: ")

        if find_account(username) is not None:
            print("Account already exists.")
            continue

        with open(accounts_file, "a") as f:
            f.write(f"{username},0\n")

        print("Account created successfully.")

    # 2 Deposit
    elif choice == "2":
        username = input("Enter username: ")
        amount = int(input("Enter amount: "))

        balance = find_account(username)

        if balance is None:
            print("Account not found.")
            continue

        new_balance = balance + amount
        update_balance(username, new_balance)

        with open(transactions_file, "a") as f:
            f.write(f"{username},DEPOSIT,{amount}\n")

        print("Deposit successful. New Balance:", new_balance)

    # 3 Withdraw
    elif choice == "3":
        username = input("Enter username: ")
        amount = int(input("Enter amount: "))

        balance = find_account(username)

        if balance is None:
            print("Account not found.")
            continue

        if amount > balance:
            print("Insufficient balance.")
            continue

        new_balance = balance - amount
        update_balance(username, new_balance)

        with open(transactions_file, "a") as f:
            f.write(f"{username},WITHDRAW,{amount}\n")

        print("Withdrawal successful. Remaining Balance:", new_balance)

    # 4 Check Balance
    elif choice == "4":
        username = input("Enter username: ")

        balance = find_account(username)

        if balance is None:
            print("Account not found.")
        else:
            print("Current Balance:", balance)

    # 5 Transaction History
    elif choice == "5":
        username = input("Enter username: ")

        if not os.path.exists(transactions_file):
            print("No transactions yet.")
            continue

        print("\n--- Transaction History ---")

        with open(transactions_file, "r") as f:
            found = False
            for line in f:
                user, action, amount = line.strip().split(",")
                if user == username:
                    print(f"{action} -> {amount}")
                    found = True

        if not found:
            print("No transactions found.")

    # Exit
    elif choice == "6":
        break

    else:
        print("Invalid choice")