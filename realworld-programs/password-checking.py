import string
password = input("Enter your password: ")
length_ok = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in string.punctuation for char in password)
score = sum([length_ok, has_upper, has_lower, has_digit, has_special])
if score <= 2:
    strength = "Weak"
elif score == 3 or score == 4:
    strength = "Medium"
else:
    strength = "Strong"

print(f"Password strength: {strength}")
