text = input("Enter a string: ")

# 1️⃣1️⃣ Find frequency of a character
char = input("Enter character to find frequency: ")
freq = 0
for ch in text:
    if ch == char:
        freq += 1
print("Frequency:", freq)


# 1️⃣2️⃣ Remove special characters
clean = ""
for ch in text:
    if ch.isalnum() or ch == " ":
        clean += ch
print("Without special characters:", clean)


# 1️⃣3️⃣ Count digits in string
digit_count = 0
for ch in text:
    if ch.isdigit():
        digit_count += 1
print("Number of digits:", digit_count)


# 1️⃣4️⃣ Check string contains only alphabets
if text.isalpha():
    print("String contains only alphabets")
else:
    print("String does not contain only alphabets")


# 1️⃣5️⃣ Check string contains only numbers
if text.isdigit():
    print("String contains only numbers")
else:
    print("String does not contain only numbers")
