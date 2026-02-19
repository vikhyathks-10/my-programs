# 1️⃣ Create and Access Tuple
n = int(input("Enter number of elements in tuple: "))
temp = []

for i in range(n):
    val = input(f"Enter element {i+1}: ")
    temp.append(val)

my_tuple = tuple(temp)

print("\nTuple created:", my_tuple)

# Access elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])


# 2️⃣ Find Length of Tuple
length = 0
for _ in my_tuple:
    length += 1

print("Length of tuple:", length)


# 3️⃣ Find Max and Min (numeric only)
numeric_tuple = tuple(int(x) for x in my_tuple if x.isdigit())

if numeric_tuple:
    maximum = numeric_tuple[0]
    minimum = numeric_tuple[0]

    for num in numeric_tuple:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    print("Maximum:", maximum)
    print("Minimum:", minimum)
else:
    print("No numeric elements to find max/min")


# 4️⃣ Count Element Frequency
frequency = {}

for item in my_tuple:
    frequency[item] = frequency.get(item, 0) + 1

print("Element frequency:", frequency)


# 5️⃣ Convert Tuple to List
tuple_list = list(my_tuple)
print("Converted to list:", tuple_list)
