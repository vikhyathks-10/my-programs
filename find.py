#Find First Missing Positive
def find_missing_positive(arr):
    n = len(arr)
    # Mark numbers (1 to n) as negative
    for i in range(n):
        if 1 <= arr[i] <= n:
            arr[arr[i] - 1] = -abs(arr[arr[i] - 1])
    # The first positive index + 1 is the missing number
    for i in range(n):
        if arr[i] > 0:
            return i + 1
    return n + 1

# Example usage
arr = [3, 4, -1, 1]
print("First Missing Positive:", find_missing_positive(arr))
arr = [1, 2, 0]
print("First Missing Positive:", find_missing_positive(arr))    