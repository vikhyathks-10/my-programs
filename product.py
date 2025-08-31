#Product of Array Except Self
def product_except_self(arr):
    n = len(arr)
    output = [1] * n
    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= arr[i]
    right_product = 1
    for i in range(n-1, -1, -1):
        output[i] *= right_product
        right_product *= arr[i]
    return output

# Example usage
arr = [1, 2, 3, 4]
print("Product of Array Except Self:", product_except_self(arr))