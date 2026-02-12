text = input("Enter a string: ")

# 6️⃣ Sort characters alphabetically
sorted_text = "".join(sorted(text.replace(" ", "")))
print("Sorted characters:", sorted_text)


# 7️⃣ Check rotation of string
s1 = input("Enter first string for rotation check: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Rotation of string")
else:
    print("Not rotation")


# 8️⃣ Find all duplicate words
words = text.lower().split()
freq = {}
duplicates = []

for word in words:
    freq[word] = freq.get(word, 0) + 1

for word in freq:
    if freq[word] > 1:
        duplicates.append(word)

print("Duplicate words:", duplicates)


# 9️⃣ Reverse words (not characters)
word_list = text.split()
reversed_words = " ".join(word_list[::-1])
print("Words reversed:", reversed_words)


# 🔟 Password strength checker
password = input("Enter password to check strength: ")

has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(not ch.isalnum() for ch in password)

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong password")
elif len(password) >= 6:
    print("Medium password")
else:
    print("Weak password")
