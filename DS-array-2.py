# 1. COUNT FREQUENCY OF EACH ELEMENT
arr = [1, 2, 2, 3, 1, 4, 2]
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("1. Frequency of each element:")
for key in freq:
    print(key, "->", freq[key])

# 2. MERGE TWO SORTED ARRAYS INTO ONE SORTED ARRAY
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

i = j = 0
merged = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

while i < len(arr1):
    merged.append(arr1[i])
    i += 1

while j < len(arr2):
    merged.append(arr2[j])
    j += 1

print("\n2. Merged Sorted Array:", merged)

# 3. FIND THE MISSING NUMBER (ARRAY SIZE n-1)
arr = [1, 2, 4, 5, 6]
n = 6

total_sum = n * (n + 1) // 2
arr_sum = sum(arr)

missing = total_sum - arr_sum
print("\n3. Missing Number:", missing)

# 4. FIND ALL PAIRS WITH A GIVEN SUM
arr = [2, 4, 3, 5, 7, 8]
target = 7

print("\n4. Pairs with sum", target, ":")
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])

# 5. CHECK IF ARRAY IS SORTED
arr = [1, 2, 3, 4, 5]
is_sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("\n5. Array is sorted")
else:
    print("\n5. Array is not sorted")
