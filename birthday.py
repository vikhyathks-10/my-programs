from datetime import datetime

birth_day = int(input("Enter your birthday date (1-31): "))
birth_month = int(input("Enter your birth month (1-12): "))

today = datetime.now()
birthday_this_year = datetime(today.year, birth_month, birth_day)

if birthday_this_year < today:
    birthday_next = datetime(today.year + 1, birth_month, birth_day)
else:
    birthday_next = birthday_this_year

days_left = (birthday_next - today).days

print(f"Your birthday is in {days_left} days!")
if days_left == 0:
    print("Happy Birthday! Enjoy your special day!")