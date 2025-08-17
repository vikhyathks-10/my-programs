def merge_lists_without_duplicates():
    list1 = input("Enter first list elements separated by space: ").split()
    list2 = input("Enter second list elements separated by space: ").split()
    
    merged_list = []
    
    for item in list1 + list2:
        if item not in merged_list:
            merged_list.append(item)
    
    print("Merged list without duplicates:", merged_list)

merge_lists_without_duplicates()
