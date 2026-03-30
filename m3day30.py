import os

users_file = "bank_users.txt"

# Create file if not exists
if not os.path.exists(users_file):
    with open(users_file, "w") as f:
        pass


# -------- Helper Functions --------
def get_user(username):
    with open(users_file, "r") as f:
        for line in f:
            user, pwd, balance = line.strip().split(",")
            if user == username:
                return user, pwd, int(balance)
    return None


def update_user(username, new_balance):
    records = []

    with open(users_file, "r") as f:
        for line in f:
            user, pwd, balance = line.strip().split(",")
            if user == username:
                records.append(f"{user},{pwd},{new_balance}\n")
            else:
                records.append(line)

    with open(users_file, "w") as f:
        f.writelines(records)


# -------- Login System --------
def login():
    attempts = 3

    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        user_data = get_user(username)

        if user_data and user_data[1] == password:
            print("Login successful ✅")
            return username

        attempts -= 1
        print("Invalid credentials. Attempts left:", attempts)

    print("Account locked ❌")
    return None


# -------- Register --------
def register():
    username = input("Enter new username: ")
    password = input("Enter password: ")

    with open(users_file, "a") as f:
        f.write(f"{username},{password},0\n")

    print("Account created successfully.")


# -------- Main Menu --------
while True:

    print("\n------ ATM SYSTEM ------")
    print("1 Register")
    print("2 Login")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        user = login()

        if user:
            while True:
                print("\n--- ATM MENU ---")
                print("1 Check Balance")
                print("2 Deposit")
                print("3 Withdraw")
                print("4 Logout")

                opt = input("Enter option: ")

                user_data = get_user(user)
                balance = user_data[2]

                # Check Balance
                if opt == "1":
                    print("Balance:", balance)

                # Deposit
                elif opt == "2":
                    try:
                        amount = int(input("Enter amount: "))
                        if amount <= 0:
                            raise ValueError("Invalid amount")

                        balance += amount
                        update_user(user, balance)
                        print("Deposit successful. New Balance:", balance)

                    except ValueError as e:
                        print("Error:", e)

                # Withdraw
                elif opt == "3":
                    try:
                        amount = int(input("Enter amount: "))

                        if amount <= 0:
                            raise ValueError("Invalid amount")

                        if amount > balance:
                            raise ValueError("Insufficient balance")

                        balance -= amount
                        update_user(user, balance)
                        print("Withdraw successful. Remaining Balance:", balance)

                    except ValueError as e:
                        print("Error:", e)

                # Logout
                elif opt == "4":
                    print("Logged out.")
                    break

                else:
                    print("Invalid option")

    elif choice == "3":
        break

    else:
        print("Invalid choice")