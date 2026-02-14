# Create list
n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    numbers.append(val)

print("Original list:", numbers)


# 6️⃣ Reverse a list
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)


# 7️⃣ Search element (Linear Search)
key = int(input("Enter element to search: "))
found = False

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")


# 8️⃣ Remove duplicates
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print("List without duplicates:", unique)


# 9️⃣ Copy one list to another
copied_list = numbers.copy()
print("Copied list:", copied_list)


# 🔟 Merge two lists
n2 = int(input("Enter number of elements in second list: "))
list2 = []

for i in range(n2):
    val = int(input(f"Enter element {i+1}: "))
    list2.append(val)

merged = numbers + list2
print("Merged list:", merged)
