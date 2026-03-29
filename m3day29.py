import random
import string
import datetime
import json

# -------- 1 Password Generator --------
def generate_password():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(chars) for _ in range(length))

    with open("passwords.txt", "a") as f:
        f.write(password + "\n")

    print("Generated Password:", password)
    print("Saved to passwords.txt")


# -------- 2 OTP Generator --------
def generate_otp():
    otp = random.randint(1000, 9999)
    print("Your OTP is:", otp)


# -------- 3 Date-based Log --------
def write_log():
    message = input("Enter log message: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    filename = f"log_{date}.txt"

    with open(filename, "a") as f:
        f.write(message + "\n")

    print("Log saved in", filename)


# -------- 4 Error Logging --------
def log_error():
    try:
        num = int(input("Enter number: "))
        result = 10 / num
        print("Result:", result)

    except Exception as e:
        with open("error_log.txt", "a") as f:
            f.write(str(e) + "\n")
        print("Error logged.")


# -------- 5 Config Reader --------
def read_config():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)

        print("\n--- Config Settings ---")
        for key, value in config.items():
            print(f"{key}: {value}")

    except FileNotFoundError:
        print("Config file not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")


# -------- Main Menu --------
while True:

    print("\n------ REAL-WORLD UTILITIES ------")
    print("1 Password Generator")
    print("2 OTP Generator")
    print("3 Write Log (Date-based)")
    print("4 Error Logging System")
    print("5 Read Config File")
    print("6 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        generate_password()

    elif choice == "2":
        generate_otp()

    elif choice == "3":
        write_log()

    elif choice == "4":
        log_error()

    elif choice == "5":
        read_config()

    elif choice == "6":
        break

    else:
        print("Invalid choice")