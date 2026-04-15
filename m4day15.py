# 🔹 DAY 15 - ARRAY OPERATIONS


# 🔹 1. Insert Element at Position
def insert_element(arr, pos, value):
    return arr[:pos] + [value] + arr[pos:]


# 🔹 2. Delete Element
def delete_element(arr, value):
    if value in arr:
        arr.remove(value)
    return arr


# 🔹 3. Reverse Array
def reverse_array(arr):
    return arr[::-1]


# 🔹 4. Find Max and Min
def find_max_min(arr):
    return max(arr), min(arr)


# 🔹 5. Rotate Array (Right Rotation by k)
def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]


# 🔹 MAIN PROGRAM

arr = [10, 20, 30, 40, 50]

print("\n--- Insert Element ---")
arr = insert_element(arr, 2, 25)
print(arr)


print("\n--- Delete Element ---")
arr = delete_element(arr, 30)
print(arr)


print("\n--- Reverse Array ---")
print(reverse_array(arr))


print("\n--- Max and Min ---")
mx, mn = find_max_min(arr)
print("Max:", mx, "Min:", mn)


print("\n--- Rotate Array ---")
print(rotate_array(arr, 2))