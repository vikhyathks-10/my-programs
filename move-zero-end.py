arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6]
print("Original Array:", arr)

pos = 0 
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1
while pos < len(arr):
    arr[pos] = 0
    pos += 1

print("Array after moving zeros:", arr)
