data_input = input("Enter your total monthly data (in GB or type 'unlimited'): ").strip().lower()

if data_input == "unlimited":
    total_data = float('inf')  
else:
    try:
        total_data = float(data_input) 
    except ValueError:
        print("❌ Invalid input. Please enter a number or 'unlimited'.")
        exit()
try:
    daily_usage = float(input("Enter your daily data usage (in GB): "))
except ValueError:
    print("❌ Invalid input. Please enter a number.")
    exit()

remaining_data = total_data
day = 1
if total_data == float('inf'):
    print("\n♾️ Unlimited plan detected — tracking daily usage for 30 days...\n")
    for day in range(1, 31):
        print(f"Day {day}: Used {daily_usage:.2f} GB")
    print("\nEnjoy your unlimited data without worrying about limits!")
else:
    while remaining_data > 0:
        print(f"\nDay {day}:")
        remaining_data -= daily_usage

        if remaining_data < 0:
            remaining_data = 0

        print(f"Remaining Data: {remaining_data:.2f} GB")
        if remaining_data == 0:
            print("✅ You have used up all your data for the month.")
            break
        if remaining_data < (0.2 * total_data) and remaining_data > 0:
            print("⚠️ Warning: Your data is below 20%!")

        day += 1

    print("Please consider upgrading your plan or reducing usage.")
