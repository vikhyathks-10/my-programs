print("Welcome to Domino's Pizza!")
size = input("Choose pizza size (S/M/L): ").upper()
toppings = input("Do you want extra toppings? (yes/no): ").lower()
if size == 'S':
    price = 150
elif size == 'M':
    price = 200
elif size == 'L':
    price = 250
else:
    print("Invalid size selected.")
    exit()
if toppings == 'yes':
    price += 50
print(f"Total Bill: ₹{price}")
