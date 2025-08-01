import time

water_count = 0

def show_menu():
    print("\nWater Intake Logger")
    print("1. Add a glass")
    print("2. Show total")
    print("3. Reset for today")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        water_count += 1
        print(f"Added! Total glasses today: {water_count}")
    elif choice == "2":
        print(f"You've had {water_count} glasses of water today.")
    elif choice == "3":
        confirm = input("Are you sure you want to reset? (yes/no): ").lower()
        if confirm == "yes":
            water_count = 0
            print("Count reset to 0.")
    elif choice == "4":
        print("Stay hydrated! Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
    time.sleep(1)
