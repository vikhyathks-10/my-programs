# 🔹 DAY 12 - ARRAY LOGIC PROBLEMS


# ==================================================
# 🔹 1. Majority Element
# ==================================================

def majority_element(arr):

    candidate = None
    count = 0

    for num in arr:

        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


# ==================================================
# 🔹 2. Missing Positive Number
# ==================================================

def missing_positive_number(arr):

    positive_nums = set()

    for num in arr:

        if num > 0:
            positive_nums.add(num)

    smallest = 1

    while smallest in positive_nums:
        smallest += 1

    return smallest


# ==================================================
# 🔹 3. Product of Array Except Self
# ==================================================

def product_except_self(arr):

    n = len(arr)

    result = [1] * n

    left_product = 1

    for i in range(n):

        result[i] = left_product

        left_product *= arr[i]

    right_product = 1

    for i in range(n - 1, -1, -1):

        result[i] *= right_product

        right_product *= arr[i]

    return result


# ==================================================
# 🔹 4. Move Zeros To End
# ==================================================

def move_zeros_to_end(arr):

    result = []

    zero_count = 0

    for num in arr:

        if num == 0:
            zero_count += 1
        else:
            result.append(num)

    result.extend([0] * zero_count)

    return result


# ==================================================
# 🔹 5. Rearrange Positive & Negative Numbers
# ==================================================

def rearrange_positive_negative(arr):

    positive = []
    negative = []

    for num in arr:

        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)

    return positive + negative


# ==================================================
# 🔹 MAIN PROGRAM
# ==================================================

arr1 = [2, 2, 1, 1, 2, 2, 2]

arr2 = [3, 4, -1, 1]

arr3 = [1, 2, 3, 4]

arr4 = [0, 1, 0, 3, 12]

arr5 = [1, -2, 3, -4, 5, -6]


print("🔹 Majority Element")
print(majority_element(arr1))


print("\n🔹 Missing Positive Number")
print(missing_positive_number(arr2))


print("\n🔹 Product of Array Except Self")
print(product_except_self(arr3))


print("\n🔹 Move Zeros To End")
print(move_zeros_to_end(arr4))


print("\n🔹 Rearrange Positive & Negative Numbers")
print(rearrange_positive_negative(arr5))