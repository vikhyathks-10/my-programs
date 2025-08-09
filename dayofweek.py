import datetime
date_input = input("Enter a date (dd-mm-yyyy): ")

try:
    date_obj = datetime.datetime.strptime(date_input, "%d-%m-%Y")
    day_name = date_obj.strftime("%A")
    print(f"The day of the week is: {day_name}")
except ValueError:
    print("Invalid date format. Please use dd-mm-yyyy.")
