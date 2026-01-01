# 1. REARRANGE ARRAY IN ALTERNATE POSITIVE AND NEGATIVE NUMBERS
arr = [1, -2, 3, -4, -1, 4]
pos = []
neg = []

for num in arr:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)

result = []
i = j = 0

while i < len(pos) and j < len(neg):
    result.append(pos[i])
    result.append(neg[j])
    i += 1
    j += 1

while i < len(pos):
    result.append(pos[i])
    i += 1

while j < len(neg):
    result.append(neg[j])
    j += 1

print("1. Rearranged Array (Alternate +ve & -ve):", result)

# 2. FIND MAJORITY ELEMENT IN AN ARRAY
# (Element appearing more than n/2 times)
arr = [2, 2, 1, 2, 3, 2, 2]
n = len(arr)
majority = -1

for i in range(n):
    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count += 1
    if count > n // 2:
        majority = arr[i]
        break

print("\n2. Majority Element:", majority)

# 3. REPLACE EVERY ELEMENT WITH GREATEST ELEMENT ON RIGHT
arr = [16, 17, 4, 3, 5, 2]
max_from_right = -1

for i in range(len(arr) - 1, -1, -1):
    temp = arr[i]
    arr[i] = max_from_right
    if temp > max_from_right:
        max_from_right = temp

print("\n3. Array after replacement:", arr)

# 4. FIND DUPLICATE ELEMENTS IN AN ARRAY
arr = [1, 2, 3, 2, 4, 1, 5]
duplicates = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

print("\n4. Duplicate elements:", duplicates)

# 5. CHECK IF TWO ARRAYS ARE EQUAL
arr1 = [1, 2, 3, 4]
arr2 = [1, 2, 3, 4]

if len(arr1) != len(arr2):
    print("\n5. Arrays are not equal")
else:
    equal = True
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            equal = False
            break

    if equal:
        print("\n5. Arrays are equal")
    else:
        print("\n5. Arrays are not equal")
