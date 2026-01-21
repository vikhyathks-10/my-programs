# 1️⃣ Create a Tuple
n = int(input("How many elements in the tuple: "))
temp_list = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    temp_list.append(val)

my_tuple = tuple(temp_list)
print("\nTuple created:", my_tuple)


# 2️⃣ Tuple Length
length = 0
for _ in my_tuple:
    length += 1
print("Length of tuple:", length)


# 3️⃣ Maximum in Tuple
maximum = my_tuple[0]
for item in my_tuple:
    if item > maximum:
        maximum = item
print("Maximum element:", maximum)


# 4️⃣ Minimum in Tuple
minimum = my_tuple[0]
for item in my_tuple:
    if item < minimum:
        minimum = item
print("Minimum element:", minimum)


# 5️⃣ Convert Tuple to List
tuple_list = []
for item in my_tuple:
    tuple_list.append(item)

print("Tuple converted to list:", tuple_list)
