def leap_year_checker():
    year_input = input("Enter a year: ")
    if not year_input.isdigit():
        print("Please enter a valid year.")
        return
    year = int(year_input)

    if year % 400 == 0:
        print(f"{year} is a leap year.")
    elif year % 100 == 0:
        print(f"{year} is NOT a leap year.")
    elif year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is NOT a leap year.")

leap_year_checker()
