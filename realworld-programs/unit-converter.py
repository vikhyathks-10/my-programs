print("Distance Converter")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
choice = input("Choose conversion (1 or 2): ")

if choice == "1":
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.621371
    print(f"{km} km = {miles:.2f} miles")

elif choice == "2":
    miles = float(input("Enter distance in miles: "))
    km = miles / 0.621371
    print(f"{miles} miles = {km:.2f} km")

else:
    print("Invalid choice. Please enter 1 or 2.")
