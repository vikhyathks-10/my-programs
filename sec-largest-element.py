def second_largest():
    arr = [10, 20, 4, 45, 99]
    largest = arr[0]
    second = None

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif second is None or (num > second and num != largest):
            second = num

    print(f"Second Largest: {second}")

second_largest()
