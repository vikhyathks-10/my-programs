# Input string
text = input("Enter a string: ")

# 1️⃣ Convert to Uppercase
print("Uppercase:", text.upper())

# 2️⃣ Convert to Lowercase
print("Lowercase:", text.lower())

# 3️⃣ Replace a Character
old = input("Enter character to replace: ")
new = input("Enter new character: ")
print("After replacement:", text.replace(old, new))

# 4️⃣ Count Vowels
vowel_count = 0
for ch in text.lower():
    if ch in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1
print("Number of vowels:", vowel_count)

# 5️⃣ Remove Spaces
no_space = ""
for ch in text:
    if ch != " ":
        no_space += ch
print("String without spaces:", no_space)
