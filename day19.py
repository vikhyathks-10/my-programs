# Create first list
list1 = []
n1 = int(input("How many elements in first list: "))

for i in range(n1):
    val = int(input(f"Enter element {i+1}: "))
    list1.append(val)

print("\nFirst List:", list1)


# 1️⃣ Even numbers from list
print("\nEven numbers:")
for item in list1:
    if item % 2 == 0:
        print(item)


# 2️⃣ Odd numbers from list
print("\nOdd numbers:")
for item in list1:
    if item % 2 != 0:
        print(item)


# 3️⃣ Square each element
print("\nSquares of elements:")
for item in list1:
    print(item, "square =", item * item)


# Create second list
list2 = []
n2 = int(input("\nHow many elements in second list: "))

for i in range(n2):
    val = int(input(f"Enter element {i+1}: "))
    list2.append(val)

print("Second List:", list2)


# 4️⃣ Merge two lists
merged_list = list1 + list2
print("\nMerged List:", merged_list)


# 5️⃣ Common elements
print("Common elements:")
found = False
for item in list1:
    if item in list2:
        print(item)
        found = True

if not found:
    print("No common elements found")
