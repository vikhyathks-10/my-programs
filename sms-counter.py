msg = input("Enter SMS Text: ")

length = len(msg)
print("Characters:", length)

if length > 160:
    pages = (length // 160) + 1
    print("This will take", pages, "SMS messages.")
else:
    print("It fits in one SMS.")
