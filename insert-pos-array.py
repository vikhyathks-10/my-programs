def insert_element():
    arr = [1, 2, 4, 5]
    element = 3
    position = 3  # index starts at 1 for user logic

    if position < 1 or position > len(arr) + 1:
        print("Invalid position")
    else:
        arr.append(0)  # add dummy space
        for i in range(len(arr) - 1, position - 1, -1):
            arr[i] = arr[i - 1]
        arr[position - 1] = element
        print("Array after insertion:", arr)

insert_element()
