# Create first set
n1 = int(input("Enter number of elements in first set: "))
set1 = set()

for i in range(n1):
    val = input(f"Enter element {i+1}: ")
    set1.add(val)

print("\nFirst Set:", set1)


# Create second set
n2 = int(input("\nEnter number of elements in second set: "))
set2 = set()

for i in range(n2):
    val = input(f"Enter element {i+1}: ")
    set2.add(val)

print("Second Set:", set2)


# 1️⃣ Symmetric Difference
sym_diff = set1.symmetric_difference(set2)
print("\nSymmetric Difference:", sym_diff)


# 2️⃣ Find Unique Elements from List
lst = input("\nEnter elements of list separated by space: ").split()
unique_elements = set(lst)
print("Unique elements from list:", unique_elements)


# 3️⃣ Remove Duplicates Using Set
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
no_duplicates = list(set(duplicate_list))
print("Original list:", duplicate_list)
print("List after removing duplicates:", no_duplicates)


# 4️⃣ Check Subset
if set1.issubset(set2):
    print("Set1 is subset of Set2")
else:
    print("Set1 is not subset of Set2")


# 5️⃣ Set Menu-Driven Program
while True:
    print("\nSet Menu:")
    print("1. Add element")
    print("2. Remove element")
    print("3. Display set")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        elem = input("Enter element to add: ")
        set1.add(elem)

    elif choice == 2:
        elem = input("Enter element to remove: ")
        if elem in set1:
            set1.remove(elem)
        else:
            print("Element not found")

    elif choice == 3:
        print("Current Set:", set1)

    elif choice == 4:
        break

    else:
        print("Invalid choice")