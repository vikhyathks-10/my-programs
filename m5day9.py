# 🔹 DAY 9 - REGEX VALIDATION

import re


# 🔹 1. Email Validation

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


# 🔹 2. Phone Number Validation

def validate_phone(phone):
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, phone))


# 🔹 3. Username Validation

def validate_username(username):
    pattern = r'^[a-zA-Z0-9_]{4,15}$'
    return bool(re.match(pattern, username))


# 🔹 4. ZIP / PIN Code Checker

def validate_pin(pin):
    pattern = r'^\d{6}$'
    return bool(re.match(pattern, pin))


# 🔹 5. Password Pattern Check

def validate_password(password):
    pattern = (
        r'^(?=.*[A-Z])'      # at least 1 uppercase
        r'(?=.*[a-z])'       # at least 1 lowercase
        r'(?=.*\d)'          # at least 1 digit
        r'(?=.*[@$!%*?&])'   # at least 1 special char
        r'[A-Za-z\d@$!%*?&]{8,}$'
    )
    return bool(re.match(pattern, password))


# 🔹 MAIN PROGRAM

print("\n--- Email Validation ---")
print(validate_email("vikyat@gmail.com"))


print("\n--- Phone Validation ---")
print(validate_phone("9876543210"))


print("\n--- Username Validation ---")
print(validate_username("vikyat_123"))


print("\n--- PIN Code Validation ---")
print(validate_pin("560001"))


print("\n--- Password Validation ---")
print(validate_password("Strong@123"))