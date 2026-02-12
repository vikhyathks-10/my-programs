import string

text = input("Enter a string: ")

# 1️⃣ Count substring occurrences
sub = input("Enter substring to count: ")
count = 0
start = 0

while True:
    pos = text.find(sub, start)
    if pos == -1:
        break
    count += 1
    start = pos + 1

print("Substring occurrences:", count)


# 2️⃣ Split string into words
words = text.split()
print("Words:", words)


# 3️⃣ Join words using delimiter
delimiter = "-"
joined = delimiter.join(words)
print("Joined with '-':", joined)


# 4️⃣ Capitalize first letter of each word
capitalized = text.title()
print("Capitalized:", capitalized)


# 5️⃣ Remove punctuation
clean = ""
for ch in text:
    if ch not in string.punctuation:
        clean += ch

print("Without punctuation:", clean)
