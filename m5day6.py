# 🔹 DAY 6 - COLLECTIONS MODULE

from collections import Counter, defaultdict, namedtuple, deque


# 🔹 1. Counter Example

print("\n--- Counter Example ---")

text = "programming"

counter = Counter(text)

print(counter)


# 🔹 2. defaultdict Usage

print("\n--- defaultdict Example ---")

students = defaultdict(list)

students["Python"].append("Vikyat")
students["Python"].append("Rahul")
students["Java"].append("Anil")

print(dict(students))


# 🔹 3. namedtuple Example

print("\n--- namedtuple Example ---")

Student = namedtuple("Student", ["name", "age", "course"])

s1 = Student("Vikyat", 19, "CS")

print("Name:", s1.name)
print("Age:", s1.age)
print("Course:", s1.course)


# 🔹 4. deque Operations

print("\n--- deque Operations ---")

dq = deque()

dq.append(10)
dq.append(20)
dq.appendleft(5)

print("Deque:", dq)

dq.pop()
print("After pop:", dq)

dq.popleft()
print("After popleft:", dq)


# 🔹 5. Frequency Counter App

print("\n--- Frequency Counter App ---")

sentence = "python is easy and python is powerful"

words = sentence.split()

freq = Counter(words)

for word, count in freq.items():
    print(word, "->", count)