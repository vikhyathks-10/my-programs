# 1️⃣ Create a Set
n1 = int(input("Enter number of elements in first set: "))
set1 = set()

for i in range(n1):
    val = input(f"Enter element {i+1}: ")
    set1.add(val)

print("\nFirst Set:", set1)


# 2️⃣ Add and Remove Elements
add_elem = input("\nEnter element to add: ")
set1.add(add_elem)
print("After adding:", set1)

remove_elem = input("Enter element to remove: ")
if remove_elem in set1:
    set1.remove(remove_elem)
    print("After removing:", set1)
else:
    print("Element not found in set")


# 3️⃣ Create Second Set
n2 = int(input("\nEnter number of elements in second set: "))
set2 = set()

for i in range(n2):
    val = input(f"Enter element {i+1}: ")
    set2.add(val)

print("Second Set:", set2)


# 4️⃣ Union of Two Sets
union_set = set1.union(set2)
print("Union:", union_set)


# 5️⃣ Intersection of Two Sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)


# 6️⃣ Difference of Sets
difference_set = set1.difference(set2)
print("Difference (Set1 - Set2):", difference_set)