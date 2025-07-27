def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

try:
    user_input = input("Enter a year: ")
    year = int(user_input) 
    if year < 0:
        print("Please enter a valid positive year.")
    else:
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")

except:
    print("Invalid input! Please enter a valid numeric year.")
    

