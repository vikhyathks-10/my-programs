# File name
file_name = "sample.txt"

# -------------------------------------
# Create the file if it does not exist
# -------------------------------------
with open(file_name, "w") as f:
    f.write("Python is a powerful programming language. "
            "Python is easy to learn and widely used.")

# =====================================
# 1️⃣ Count Number of Words
# =====================================
with open(file_name, "r") as file:
    text = file.read()

words = text.split()
print("Number of words:", len(words))


# =====================================
# 2️⃣ Count Number of Characters
# =====================================
char_count = len(text.replace("\n", ""))
print("Number of characters:", char_count)


# =====================================
# 3️⃣ Find Longest Word in File
# =====================================
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)


# =====================================
# 4️⃣ Convert File Content to Uppercase
# =====================================
upper_file = "uppercase.txt"

with open(upper_file, "w") as file:
    file.write(text.upper())

print("Uppercase content saved to uppercase.txt")


# =====================================
# 5️⃣ Remove Extra Spaces from File Text
# =====================================
clean_text = " ".join(text.split())

clean_file = "cleaned.txt"

with open(clean_file, "w") as file:
    file.write(clean_text)

print("File without extra spaces saved to cleaned.txt")