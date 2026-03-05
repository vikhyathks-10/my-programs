file_name = "sample.txt"

# Read file content
with open(file_name, "r") as file:
    text = file.read()

words = text.split()


# =====================================
# 1️⃣ Search for a Word in File
# =====================================
search_word = input("Enter word to search: ")

if search_word in words:
    print("Word found in file")
else:
    print("Word not found")


# =====================================
# 2️⃣ Count Occurrences of a Word
# =====================================
count = 0
for word in words:
    if word == search_word:
        count += 1

print("Occurrences of word:", count)


# =====================================
# 3️⃣ Replace a Word in File
# =====================================
replace_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

updated_text = text.replace(replace_word, new_word)

with open("updated.txt", "w") as file:
    file.write(updated_text)

print("Word replaced and saved to updated.txt")


# =====================================
# 4️⃣ Delete a Specific Word
# =====================================
delete_word = input("Enter word to delete: ")

filtered_words = []

for word in words:
    if word != delete_word:
        filtered_words.append(word)

new_text = " ".join(filtered_words)

with open("deleted_word.txt", "w") as file:
    file.write(new_text)

print("Word removed and saved to deleted_word.txt")


# =====================================
# 5️⃣ Find Lines Containing a Keyword
# =====================================
keyword = input("Enter keyword to find lines: ")

print("\nLines containing keyword:")
with open(file_name, "r") as file:
    for line in file:
        if keyword in line:
            print(line.strip())