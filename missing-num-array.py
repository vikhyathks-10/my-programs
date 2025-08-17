arr = [1, 2, 3, 5]
n = len(arr) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
print("Missing Number:", expected_sum - actual_sum)
