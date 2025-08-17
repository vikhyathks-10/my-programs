def find_max_min():
    arr = [4, 2, 9, 1, 5]
    maximum = arr[0]
    minimum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    print(f"Max: {maximum}, Min: {minimum}")

find_max_min()
