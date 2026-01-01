arr = [10, 4, 23, 7, 1, 15]
print("Original Array:", arr)

# 1. FIND LARGEST AND SMALLEST ELEMENT

largest = arr[0]
smallest = arr[0]

for num in arr:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("\n1. Largest Element:", largest)
print("1. Smallest Element:", smallest)

# 2. REVERSE ARRAY WITHOUT EXTRA SPACE

start = 0
end = len(arr) - 1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print("\n2. Reversed Array:", arr)

# 3. ROTATE ARRAY BY K POSITIONS (RIGHT ROTATION)

k = 2
k = k % len(arr)

arr = arr[-k:] + arr[:-k]

print("\n3. Array after rotating by", k, "positions:", arr)

# 4. FIND SECOND LARGEST ELEMENT

largest = second_largest = -1

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("\n4. Second Largest Element:", second_largest)

# 5. REMOVE DUPLICATE ELEMENTS

arr_with_duplicates = [1, 2, 3, 2, 4, 1, 5]
unique_arr = []

for num in arr_with_duplicates:
    if num not in unique_arr:
        unique_arr.append(num)

print("\n5. Array without duplicates:", unique_arr)
