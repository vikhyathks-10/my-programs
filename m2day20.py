# Create first tuple
n1 = int(input("Enter number of elements in first tuple: "))
t1 = []

for i in range(n1):
    val = input(f"Enter element {i+1}: ")
    t1.append(val)

tuple1 = tuple(t1)


# Create second tuple
n2 = int(input("\nEnter number of elements in second tuple: "))
t2 = []

for i in range(n2):
    val = input(f"Enter element {i+1}: ")
    t2.append(val)

tuple2 = tuple(t2)

print("\nTuple1:", tuple1)
print("Tuple2:", tuple2)


# 1️⃣ Merge two tuples
merged = tuple1 + tuple2
print("Merged tuple:", merged)


# 2️⃣ Check element exists
element = input("\nEnter element to check existence: ")

if element in merged:
    print("Element exists in tuple")
else:
    print("Element does not exist")


# 3️⃣ Reverse tuple
reversed_tuple = merged[::-1]
print("Reversed tuple:", reversed_tuple)


# 4️⃣ Sort tuple (numeric only)
numeric_tuple = tuple(int(x) for x in merged if x.isdigit())

if numeric_tuple:
    sorted_tuple = tuple(sorted(numeric_tuple))
    print("Sorted numeric tuple:", sorted_tuple)
else:
    print("No numeric elements to sort")


# 5️⃣ Nested tuple access
nested = ((1, 2), (3, 4), (5, 6))
print("\nNested tuple:", nested)
print("Access element 4:", nested[1][1])