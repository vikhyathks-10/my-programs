import random
import string

while True:
    print("\n----- RANDOM MODULE PROGRAM -----")
    print("1. Random Number Generator")
    print("2. Dice Simulator")
    print("3. Password Generator")
    print("4. Lottery Number Picker")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # 1 Random Number Generator
    if choice == "1":
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))
        num = random.randint(start, end)
        print("Random Number:", num)

    # 2 Dice Simulator
    elif choice == "2":
        dice = random.randint(1, 6)
        print("Dice rolled:", dice)

    # 3 Password Generator
    elif choice == "3":
        length = int(input("Enter password length: "))
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)

    # 4 Lottery Number Picker
    elif choice == "4":
        numbers = random.sample(range(1, 50), 6)
        print("Lottery Numbers:", numbers)

    # Exit
    elif choice == "5":
        print("Program exited.")
        break

    else:
        print("Invalid choice.")