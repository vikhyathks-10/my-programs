# Create list
n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    numbers.append(val)

print("\nOriginal List:", numbers)


# 1️⃣ Multiply all elements
product = 1
for num in numbers:
    product *= num

print("Product of all elements:", product)


# 2️⃣ Check list is palindrome
is_palindrome = True
for i in range(len(numbers) // 2):
    if numbers[i] != numbers[len(numbers) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("List is Palindrome")
else:
    print("List is Not Palindrome")


# 3️⃣ Sort without using sort() (Bubble Sort)
sorted_list = numbers.copy()

for i in range(len(sorted_list)):
    for j in range(0, len(sorted_list) - i - 1):
        if sorted_list[j] > sorted_list[j + 1]:
            # swap
            sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

print("Sorted List (Bubble Sort):", sorted_list)


# 4️⃣ Find duplicates
duplicates = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

print("Duplicate elements:", duplicates)


# 5️⃣ Find intersection manually (with another list)
n2 = int(input("\nEnter number of elements in second list: "))
list2 = []

for i in range(n2):
    val = int(input(f"Enter element {i+1}: "))
    list2.append(val)

intersection = []
for num in numbers:
    if num in list2 and num not in intersection:
        intersection.append(num)

print("Intersection of lists:", intersection)
