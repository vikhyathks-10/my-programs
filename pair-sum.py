arr = [1, 2, 3, 4, 5, 6]
target = 7

print("Array:", arr)
print("Target Sum:", target)

pairs = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            pairs.append((arr[i], arr[j]))

print("Pairs with sum", target, ":", pairs)
