# =====================================
# 1️⃣ Frequency of Words in Sentence
# =====================================
sentence = input("Enter a sentence: ").lower()
words = sentence.split()

word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("\nWord Frequency:", word_freq)


# =====================================
# 2️⃣ Dictionary Comprehension
# =====================================
n = int(input("\nEnter limit for square dictionary: "))
square_dict = {x: x*x for x in range(1, n+1)}

print("Dictionary using comprehension:", square_dict)


# =====================================
# 3️⃣ Convert Dictionary to List
# =====================================
dict_to_list = list(square_dict.items())
print("Dictionary converted to list:", dict_to_list)


# =====================================
# 4️⃣ Find Duplicate Values
# =====================================
sample_dict = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20}

values_seen = []
duplicate_values = []

for value in sample_dict.values():
    if value in values_seen and value not in duplicate_values:
        duplicate_values.append(value)
    else:
        values_seen.append(value)

print("Duplicate values:", duplicate_values)


# =====================================
# 5️⃣ Report Card Generator
# =====================================
students = {}
m = int(input("\nEnter number of students: "))

for i in range(m):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nReport Card")
for name, marks in students.items():
    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    print(name, ":", marks, "Grade:", grade)