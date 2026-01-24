# Sample dictionary
data = {
    "name": "Vikyt",
    "course": "CS",
    "college": "PS College"
}

# 1️⃣ Print Keys
print("Dictionary Keys:")
for key in data.keys():
    print(key)


# 2️⃣ Print Values
print("\nDictionary Values:")
for value in data.values():
    print(value)


# 3️⃣ Count Characters in a String
text = input("\nEnter a string to count characters: ")
char_count = {}

for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print("Character count:", char_count)


# 4️⃣ Word Frequency
sentence = input("\nEnter a sentence: ")
words = sentence.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("Word frequency:", word_freq)


# 5️⃣ Student Marks Dictionary
students = {}
n = int(input("\nHow many students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Marks:")
for name, marks in students.items():
    print(name, ":", marks)
