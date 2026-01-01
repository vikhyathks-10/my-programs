# 1. MOVE ALL ZEROS TO THE END OF THE ARRAY
arr = [0, 1, 0, 3, 12]
index = 0

for num in arr:
    if num != 0:
        arr[index] = num
        index += 1

while index < len(arr):
    arr[index] = 0
    index += 1

print("1. Array after moving zeros to end:", arr)

# 2. FIND INTERSECTION OF TWO ARRAYS
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
intersection = []

for num in arr1:
    if num in arr2 and num not in intersection:
        intersection.append(num)

print("\n2. Intersection of arrays:", intersection)

# 3. FIND UNION OF TWO ARRAYS
union = []

for num in arr1:
    if num not in union:
        union.append(num)

for num in arr2:
    if num not in union:
        union.append(num)

print("\n3. Union of arrays:", union)

# 4. MAXIMUM SUBARRAY SUM (KADANE'S ALGORITHM)
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = arr[0]
current_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print("\n4. Maximum Subarray Sum:", max_sum)

# 5. FIND LEADERS IN AN ARRAY
arr = [16, 17, 4, 3, 5, 2]
leaders = []
max_from_right = arr[-1]
leaders.append(max_from_right)

for i in range(len(arr) - 2, -1, -1):
    if arr[i] > max_from_right:
        leaders.append(arr[i])
        max_from_right = arr[i]

leaders.reverse()
print("\n5. Leaders in the array:", leaders)
