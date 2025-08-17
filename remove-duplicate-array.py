arr = [1, 2, 2, 3, 4, 4, 5]
unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("Array without duplicates:", unique)
