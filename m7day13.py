# ==========================================================
# Month 7 - Day 13
# Python Collections Module
#
# Topics Covered:
# 1. Counter
# 2. defaultdict
# 3. OrderedDict
# 4. namedtuple
# 5. ChainMap
# 6. Counter-Based Problems
# ==========================================================

from collections import Counter, defaultdict, OrderedDict, namedtuple, ChainMap

print("=" * 60)
print("1. COUNTER")
print("=" * 60)

text = "programming"

counter = Counter(text)

print("Character Frequency:")
print(counter)

print("\nMost Common Characters:")
print(counter.most_common(3))


print("\n" + "=" * 60)
print("2. DEFAULTDICT")
print("=" * 60)

students = [
    ("CSE", "Alice"),
    ("ECE", "Bob"),
    ("CSE", "Charlie"),
    ("EEE", "David"),
    ("ECE", "Eva")
]

department = defaultdict(list)

for branch, student in students:
    department[branch].append(student)

print("Students Grouped by Department:")

for key, value in department.items():
    print(key, ":", value)


print("\n" + "=" * 60)
print("3. ORDEREDDICT")
print("=" * 60)

ordered = OrderedDict()

ordered["Apple"] = 100
ordered["Banana"] = 50
ordered["Mango"] = 120

print("Items in Insertion Order:")

for key, value in ordered.items():
    print(key, ":", value)


print("\n" + "=" * 60)
print("4. NAMEDTUPLE")
print("=" * 60)

Student = namedtuple("Student", ["name", "age", "branch"])

s1 = Student("Vikhyath", 20, "CSE")

print("Student Details")
print("Name   :", s1.name)
print("Age    :", s1.age)
print("Branch :", s1.branch)


print("\n" + "=" * 60)
print("5. CHAINMAP")
print("=" * 60)

defaults = {
    "language": "Python",
    "editor": "VS Code"
}

user = {
    "editor": "PyCharm"
}

settings = ChainMap(user, defaults)

print("Language :", settings["language"])
print("Editor   :", settings["editor"])


print("\n" + "=" * 60)
print("6. COUNTER-BASED PROBLEM")
print("=" * 60)

numbers = [1,2,2,3,3,3,4,4,4,4]

frequency = Counter(numbers)

print("Frequency:")

for num, count in frequency.items():
    print(num, ":", count)

print("\nMost Frequent Element:")
print(frequency.most_common(1)[0])


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ Counter

Counts frequency of elements.

Example:

Counter("banana")

Returns

{'a':3,'n':2,'b':1}

Useful Methods:

most_common()
elements()
update()

Time:
O(n)

--------------------------------------------------

✔ defaultdict

Automatically creates
default values.

Example:

defaultdict(list)

No KeyError.

--------------------------------------------------

✔ OrderedDict

Maintains insertion order.

(Regular dictionaries also preserve
insertion order in Python 3.7+.)

--------------------------------------------------

✔ namedtuple

Tuple with named fields.

Example:

student.name

instead of

student[0]

--------------------------------------------------

✔ ChainMap

Combines multiple dictionaries
without copying them.

Searches dictionaries from
left to right.

--------------------------------------------------

✔ Counter Interview Problems

• Character Frequency
• Word Frequency
• Majority Element
• Most Frequent Element
• Duplicate Detection

--------------------------------------------------

Interview Tip

Whenever you hear:

✔ Frequency
✔ Counting
✔ Grouping
✔ Mapping

Think:

👉 collections module

Important Classes:

Counter
defaultdict
OrderedDict
namedtuple
ChainMap
""")