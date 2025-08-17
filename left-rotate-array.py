arr = [1, 2, 3, 4, 5]
k = 2
temp = arr[:k]
for i in range(len(arr) - k):
    arr[i] = arr[i + k]
arr[-k:] = temp

print("Left Rotated Array:", arr)
