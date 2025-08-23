arr = [3, 4, -1, 1]
print("Array:", arr)

arr = [x for x in arr if x > 0]  

missing = 1
for num in arr:
    if num == missing:
        missing += 1

print("First Missing Positive:", missing)
