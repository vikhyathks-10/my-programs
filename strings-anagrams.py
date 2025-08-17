def check_anagram():
    str1 = input("Enter first string: ").replace(" ", "").lower()
    str2 = input("Enter second string: ").replace(" ", "").lower()

    if len(str1) != len(str2):
        print("Not anagrams (different lengths).")
        return

    dict1 = {}
    dict2 = {}

    for char in str1:
        dict1[char] = dict1.get(char, 0) + 1

    for char in str2:
        dict2[char] = dict2.get(char, 0) + 1

    if dict1 == dict2:
        print("The strings are anagrams.")
    else:
        print("The strings are NOT anagrams.")

check_anagram()
