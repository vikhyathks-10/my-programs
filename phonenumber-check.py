phone = input("Enter phone number: ")

if len(phone) == 10 and phone.isdigit():
    print("Valid phone number.")
else:
    print("Invalid input! Please enter a 10-digit phone number consisting of digits only.")