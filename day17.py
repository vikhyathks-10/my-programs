# 1️⃣ Create a List
numbers = []
n = int(input("How many elements you want to add: "))

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    numbers.append(val)

print("\nList created:", numbers)


# 2️⃣ Print List Elements
print("\nList elements are:")
for item in numbers:
    print(item)


# 3️⃣ Sum of List Elements
total = 0
for item in numbers:
    total += item

print("\nSum of elements:", total)


# 4️⃣ Largest Element
largest = numbers[0]
for item in numbers:
    if item > largest:
        largest = item

print("Largest element:", largest)


# 5️⃣ Smallest Element
smallest = numbers[0]
for item in numbers:
    if item < smallest:
        smallest = item

print("Smallest element:", smallest)
