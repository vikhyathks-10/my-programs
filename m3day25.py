filename = "users.txt"

# -------- Password Validation --------
def is_valid_password(password):
    if len(password) < 6:
        return "Password must be at least 6 characters"
    if not any(c.isdigit() for c in password):
        return "Password must contain a number"
    if not any(c.isupper() for c in password):
        return "Password must contain an uppercase letter"
    return "Valid"


while True:

    print("\n------ LOGIN & REGISTRATION SYSTEM ------")
    print("1 Register User")
    print("2 Login")
    print("3 Show All Users")
    print("4 Exit")

    choice = input("Enter choice: ")

    # 1 Register
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        check = is_valid_password(password)

        if check != "Valid":
            print("Error:", check)
            continue

        with open(filename, "a") as f:
            f.write(f"{username},{password}\n")

        print("User registered successfully.")

    # 2 Login
    elif choice == "2":
        user = input("Enter username: ")
        pwd = input("Enter password: ")

        found = False
        attempts = 3

        try:
            with open(filename, "r") as f:
                users = f.readlines()
        except FileNotFoundError:
            print("No users registered yet.")
            continue

        while attempts > 0:
            for line in users:
                u, p = line.strip().split(",")
                if u == user and p == pwd:
                    print("Login successful ✅")
                    found = True
                    break

            if found:
                break
            else:
                attempts -= 1
                print("Invalid credentials. Attempts left:", attempts)

                if attempts > 0:
                    user = input("Re-enter username: ")
                    pwd = input("Re-enter password: ")

        if not found:
            print("Account locked ❌")

    # 3 Show users
    elif choice == "3":
        try:
            with open(filename, "r") as f:
                print("\n--- Registered Users ---")
                for line in f:
                    username, _ = line.strip().split(",")
                    print(username)
        except FileNotFoundError:
            print("No users found.")

    # Exit
    elif choice == "4":
        break

    else:
        print("Invalid choice")