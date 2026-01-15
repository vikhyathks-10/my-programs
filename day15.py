# 1️⃣ Print String
text = input("Enter a string: ")
print("You entered:", text)


# 2️⃣ String Length
length = 0
for ch in text:
    length += 1
print("Length of string:", length)


# 3️⃣ Reverse String
rev = ""
for ch in text:
    rev = ch + rev
print("Reversed string:", rev)


# 4️⃣ Check Palindrome String
if text == rev:
    print("Palindrome string")
else:
    print("Not a palindrome string")


# 5️⃣ Count Characters (excluding spaces)
count = 0
for ch in text:
    if ch != " ":
        count += 1
print("Total characters (without spaces):", count)
