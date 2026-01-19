# Create a list
numbers = []
n = int(input("How many elements you want to add: "))

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    numbers.append(val)

print("\nOriginal List:", numbers)


# 1️⃣ Sort the List
sorted_list = numbers.copy()
sorted_list.sort()
print("Sorted List:", sorted_list)


# 2️⃣ Reverse the List
reversed_list = numbers.copy()
reversed_list.reverse()
print("Reversed List:", reversed_list)


# 3️⃣ Count an Element
element = int(input("\nEnter element to count: "))
count = 0
for item in numbers:
    if item == element:
        count += 1
print(f"{element} appears {count} times")


# 4️⃣ Remove Duplicates
unique_list = []
for item in numbers:
    if item not in unique_list:
        unique_list.append(item)
print("List without duplicates:", unique_list)


# 5️⃣ Find Index of an Element
search = int(input("\nEnter element to find index: "))
found = False

for i in range(len(numbers)):
    if numbers[i] == search:
        print(f"Index of {search} is:", i)
        found = True
        break

if not found:
    print("Element not found in list")
