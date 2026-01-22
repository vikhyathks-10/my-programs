# 1️⃣ Create a Set
n1 = int(input("How many elements in first set: "))
set1 = set()

for i in range(n1):
    val = int(input(f"Enter element {i+1}: "))
    set1.add(val)

print("\nFirst Set:", set1)


# 2️⃣ Create Second Set
n2 = int(input("\nHow many elements in second set: "))
set2 = set()

for i in range(n2):
    val = int(input(f"Enter element {i+1}: "))
    set2.add(val)

print("Second Set:", set2)


# 3️⃣ Union of Sets
union_set = set1.union(set2)
print("\nUnion:", union_set)


# 4️⃣ Intersection of Sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)


# 5️⃣ Difference of Sets
difference_set = set1.difference(set2)
print("Difference (Set1 - Set2):", difference_set)


# 6️⃣ Remove Duplicates Using Set
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))

print("\nOriginal List:", nums)
print("List without duplicates:", unique_nums)
