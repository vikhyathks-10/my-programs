arr = [1, 2, 3, 4, 5]
k = 2
print("Original Array:", arr)

k = k % len(arr)  
rotated = arr[-k:] + arr[:-k]

print("Array after rotating by", k, "positions:", rotated)
