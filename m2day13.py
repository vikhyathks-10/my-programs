# 1️⃣ Create list and display
n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    numbers.append(val)

print("List created:", numbers)


# 2️⃣ Find sum of list elements
total = 0
for num in numbers:
    total += num
print("Sum of elements:", total)


# 3️⃣ Find maximum and minimum
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("Maximum:", maximum)
print("Minimum:", minimum)


# 4️⃣ Count even and odd numbers
even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)


# 5️⃣ Sort list (ascending & descending)
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending order:", ascending)
print("Descending order:", descending)
