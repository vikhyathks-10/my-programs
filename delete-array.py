def delete_element():
    arr = [10, 20, 30, 40]
    position = 2  # index starts at 1 for user logic

    if position < 1 or position > len(arr):
        print("Invalid position")
    else:
        for i in range(position - 1, len(arr) - 1):
            arr[i] = arr[i + 1]
        arr.pop()
        print("Array after deletion:", arr)

delete_element()
