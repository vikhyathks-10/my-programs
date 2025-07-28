import datetime
birth_year = int(input("Enter your birth year: "))
current_year = datetime.datetime.now().year
age = current_year - birth_year
print(f"\nYou are {age} years old.")
