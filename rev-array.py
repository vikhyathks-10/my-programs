def reverse_array():
    arr = [1, 2, 3, 4]
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    print("Reversed Array:", arr)

reverse_array()
