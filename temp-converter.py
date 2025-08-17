def temperature_converter():
    print("Choose conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        celsius_input = input("Enter temperature in Celsius: ")
        try:
            celsius = float(celsius_input)
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "2":
        fahrenheit_input = input("Enter temperature in Fahrenheit: ")
        try:
            fahrenheit = float(fahrenheit_input)
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F = {celsius:.2f}°C")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Invalid choice.")

temperature_converter()

