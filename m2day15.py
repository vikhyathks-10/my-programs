# Create list
n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    numbers.append(val)

print("\nOriginal List:", numbers)


# 1️⃣ Find Second Largest Element
unique = list(set(numbers))   # remove duplicates
if len(unique) >= 2:
    unique.sort()
    print("Second largest element:", unique[-2])
else:
    print("Second largest not found")


# 2️⃣ Count Positive & Negative Numbers
positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Positive count:", positive)
print("Negative count:", negative)


# 3️⃣ Replace Even Numbers with 0
modified = []

for num in numbers:
    if num % 2 == 0:
        modified.append(0)
    else:
        modified.append(num)

print("After replacing even numbers with 0:", modified)


# 4️⃣ Rotate List Elements (Left Rotation by 1)
if len(numbers) > 0:
    rotated = numbers[1:] + numbers[:1]
    print("List after left rotation:", rotated)
else:
    print("List is empty")


# 5️⃣ Find Missing Number in List (1 to n series)
# Assumes list should contain numbers from 1 to n with one missing

expected_sum = (len(numbers) + 1) * (len(numbers) + 2) // 2
actual_sum = sum(numbers)

missing = expected_sum - actual_sum
print("Missing number (if 1 to n series):", missing)
