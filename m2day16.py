# Create first list
n = int(input("Enter number of elements in list: "))
numbers = []

for i in range(n):
    val = input(f"Enter element {i+1}: ")
    numbers.append(val)

print("\nOriginal List:", numbers)


# 1️⃣ Frequency of each element
frequency = {}

for item in numbers:
    frequency[item] = frequency.get(item, 0) + 1

print("Frequency of each element:", frequency)


# 2️⃣ Find common elements between two lists
n2 = int(input("\nEnter number of elements in second list: "))
list2 = []

for i in range(n2):
    val = input(f"Enter element {i+1}: ")
    list2.append(val)

common = []
for item in numbers:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements:", common)


# 3️⃣ Find unique elements (no duplicates)
unique = []
for item in numbers:
    if numbers.count(item) == 1:
        unique.append(item)

print("Unique elements:", unique)


# 4️⃣ Split list into even & odd lists (numeric elements only)
even = []
odd = []

for item in numbers:
    if item.isdigit():
        num = int(item)
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

print("Even list:", even)
print("Odd list:", odd)


# 5️⃣ Remove empty elements
cleaned = []
for item in numbers:
    if item.strip() != "":
        cleaned.append(item)

print("List without empty elements:", cleaned)
