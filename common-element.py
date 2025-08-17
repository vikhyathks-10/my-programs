def find_common_elements():
    list1 = input("Enter first list elements separated by space: ").split()
    list2 = input("Enter second list elements separated by space: ").split()

    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)

    print("Common elements:", common)

find_common_elements()
