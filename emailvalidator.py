email = input("Enter your email address: ")
if "@" in email and "." in email:
    parts = email.split("@")
    if len(parts) == 2 and parts[0] and "." in parts[1]:
        domain = parts[1].split(".")[-1]
        if domain in ["com", "in", "org", "net"]:
            print("Valid email.")
        else:
            print("Invalid email: Unknown domain.")
    else:
        print("Invalid email format.")
else:
    print("Invalid email: Missing '@' or '.'")
