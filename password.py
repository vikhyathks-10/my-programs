import string

password = input("Enter a password: ")

length = len(password) >= 8
digit = any(c.isdigit() for c in password)
lower = any(c.islower() for c in password)
upper = any(c.isupper() for c in password)
special = any(c in string.punctuation for c in password)

if length and digit and lower and upper and special:
    print("✅ Strong Password")
else:
    print("❌ Weak Password")
    print("Tips to improve:")
    if not length:
        print("- Use at least 8 characters")
    if not digit:
        print("- Include numbers")
    if not lower:
        print("- Include lowercase letters")
    if not upper:
        print("- Include uppercase letters")
    if not special:
        print("- Add special characters (e.g., !,@,#)")
