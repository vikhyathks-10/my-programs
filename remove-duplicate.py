def remove_duplicates():
    s = input("Enter a string: ")
    result = ""
    for char in s:
        if char not in result:
            result += char
    print("String after removing duplicates:", result)

remove_duplicates()
