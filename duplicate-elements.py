arr = [4, 3, 2, 7, 8, 2, 3, 1]
print("Array:", arr)

seen = set()
duplicates = set()

for num in arr:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicate Elements:", list(duplicates))
