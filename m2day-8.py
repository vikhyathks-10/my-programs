text = input("Enter a string: ")

# 6️⃣ Remove spaces from string
no_space = ""
for ch in text:
    if ch != " ":
        no_space += ch
print("Without spaces:", no_space)


# 7️⃣ Convert to uppercase/lowercase
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())


# 8️⃣ Find longest word
words = text.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)


# 9️⃣ Find shortest word
shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print("Shortest word:", shortest)


# 🔟 Replace a word in string
old = input("Enter word to replace: ")
new = input("Enter new word: ")
print("Updated string:", text.replace(old, new))
