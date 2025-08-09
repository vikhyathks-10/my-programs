import re

def validate_plate(number_plate):
    pattern = r"^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$"
    return re.match(pattern, number_plate.upper())
plate = input("Enter vehicle number plate (e.g., KA01AB1234): ").upper()

if validate_plate(plate):
    print("✅ Valid number plate.")
else:
    print("❌ Invalid number plate format.")
